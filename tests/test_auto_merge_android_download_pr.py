"""Safety checks for merging generated Android download pull requests."""

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import auto_merge_android_download_pr as merger  # noqa: E402

REPO = "inferjay/AndroidDevTools"
HEAD = "a" * 40
BASE = "b" * 40
PR = {
    "state": "open",
    "draft": False,
    "user": {"login": "github-actions[bot]"},
    "base": {"ref": "gh-pages", "sha": BASE, "repo": {"full_name": REPO}},
    "head": {"ref": "automation/android-downloads", "sha": HEAD, "repo": {"full_name": REPO}},
    "changed_files": 2,
}
FILES = [
    {"filename": "android-emulator.html", "status": "modified", "additions": 20, "deletions": 0},
    {"filename": "index.html", "status": "modified", "additions": 20, "deletions": 20},
]
SUCCESSFUL_CHECKS = {
    "total_count": 1,
    "check_runs": [
        {
            "name": "Cloudflare Pages",
            "app": {"slug": "cloudflare-workers-and-pages"},
            "status": "completed",
            "conclusion": "success",
        }
    ],
}


class AutoMergeAndroidDownloadPrTests(unittest.TestCase):
    def setUp(self) -> None:
        self.merger = merger

    def run_gate(
        self, *, pr=None, files=None, checks=None, final_pr=None, base_refs=None, review_decision=None, attempts=2
    ):
        pr = copy.deepcopy(PR if pr is None else pr)
        files = copy.deepcopy(FILES if files is None else files)
        checks = copy.deepcopy(SUCCESSFUL_CHECKS if checks is None else checks)
        final_pr = copy.deepcopy(pr if final_pr is None else final_pr)
        pr_reads = iter((pr, final_pr))
        check_reads = iter(checks) if isinstance(checks, list) else None
        base_ref_reads = iter(base_refs) if base_refs is not None else None

        def get_json(endpoint):
            if endpoint.endswith("/git/ref/heads/gh-pages"):
                return {"object": {"sha": next(base_ref_reads) if base_ref_reads is not None else BASE}}
            if endpoint.endswith("/pulls/123"):
                return next(pr_reads)
            if "/pulls/123/files" in endpoint:
                return files
            if "/check-runs" in endpoint:
                return next(check_reads) if check_reads is not None else checks
            raise AssertionError(f"Unexpected endpoint: {endpoint}")

        with (
            patch.object(self.merger, "_get_json", side_effect=get_json),
            patch.object(self.merger, "_review_decision", return_value=review_decision),
            patch.object(self.merger, "_merge") as merge,
            patch.object(self.merger.time, "sleep") as sleep,
        ):
            self.merger.merge_verified_pr(REPO, 123, HEAD, BASE, attempts=attempts)
            return merge, sleep

    def test_merges_verified_bot_pr_after_cloudflare_success(self) -> None:
        merge, sleep = self.run_gate()
        merge.assert_called_once_with(REPO, 123, HEAD)
        sleep.assert_not_called()

    def test_merges_when_no_review_is_required(self) -> None:
        merge, _ = self.run_gate(review_decision="")
        merge.assert_called_once_with(REPO, 123, HEAD)

    def test_rejects_pr_from_other_author(self) -> None:
        pr = copy.deepcopy(PR)
        pr["user"]["login"] = "another-user"
        with self.assertRaisesRegex(self.merger.MergeBlocked, "author"):
            self.run_gate(pr=pr)

    def test_rejects_unexpected_file(self) -> None:
        files = copy.deepcopy(FILES)
        files[0]["filename"] = "README.md"
        with self.assertRaisesRegex(self.merger.MergeBlocked, "files"):
            self.run_gate(files=files)

    def test_waits_for_check_on_exact_head_commit(self) -> None:
        pending = copy.deepcopy(SUCCESSFUL_CHECKS)
        pending["check_runs"][0]["status"] = "in_progress"
        pending["check_runs"][0]["conclusion"] = None
        merge, sleep = self.run_gate(checks=[pending, SUCCESSFUL_CHECKS])
        sleep.assert_called_once()
        merge.assert_called_once_with(REPO, 123, HEAD)

    def test_failed_check_blocks_merge(self) -> None:
        failed = copy.deepcopy(SUCCESSFUL_CHECKS)
        failed["check_runs"][0]["conclusion"] = "failure"
        with self.assertRaisesRegex(self.merger.MergeBlocked, "check"):
            self.run_gate(checks=failed)

    def test_missing_cloudflare_check_times_out(self) -> None:
        missing = {"total_count": 0, "check_runs": []}
        with self.assertRaisesRegex(self.merger.MergeBlocked, "Cloudflare Pages"):
            self.run_gate(checks=missing)

    def test_head_change_after_check_blocks_merge(self) -> None:
        final_pr = copy.deepcopy(PR)
        final_pr["head"]["sha"] = "c" * 40
        with self.assertRaisesRegex(self.merger.MergeBlocked, "head"):
            self.run_gate(final_pr=final_pr)

    def test_base_branch_change_after_check_blocks_merge(self) -> None:
        with self.assertRaisesRegex(self.merger.MergeBlocked, "base branch"):
            self.run_gate(base_refs=[BASE, "c" * 40])

    def test_required_review_blocks_merge(self) -> None:
        with self.assertRaisesRegex(self.merger.MergeBlocked, "review"):
            self.run_gate(review_decision="REVIEW_REQUIRED")


if __name__ == "__main__":
    unittest.main()
