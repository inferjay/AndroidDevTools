#!/usr/bin/env python3
"""Offline regression tests for the guarded Android download updater."""

from __future__ import annotations

import sys
import datetime as dt
from dataclasses import replace
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import update_android_downloads as updater  # noqa: E402


FIXTURES = ROOT / "tests" / "fixtures"


class UpdateAndroidDownloadsTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.studio_frame = (FIXTURES / "studio-frame.html").read_text(encoding="utf-8")
        cls.emulator_frame = (FIXTURES / "emulator-frame.html").read_text(encoding="utf-8")
        cls.repository_xml = (FIXTURES / "repository2.xml").read_text(encoding="utf-8")

    @staticmethod
    def _repository_package(release: updater.Release, channel: str) -> str:
        major, minor, micro = updater._release_version(release)
        archives = "".join(
            f"<archive><complete><url>{download.filename}</url>"
            f"<size>{download.size.split()[0]}</size></complete></archive>"
            for download in release.downloads
        )
        return (
            '<remotePackage path="emulator"><revision>'
            f"<major>{major}</major><minor>{minor}</minor><micro>{micro}</micro>"
            f'</revision><channelRef ref="{channel}"/><archives>{archives}</archives>'
            '</remotePackage>'
        )

    def _supersession_sources(self) -> tuple[list[updater.Release], str]:
        # Model the 2026-10-02 failure: stable 37.2.12, archived beta 37.2.11,
        # and no dedicated beta in XML. Reuse valid fixture download metadata.
        releases, _ = updater.parse_releases(self.emulator_frame, "Android Emulator")
        stable = replace(
            next(r for r in releases if r.channel == "stable"),
            name="Android Emulator (37.2.12) Stable",
            date_display="October 1, 2026", date_iso="2026-10-01",
        )
        beta = replace(
            next(r for r in releases if r.channel == "beta"),
            name="Android Emulator (37.2.11) Beta",
            date_display="October 1, 2026", date_iso="2026-10-01",
        )
        xml = '<sdk-repository>' + self._repository_package(stable, "channel-0") + '</sdk-repository>'
        return [stable, beta, *releases], xml

    def test_studio_fixture_parses_expected_count_and_latest_release(self) -> None:
        releases, duplicates = updater.parse_releases(self.studio_frame, "Android Studio")

        self.assertEqual(678, len(releases))
        self.assertEqual(1, duplicates)
        self.assertEqual("Android Studio Quail 4 | 2026.1.4 Patch 1", releases[0].name)
        self.assertEqual("September 18, 2026", releases[0].date_display)
        self.assertEqual(6, len(releases[0].downloads))

    def test_emulator_fixture_deduplicates_exact_official_duplicate(self) -> None:
        releases, duplicates = updater.parse_releases(self.emulator_frame, "Android Emulator")

        self.assertEqual(212, len(releases))
        self.assertEqual(1, duplicates)
        self.assertEqual("Android Emulator (37.2.10) Beta", releases[0].name)
        self.assertEqual("emulator-linux_x64-16349944.zip", releases[0].downloads[0].filename)

    def test_repository_xml_cross_validation_matches_stable_and_beta(self) -> None:
        releases, _ = updater.parse_releases(self.emulator_frame, "Android Emulator")

        checks = updater.validate_emulator_repository(releases, self.repository_xml)

        self.assertEqual(
            [
                {"channel": "stable", "version": "37.1.11", "status": "matched"},
                {"channel": "beta", "version": "37.2.10", "status": "matched"},
            ],
            checks,
        )

    def test_emulator_numeric_order_preserves_official_dates_and_downloads(self) -> None:
        frame = (FIXTURES / "emulator-nonmonotonic-frame.html").read_text(encoding="utf-8")
        releases, _ = updater.parse_releases(frame, "Android Emulator")
        self.assertEqual(["37.3.3", "37.3.1"], [updater._version_from_emulator_name(r.name) for r in releases])
        self.assertEqual(["2026-10-06", "2026-10-07"], [r.date_iso for r in releases])
        self.assertEqual("emulator-linux_x64-16489710.zip", releases[0].downloads[0].filename)
        self.assertEqual("a0da0fa20903a69ae52ab501f30fc5c768dcce31434cd2f55d52addc1a2c0495", releases[0].downloads[0].checksum)
        self.assertEqual(4, len(releases[1].downloads))

    def test_emulator_transition_checks_numeric_maximum_per_channel(self) -> None:
        frame = (FIXTURES / "emulator-nonmonotonic-frame.html").read_text(encoding="utf-8")
        high, low = updater.parse_releases(frame, "Android Emulator")[0]
        stable = replace(high, name="Android Emulator (37.2.12) Stable", channel="stable")
        # Unsorted old pages and a newer publication date cannot mask rollback.
        old = [low, high, stable]
        updater._validate_transition(old, [high, low, stable], "Android Emulator")
        advanced = replace(stable, name="Android Emulator (38.0.0) Stable")
        for new in ([low, advanced], [advanced], [high, low]):
            with self.subTest(new=new), self.assertRaises(updater.UpdateError):
                updater._validate_transition(old, new, "Android Emulator")
        # A date correction on the same revision is not a binary downgrade.
        corrected = replace(high, date_iso="2026-10-05")
        updater._validate_transition(old, [corrected, low, stable], "Android Emulator")
        advanced_canary = replace(high, name="Android Emulator (37.3.10) Canary", date_iso="2026-10-05")
        updater._validate_transition(old, [advanced_canary, low, stable], "Android Emulator")
        nine = replace(high, name="Android Emulator (37.3.9) Canary")
        numeric_frame = updater.render_releases("emulator", [nine, advanced_canary])
        ordered, _ = updater.parse_releases(numeric_frame, "Android Emulator", True)
        self.assertEqual(advanced_canary, ordered[0])

    def test_nonmonotonic_emulator_update_is_idempotent_and_rollback_writes_nothing(self) -> None:
        sources = updater.load_sources(True, ROOT / "scripts" / "update_android_downloads.py")
        frame = (FIXTURES / "emulator-nonmonotonic-frame.html").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as temporary_dir:
            site = Path(temporary_dir)
            for filename, marker_names in (
                ("android-studio.html", ["studio"]),
                ("android-emulator.html", ["emulator"]),
                ("index.html", ["studio-summary", "emulator-summary"]),
            ):
                parts = []
                for name in marker_names:
                    product = "studio" if name.startswith("studio") else "emulator"
                    releases, _ = updater.parse_releases(sources[0 if product == "studio" else 1], "Android " + ("Studio" if product == "studio" else "Emulator"))
                    start, end = updater.MARKERS[name]
                    parts.append(start + "\n" + updater.render_releases(product, releases) + "\n" + end)
                (site / filename).write_text("\n".join(parts), encoding="utf-8")
            with patch.object(updater, "load_sources", return_value=(sources[0], frame + sources[1], sources[2], sources[3])):
                report = updater.run_update(site, "write", True, ROOT / "scripts" / "update_android_downloads.py")
                snapshot = {name: (site / name).read_bytes() for name in updater.TARGET_FILES}
                again = updater.run_update(site, "write", True, ROOT / "scripts" / "update_android_downloads.py")
            self.assertEqual("Android Emulator (37.3.3) Canary", report["emulator"]["latest"])
            self.assertFalse(again["changed"])
            for name in ("index.html", "android-emulator.html"):
                page = snapshot[name].decode()
                self.assertLess(page.index("37.3.3"), page.index("37.3.1"))
            low = updater.parse_releases(frame, "Android Emulator")[0][1]
            rollback_frame = updater.render_releases("emulator", [low]).replace('<devsite-expandable ', '<devsite-expandable class="expandable" ')
            with patch.object(updater, "load_sources", return_value=(sources[0], rollback_frame + sources[1], sources[2], sources[3])):
                with self.assertRaises(updater.UpdateError):
                    updater.run_update(site, "write", True, ROOT / "scripts" / "update_android_downloads.py")
            self.assertEqual(snapshot, {name: (site / name).read_bytes() for name in updater.TARGET_FILES})

    def test_repository_newer_beta_rollout_is_reported_without_failing(self) -> None:
        releases, _ = updater.parse_releases(self.emulator_frame, "Android Emulator")
        newer_repository_xml = self.repository_xml.replace(
            "<micro>10</micro>\n    </revision>\n    <display-name>Android Emulator</display-name>\n"
            "    <uses-license ref=\"android-sdk-license\"/>\n    <channelRef ref=\"channel-1\"/>",
            "<micro>11</micro>\n    </revision>\n    <display-name>Android Emulator</display-name>\n"
            "    <uses-license ref=\"android-sdk-license\"/>\n    <channelRef ref=\"channel-1\"/>",
            1,
        )

        checks = updater.validate_emulator_repository(
            releases, newer_repository_xml, today=dt.date(2026, 9, 18),
        )

        self.assertEqual(
            [
                {"channel": "stable", "version": "37.1.11", "status": "matched"},
                {
                    "channel": "beta",
                    "version": "37.2.10",
                    "status": "repository-newer",
                    "repository_version": "37.2.11",
                    "archive_release_date": "2026-09-17",
                    "checked_date_utc": "2026-09-18",
                    "archive_age_days": 1,
                    "warning_threshold_days": 7,
                    "staleness_basis": "archive-age-proxy-not-observed-mismatch-duration",
                },
            ],
            checks,
        )

    def test_repository_newer_staleness_boundary_and_future_date(self) -> None:
        releases, _ = updater.parse_releases(self.emulator_frame, "Android Emulator")
        newer_xml = self.repository_xml.replace("<micro>10</micro>", "<micro>11</micro>")
        for age in (-1, 0, 6, 7, 14):
            with self.subTest(age=age):
                checks = updater.validate_emulator_repository(
                    releases, newer_xml,
                    today=dt.date(2026, 9, 17) + dt.timedelta(days=age),
                )
                beta = checks[1]
                self.assertEqual("repository-newer", beta["status"])
                self.assertEqual(age, beta["archive_age_days"])
                self.assertEqual(age >= 7, "warning" in beta)
                self.assertNotIn("warning", checks[0])
                if age >= 7:
                    self.assertIn("not confirmed mismatch duration", beta["warning"])

    def test_old_matched_release_has_no_staleness_warning(self) -> None:
        releases, _ = updater.parse_releases(self.emulator_frame, "Android Emulator")
        checks = updater.validate_emulator_repository(
            releases, self.repository_xml, today=dt.date(2027, 1, 1),
        )
        self.assertTrue(all(check["status"] == "matched" for check in checks))
        self.assertTrue(all("warning" not in check for check in checks))

    def test_fresh_archive_rollover_clears_warning(self) -> None:
        releases, _ = updater.parse_releases(self.emulator_frame, "Android Emulator")
        newer_xml = self.repository_xml.replace("<micro>10</micro>", "<micro>11</micro>")
        releases = [replace(r, date_iso="2026-10-01") if r.channel == "beta" else r for r in releases]
        checks = updater.validate_emulator_repository(
            releases, newer_xml, today=dt.date(2026, 10, 1),
        )
        self.assertEqual("repository-newer", checks[1]["status"])
        self.assertNotIn("warning", checks[1])

    def test_repository_older_beta_rollout_still_fails_closed(self) -> None:
        releases, _ = updater.parse_releases(self.emulator_frame, "Android Emulator")
        older_repository_xml = self.repository_xml.replace(
            "<micro>10</micro>\n    </revision>\n    <display-name>Android Emulator</display-name>\n"
            "    <uses-license ref=\"android-sdk-license\"/>\n    <channelRef ref=\"channel-1\"/>",
            "<micro>9</micro>\n    </revision>\n    <display-name>Android Emulator</display-name>\n"
            "    <uses-license ref=\"android-sdk-license\"/>\n    <channelRef ref=\"channel-1\"/>",
            1,
        )

        with self.assertRaisesRegex(updater.UpdateError, "未找到 beta Emulator 37.2.10"):
            updater.validate_emulator_repository(releases, older_repository_xml)

    def test_absent_beta_is_reported_as_superseded_by_matched_stable(self) -> None:
        releases, xml = self._supersession_sources()

        checks = updater.validate_emulator_repository(releases, xml, today=dt.date(2027, 1, 1))

        self.assertEqual({"channel": "stable", "version": "37.2.12", "status": "matched"}, checks[0])
        beta = checks[1]
        self.assertEqual("37.2.11", beta["version"])
        self.assertEqual("beta-superseded-by-stable", beta["status"])
        self.assertEqual("stable", beta["repository_channel"])
        self.assertEqual("37.2.12", beta["repository_version"])
        self.assertEqual("2026-10-01", beta["archive_release_date"])
        self.assertEqual("2026-10-01", beta["archive_stable_release_date"])
        self.assertIn("metadata was not matched", beta["warning"])
        self.assertIn("not archive-newer rollout-lag tolerance", beta["warning"])

    def test_supersession_requires_independently_matched_newer_stable(self) -> None:
        releases, xml = self._supersession_sources()
        stable, beta = releases[:2]
        cases = {
            "stable older than beta": ([stable, replace(beta, name="Android Emulator (37.2.13) Beta")], xml),
            "same version": ([stable, replace(beta, name="Android Emulator (37.2.12) Beta")], xml),
            "beta published later": ([stable, replace(beta, date_iso="2026-10-02")], xml),
            "stable absent from archive": ([beta], xml),
            "stable only repository-newer": (releases, xml.replace("<micro>12</micro>", "<micro>13</micro>")),
            "only higher channel available": (releases, xml.replace('ref="channel-0"', 'ref="channel-2"')),
        }
        for case, (candidates, repository) in cases.items():
            with self.subTest(case=case), self.assertRaisesRegex(updater.UpdateError, "未找到"):
                updater.validate_emulator_repository(candidates, repository)

    def test_existing_older_beta_package_does_not_use_stable_fallback(self) -> None:
        releases, xml = self._supersession_sources()
        old_beta = next(r for r in releases[2:] if r.channel == "beta")
        xml = xml.replace('</sdk-repository>', self._repository_package(old_beta, "channel-1") + '</sdk-repository>')

        with self.assertRaisesRegex(updater.UpdateError, "未找到 beta Emulator 37.2.11"):
            updater.validate_emulator_repository(releases, xml)

    def test_exact_beta_match_and_mismatches_take_priority_over_supersession(self) -> None:
        releases, xml = self._supersession_sources()
        beta = releases[1]
        beta_package = self._repository_package(beta, "channel-1")
        exact_xml = xml.replace('</sdk-repository>', beta_package + '</sdk-repository>')
        checks = updater.validate_emulator_repository(releases, exact_xml)
        self.assertEqual({"channel": "beta", "version": "37.2.11", "status": "matched"}, checks[1])
        for corrupted_package in (
            beta_package.replace(beta.downloads[0].filename, "missing.zip"),
            beta_package.replace(beta.downloads[0].size.split()[0], "1"),
        ):
            with self.subTest(package=corrupted_package[:100]), self.assertRaises(updater.UpdateError):
                updater.validate_emulator_repository(
                    releases, xml.replace('</sdk-repository>', corrupted_package + '</sdk-repository>'),
                )

    def test_stable_download_mismatches_still_fail_before_supersession(self) -> None:
        releases, xml = self._supersession_sources()
        stable = releases[0]
        for corrupted_xml in (
            xml.replace(stable.downloads[0].filename, "missing.zip"),
            xml.replace(stable.downloads[0].size.split()[0], "1"),
        ):
            with self.subTest(xml=corrupted_xml[:100]), self.assertRaises(updater.UpdateError):
                updater.validate_emulator_repository(releases, corrupted_xml)

    def test_incomplete_beta_entry_is_not_treated_as_absent(self) -> None:
        releases, xml = self._supersession_sources()
        beta_package = self._repository_package(releases[1], "channel-1")
        incomplete_package = beta_package[:beta_package.index('<archives>')] + '</remotePackage>'
        incomplete_xml = xml.replace('</sdk-repository>', incomplete_package + '</sdk-repository>')
        for invalid_xml in (incomplete_xml, '<broken', '<sdk-repository/>'):
            with self.subTest(xml=invalid_xml[:100]), self.assertRaises(updater.UpdateError):
                updater.validate_emulator_repository(releases, invalid_xml)

    def test_superseded_beta_keeps_archive_download_validation(self) -> None:
        releases, _ = self._supersession_sources()
        beta = releases[1]
        for invalid_download in (
            replace(beta.downloads[0], url="https://example.invalid/emulator.zip"),
            replace(beta.downloads[0], checksum=""),
            replace(beta.downloads[0], size=""),
        ):
            invalid_beta = replace(beta, downloads=(invalid_download, *beta.downloads[1:]))
            frame = updater.render_releases("emulator", [releases[0], invalid_beta])
            with self.subTest(download=invalid_download), self.assertRaises(updater.UpdateError):
                updater.parse_releases(frame, "Android Emulator", accept_all_devsite_expandables=True)

    def test_download_validation_rejects_untrusted_host(self) -> None:
        download = updater.Download(
            platform="Linux",
            url="https://example.invalid/android.zip",
            filename="android.zip",
            size="1 MB",
            checksum="a" * 64,
            group="Zip files",
        )

        with self.assertRaises(updater.UpdateError):
            updater._validate_download(download, "test")

    def test_download_validation_rejects_missing_checksum(self) -> None:
        download = updater.Download(
            platform="Linux",
            url="https://dl.google.com/android/repository/android.zip",
            filename="android.zip",
            size="1 MB",
            checksum="",
            group="Zip files",
        )

        with self.assertRaises(updater.UpdateError):
            updater._validate_download(download, "test")

    def test_rendering_uses_stable_id_and_escapes_markup(self) -> None:
        release = updater.Release(
            name="Android Studio Quail 4 | 2026.1.4 <Patch>",
            date_display="September 18, 2026",
            date_iso="2026-09-18",
            channel="stable",
            downloads=(
                updater.Download(
                    platform="Mac <Intel>",
                    url="https://dl.google.com/android/repository/file?a=1&b=2",
                    filename="file.zip",
                    size="1 MB",
                    checksum="b" * 64,
                    group="Zip files",
                ),
            ),
        )

        rendered = updater.render_release("studio", release)

        self.assertIn('id="studio-2026-1-4-stable"', rendered)
        self.assertIn("Mac &lt;Intel&gt;", rendered)
        self.assertIn("a=1&amp;b=2", rendered)
        self.assertNotIn("<Patch>", rendered)

    def test_marker_replacement_preserves_surrounding_page(self) -> None:
        start, end = updater.MARKERS["studio"]
        original = f"prefix\n{start}\nold\n{end}\nsuffix"

        replaced = updater._replace_marker(original, "studio", "new")

        self.assertEqual(f"prefix\n{start}\nnew\n{end}\nsuffix", replaced)
        with self.assertRaises(updater.UpdateError):
            updater._replace_marker(f"{original}\n{start}", "studio", "new")

    def test_bootstrap_then_write_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as temporary_dir:
            site_dir = Path(temporary_dir)
            (site_dir / "android-studio.html").write_text(
                '<div class="all-downloads"><p>keep archive chrome</p></div>\n',
                encoding="utf-8",
            )
            (site_dir / "android-emulator.html").write_text(
                '<div class="all-downloads"><p>keep archive emulator</p></div>\n',
                encoding="utf-8",
            )
            (site_dir / "index.html").write_text(
                '<div id="android-studio"><h2>Studio</h2>\n'
                '<devsite-expandable><p>old studio</p></devsite-expandable>\n'
                '<center><a class="btn btn-large btn-action" href="android-studio.html">more</a></center>\n'
                '</div>\n'
                '<div id="android-emulator"><h2>Emulator</h2>\n'
                '<devsite-expandable><p>old emulator</p></devsite-expandable>\n'
                '<center><a class="btn btn-large btn-action" href="android-emulator.html">more</a></center>\n'
                '</div>\n',
                encoding="utf-8",
            )

            first = updater.run_update(
                site_dir=site_dir,
                mode="bootstrap",
                offline_fixtures=True,
                script_path=ROOT / "scripts" / "update_android_downloads.py",
            )
            snapshot = {name: (site_dir / name).read_bytes() for name in updater.TARGET_FILES}
            second = updater.run_update(
                site_dir=site_dir,
                mode="write",
                offline_fixtures=True,
                script_path=ROOT / "scripts" / "update_android_downloads.py",
            )
            third = updater.run_update(
                site_dir=site_dir,
                mode="check",
                offline_fixtures=True,
                script_path=ROOT / "scripts" / "update_android_downloads.py",
            )

            self.assertEqual(list(updater.TARGET_FILES), first["changed_files"])
            self.assertFalse(second["changed"])
            self.assertFalse(third["changed"])
            self.assertEqual(snapshot, {name: (site_dir / name).read_bytes() for name in updater.TARGET_FILES})

            # A stale warning must survive a no-change write without touching pages.
            sources = updater.load_sources(True, ROOT / "scripts" / "update_android_downloads.py")
            newer_xml = sources[2].replace("<micro>10</micro>", "<micro>11</micro>")
            validate = updater.validate_emulator_repository
            with patch.object(updater, "load_sources", return_value=(sources[0], sources[1], newer_xml, sources[3])), patch.object(
                updater, "validate_emulator_repository",
                side_effect=lambda releases, xml: validate(releases, xml, today=dt.date(2026, 10, 1)),
            ):
                stale = updater.run_update(site_dir, "write", True, ROOT / "scripts" / "update_android_downloads.py")
            self.assertFalse(stale["changed"])
            self.assertEqual("repository-newer", stale["repository_cross_validation"][1]["status"])
            self.assertIn("warning", stale["repository_cross_validation"][1])
            self.assertEqual(snapshot, {name: (site_dir / name).read_bytes() for name in updater.TARGET_FILES})

            # Supersession must allow a real page update and still report on a
            # subsequent no-change run, without altering the write allowlist.
            releases, xml = self._supersession_sources()
            frame = updater.render_releases("emulator", releases).replace(
                '<devsite-expandable ', '<devsite-expandable class="expandable" ',
            )
            with patch.object(updater, "load_sources", return_value=(sources[0], frame, xml, sources[3])):
                promoted = updater.run_update(site_dir, "write", True, ROOT / "scripts" / "update_android_downloads.py")
                promoted_snapshot = {name: (site_dir / name).read_bytes() for name in updater.TARGET_FILES}
                no_change = updater.run_update(site_dir, "write", True, ROOT / "scripts" / "update_android_downloads.py")
            self.assertEqual(["android-emulator.html", "index.html"], promoted["changed_files"])
            self.assertFalse(no_change["changed"])
            self.assertEqual("beta-superseded-by-stable", no_change["repository_cross_validation"][1]["status"])
            self.assertIn("warning", no_change["repository_cross_validation"][1])
            self.assertEqual(promoted_snapshot, {name: (site_dir / name).read_bytes() for name in updater.TARGET_FILES})

            # A validation failure in write mode must not partially write pages.
            invalid_xml = xml.replace(releases[0].downloads[0].size.split()[0], "1")
            with patch.object(updater, "load_sources", return_value=(sources[0], frame, invalid_xml, sources[3])):
                with self.assertRaises(updater.UpdateError):
                    updater.run_update(site_dir, "write", True, ROOT / "scripts" / "update_android_downloads.py")
            self.assertEqual(promoted_snapshot, {name: (site_dir / name).read_bytes() for name in updater.TARGET_FILES})


if __name__ == "__main__":
    unittest.main()
