#!/usr/bin/env python3
"""Offline regression tests for the guarded Android download updater."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


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


if __name__ == "__main__":
    unittest.main()
