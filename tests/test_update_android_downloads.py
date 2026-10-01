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


if __name__ == "__main__":
    unittest.main()
