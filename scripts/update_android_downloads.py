#!/usr/bin/env python3
"""Fetch, validate, render, and safely update Android download pages.

The script deliberately uses only the Python standard library so that the
scheduled GitHub Action does not need to install a parser or other runtime
dependency.  The official archive pages expose a small HTML ``.frame``
document; that document is parsed with :class:`html.parser.HTMLParser`, while
the repository XML is parsed with :mod:`xml.etree.ElementTree`.
"""

from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Iterable, Mapping, Sequence
from xml.etree import ElementTree as ET


STUDIO_ARCHIVE_URL = "https://developer.android.com/studio/archive"
EMULATOR_ARCHIVE_URL = "https://developer.android.com/studio/emulator_archive"
REPOSITORY_URL = "https://dl.google.com/android/repository/repository2-3.xml"
ALLOWED_DOWNLOAD_HOSTS = {
    "edgedl.me.gvt1.com",
    "redirector.gvt1.com",
    "dl.google.com",
}
TARGET_FILES = (
    "android-studio.html",
    "android-emulator.html",
    "index.html",
)
MARKERS = {
    "studio": (
        "<!-- android-downloads:auto:studio:start -->",
        "<!-- android-downloads:auto:studio:end -->",
    ),
    "emulator": (
        "<!-- android-downloads:auto:emulator:start -->",
        "<!-- android-downloads:auto:emulator:end -->",
    ),
    "studio-summary": (
        "<!-- android-downloads:auto:studio-summary:start -->",
        "<!-- android-downloads:auto:studio-summary:end -->",
    ),
    "emulator-summary": (
        "<!-- android-downloads:auto:emulator-summary:start -->",
        "<!-- android-downloads:auto:emulator-summary:end -->",
    ),
}
MIN_COUNT_RATIO = 0.8
MAX_DIFF_LINES = 2000
USER_AGENT = "AndroidDevTools-download-updater/1.0 (+https://github.com/inferjay/AndroidDevTools)"
DATE_RE = re.compile(
    r"\b(?:January|February|March|April|May|June|July|August|September|October|November|December|"
    r"Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+\d{1,2},\s+\d{4}\b"
)
CHECKSUM_RE = re.compile(r"\b[0-9a-fA-F]{64}\b")
VERSION_RE = re.compile(r"\d+(?:\.\d+)+")


class UpdateError(RuntimeError):
    """An expected validation or update failure that must fail closed."""


@dataclass(frozen=True)
class Download:
    platform: str
    url: str
    filename: str
    size: str
    checksum: str
    group: str

    def fingerprint(self) -> tuple[str, str, str, str, str]:
        return (self.platform, self.url, self.filename, self.size, self.checksum)


@dataclass(frozen=True)
class Release:
    name: str
    date_display: str
    date_iso: str
    channel: str
    downloads: tuple[Download, ...]

    def identity(self) -> tuple[str, str]:
        return (self.name, self.date_iso)

    def fingerprint(self) -> tuple[tuple[str, str, str, str, str], ...]:
        return tuple(download.fingerprint() for download in self.downloads)


def _normalise_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def _parse_date(value: str) -> dt.date:
    for fmt in ("%B %d, %Y", "%b %d, %Y"):
        try:
            return dt.datetime.strptime(value, fmt).date()
        except ValueError:
            pass
    raise UpdateError(f"无法解析发布日期: {value!r}")


def _infer_channel(name: str, class_name: str = "") -> str:
    value = f"{class_name} {name}".lower()
    if "canary" in value:
        return "canary"
    if "beta" in value:
        return "beta"
    if re.search(r"\brc(?:\s*\d+)?\b", value):
        return "rc"
    return "stable"


def _platform_from_prefix(prefix: str, filename: str) -> str:
    prefix = _normalise_space(prefix).rstrip(":").strip()
    if prefix:
        return prefix
    if "linux" in filename:
        return "Linux"
    if "windows" in filename:
        return "Windows (64-bit)"
    if "aarch64" in filename or "arm" in filename:
        return "Mac (Apple Silicon)"
    if "darwin" in filename or "mac" in filename:
        return "Mac (Intel)"
    return "Download"


def _download_group(url: str) -> str:
    return "Installers" if "/install/" in url else "Zip files"


class FrameParser(HTMLParser):
    """Parse expandable release blocks from an official archive frame."""

    def __init__(self, accept_all_devsite_expandables: bool = False) -> None:
        super().__init__(convert_charrefs=True)
        self.accept_all_devsite_expandables = accept_all_devsite_expandables
        self.blocks: list[dict[str, object]] = []
        self.current: dict[str, object] | None = None
        self.container_tag = ""
        self.container_depth = 0
        self.current_link: dict[str, object] | None = None
        self.last_closed_link: dict[str, object] | None = None
        self.line_buffer = ""

    @staticmethod
    def _attrs(attrs: Sequence[tuple[str, str | None]]) -> dict[str, str]:
        return {key: value or "" for key, value in attrs}

    def _is_container(self, tag: str, attrs: Mapping[str, str]) -> bool:
        if tag == "section":
            return "expandable" in attrs.get("class", "").split()
        if tag == "devsite-expandable":
            return self.accept_all_devsite_expandables or "expandable" in attrs.get("class", "").split()
        return False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        attr_map = self._attrs(attrs)
        if self.current is None and self._is_container(tag, attr_map):
            self.current = {
                "text": [],
                "links": [],
                "class": attr_map.get("class", ""),
            }
            self.container_tag = tag
            self.container_depth = 1
            self.current_link = None
            self.last_closed_link = None
            self.line_buffer = ""
            return

        if self.current is None:
            return
        if tag == self.container_tag:
            self.container_depth += 1
        if tag == "a":
            link: dict[str, object] = {
                "href": attr_map.get("href", ""),
                "text": [],
                "prefix": self.line_buffer.strip(),
                "trailing": [],
            }
            links = self.current["links"]
            assert isinstance(links, list)
            links.append(link)
            self.current_link = link
            self.last_closed_link = None

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if self.current is None:
            return
        if tag == "a" and self.current_link is not None:
            link_text = _normalise_space("".join(self.current_link["text"]))
            prefix = str(self.current_link["prefix"])
            self.line_buffer = _normalise_space(f"{prefix} {link_text}")
            self.last_closed_link = self.current_link
            self.current_link = None
        if tag == self.container_tag:
            self.container_depth -= 1
            if self.container_depth == 0:
                current = self.current
                self.current = None
                self._finish_block(current)

    def handle_data(self, data: str) -> None:
        if self.current is None:
            return
        text = self.current["text"]
        assert isinstance(text, list)
        text.append(data)
        if self.current_link is not None:
            link_text = self.current_link["text"]
            assert isinstance(link_text, list)
            link_text.append(data)
            return
        if self.last_closed_link is not None:
            trailing = self.last_closed_link["trailing"]
            assert isinstance(trailing, list)
            trailing.append(data)
        if "\n" in data:
            self.line_buffer = data.rsplit("\n", 1)[-1]
        else:
            self.line_buffer += data

    def _finish_block(self, block: Mapping[str, object]) -> None:
        raw_text = "".join(str(item) for item in block["text"])
        lines = [_normalise_space(line) for line in raw_text.splitlines()]
        lines = [line for line in lines if line]
        name = next(
            (line for line in lines if line.startswith("Android Studio") or line.startswith("Android Emulator")),
            "",
        )
        if not name:
            match = re.search(r"(Android (?:Studio|Emulator)[^\n]+)", raw_text)
            name = _normalise_space(match.group(1)) if match else ""
        date_match = DATE_RE.search(raw_text)
        date_display = date_match.group(0) if date_match else ""
        links: list[Download] = []
        checksum_map: dict[str, str] = {}
        normalised_text = _normalise_space(raw_text)
        checksum_pairs = re.findall(r"\b([0-9a-fA-F]{64})\s+([^\s]+)", normalised_text)
        for checksum, filename in checksum_pairs:
            checksum_map[filename] = checksum.lower()

        raw_links = block["links"]
        assert isinstance(raw_links, list)
        for link_index, raw_link in enumerate(raw_links):
            href = str(raw_link.get("href", ""))
            filename = Path(urllib.parse.urlsplit(href).path).name
            link_text = _normalise_space("".join(raw_link.get("text", [])))
            if not filename:
                filename = link_text
            trailing = _normalise_space("".join(raw_link.get("trailing", [])))
            size_match = re.search(r"\(([^)]*(?:bytes|[KMGT]?B))\)", trailing, re.IGNORECASE)
            size = _normalise_space(size_match.group(1)) if size_match else ""
            checksum = checksum_map.get(filename, "")
            # A small number of historical official frame entries contain a
            # stale filename beside an otherwise valid checksum.  Keep the
            # source order as a guarded fallback, but only when the frame has
            # exactly one checksum for every download.  A missing checksum or
            # a count mismatch still fails closed below.
            if not checksum and len(checksum_pairs) == len(raw_links) and link_index < len(checksum_pairs):
                checksum = checksum_pairs[link_index][0].lower()
            links.append(
                Download(
                    platform=_platform_from_prefix(str(raw_link.get("prefix", "")), filename),
                    url=href,
                    filename=filename,
                    size=size,
                    checksum=checksum,
                    group=_download_group(href),
                )
            )
        class_name = str(block.get("class", ""))
        self.blocks.append(
            {
                "name": name,
                "date_display": date_display,
                "channel": _infer_channel(name, class_name),
                "downloads": tuple(links),
            }
        )


def _validate_download(download: Download, context: str) -> None:
    parsed = urllib.parse.urlsplit(download.url)
    if parsed.scheme != "https" or parsed.hostname not in ALLOWED_DOWNLOAD_HOSTS:
        raise UpdateError(f"{context}: 不允许的下载域名: {download.url}")
    if not download.filename:
        raise UpdateError(f"{context}: 下载文件名为空")
    if not download.size:
        raise UpdateError(f"{context}: 缺少文件大小: {download.filename}")
    if not CHECKSUM_RE.fullmatch(download.checksum):
        raise UpdateError(f"{context}: 缺少或格式错误的 SHA-256: {download.filename}")


def _validate_release(raw: Mapping[str, object], index: int, kind: str) -> Release:
    name = _normalise_space(str(raw.get("name", "")))
    date_display = _normalise_space(str(raw.get("date_display", "")))
    if not name:
        raise UpdateError(f"{kind} 第 {index + 1} 个条目缺少版本名")
    if not date_display:
        raise UpdateError(f"{kind} {name} 缺少发布日期")
    date = _parse_date(date_display)
    raw_downloads = raw.get("downloads", ())
    assert isinstance(raw_downloads, tuple)
    if not raw_downloads:
        raise UpdateError(f"{kind} {name} 没有下载项")
    downloads = tuple(raw_downloads)
    for download in downloads:
        _validate_download(download, f"{kind} {name}")
    return Release(
        name=name,
        date_display=date_display,
        date_iso=date.isoformat(),
        channel=str(raw.get("channel", "stable")),
        downloads=downloads,
    )


def parse_releases(source: str, kind: str, accept_all_devsite_expandables: bool = False) -> tuple[list[Release], int]:
    parser = FrameParser(accept_all_devsite_expandables=accept_all_devsite_expandables)
    parser.feed(source)
    parser.close()
    if not parser.blocks:
        raise UpdateError(f"{kind} frame 中没有找到 expandable 条目")
    parsed = [_validate_release(block, index, kind) for index, block in enumerate(parser.blocks)]
    unique: list[Release] = []
    by_identity: dict[tuple[str, str], Release] = {}
    duplicate_count = 0
    for release in parsed:
        previous = by_identity.get(release.identity())
        if previous is None:
            by_identity[release.identity()] = release
            unique.append(release)
            continue
        if previous.fingerprint() != release.fingerprint():
            raise UpdateError(f"{kind} 出现相同版本但下载元数据不同: {release.name} / {release.date_iso}")
        duplicate_count += 1
    return unique, duplicate_count


def _release_version(release: Release) -> tuple[int, ...]:
    match = VERSION_RE.search(release.name)
    return tuple(int(value) for value in match.group(0).split(".")) if match else ()


def _release_order_key(release: Release) -> tuple[str, tuple[int, ...], str]:
    return (release.date_iso, _release_version(release), release.name)


def _release_id(product: str, release: Release) -> str:
    version = VERSION_RE.search(release.name)
    version_slug = re.sub(r"[^a-z0-9]+", "-", version.group(0).lower()) if version else "unknown"
    channel = release.channel
    suffix_match = re.search(r"(?:patch|rc|canary|beta)\s*(\d+)", release.name, re.IGNORECASE)
    suffix = f"-{channel}-{suffix_match.group(1)}" if suffix_match else f"-{channel}"
    return f"{product}-{version_slug}{suffix}".replace("--", "-")


def _render_download_group(downloads: Iterable[Download]) -> list[str]:
    items = list(downloads)
    if not items:
        return []
    lines = [f"                {items[0].group}"]
    for download in items:
        lines.append(
            f"                {html.escape(download.platform)}: <a href=\"{html.escape(download.url, quote=True)}\">"
            f"{html.escape(download.filename)}</a> ({html.escape(download.size)})"
        )
    lines.append("")
    lines.append("                SHA-256 checksums")
    for download in items:
        lines.append(f"                {download.checksum} {html.escape(download.filename)}")
    return lines


def render_release(product: str, release: Release) -> str:
    release_id = _release_id(product, release)
    lines = [
        f'            <devsite-expandable is-upgraded="" id="{release_id}">',
        f'              <p class="expand-control" aria-controls="{release_id}" aria-expanded="false" tabindex="0" role="button">',
        f"                {html.escape(release.name)}",
        f"                <span>{html.escape(release.date_display)}</span>",
        "              </p>",
        "              <div class=\"downloads\">",
    ]
    groups: list[str] = []
    for download in release.downloads:
        if download.group not in groups:
            groups.append(download.group)
    for group in groups:
        lines.extend(_render_download_group(download for download in release.downloads if download.group == group))
        lines.append("")
    if lines[-1] == "":
        lines.pop()
    lines.extend(["              </div>", "            </devsite-expandable>"])
    return "\n".join(lines)


def render_releases(product: str, releases: Sequence[Release]) -> str:
    return "\n\n".join(render_release(product, release) for release in releases)


def _find_matching_tag(text: str, opening_start: int, tag_name: str) -> tuple[int, int]:
    token = re.compile(rf"<(/?){re.escape(tag_name)}\b[^>]*>", re.IGNORECASE)
    depth = 0
    for match in token.finditer(text, opening_start):
        if match.group(1):
            depth -= 1
            if depth == 0:
                return match.start(), match.end()
        else:
            depth += 1
    raise UpdateError(f"未找到匹配的 </{tag_name}>")


def _replace_marker(text: str, marker_name: str, body: str) -> str:
    start, end = MARKERS[marker_name]
    if text.count(start) != 1 or text.count(end) != 1:
        raise UpdateError(f"{marker_name} 生成区块标记缺失或重复")
    start_index = text.index(start) + len(start)
    end_index = text.index(end)
    if end_index < start_index:
        raise UpdateError(f"{marker_name} 生成区块标记顺序错误")
    end_line_start = text.rfind("\n", 0, end_index) + 1
    return text[:start_index] + "\n" + body.rstrip() + "\n" + text[end_line_start:]


def _marked_body(text: str, marker_name: str) -> str:
    start, end = MARKERS[marker_name]
    if text.count(start) != 1 or text.count(end) != 1:
        raise UpdateError(f"{marker_name} 生成区块标记缺失或重复")
    begin = text.index(start) + len(start)
    finish = text.index(end)
    if finish < begin:
        raise UpdateError(f"{marker_name} 生成区块标记顺序错误")
    return text[begin:finish]


def _replace_all_downloads_container(page: str, marker_name: str, body: str) -> str:
    opening = re.search(r'<div\b[^>]*class=["\'][^"\']*\ball-downloads\b[^"\']*["\'][^>]*>', page, re.IGNORECASE)
    if opening is None:
        raise UpdateError(f"页面中没有找到 all-downloads 容器: {marker_name}")
    closing_start, _ = _find_matching_tag(page, opening.start(), "div")
    marker_start, marker_end = MARKERS[marker_name]
    replacement = f"\n{marker_start}\n{body.rstrip()}\n{marker_end}\n          "
    return page[: opening.end()] + replacement + page[closing_start:]


def _replace_index_section(page: str, section_id: str, marker_name: str, product: str, releases: Sequence[Release]) -> str:
    opening = re.search(
        rf'<div\b[^>]*id=["\']{re.escape(section_id)}["\'][^>]*>', page, re.IGNORECASE
    )
    if opening is None:
        raise UpdateError(f"首页缺少区块: {section_id}")
    closing_start, _ = _find_matching_tag(page, opening.start(), "div")
    section = page[opening.end() : closing_start]
    first_expandable = re.search(r"<devsite-expandable\b", section, re.IGNORECASE)
    if first_expandable is None:
        raise UpdateError(f"首页 {section_id} 缺少可展开下载项")
    target_link = "android-studio.html" if product == "studio" else "android-emulator.html"
    call_to_action = section.find(f'<center><a class="btn btn-large btn-action" href="{target_link}">')
    if call_to_action < 0:
        raise UpdateError(f"首页 {section_id} 缺少版本页链接")
    marker_start, marker_end = MARKERS[marker_name]
    body = render_releases(product, list(releases)[:2])
    replacement = f"\n                    {marker_start}\n{body}\n                    {marker_end}\n                    <br>\n"
    new_section = section[: first_expandable.start()] + replacement + "                    " + section[call_to_action:]
    return page[: opening.end()] + new_section + page[closing_start:]


def bootstrap_site(site_dir: Path, studio: Sequence[Release], emulator: Sequence[Release]) -> list[str]:
    """Add markers and perform the one-time initial migration."""
    paths = {name: site_dir / name for name in TARGET_FILES}
    pages = {name: path.read_text(encoding="utf-8") for name, path in paths.items()}
    if any(any(pages[name].count(marker) for marker in markers) for name, markers in (("android-studio.html", MARKERS["studio"]), ("android-emulator.html", MARKERS["emulator"]), ("index.html", MARKERS["studio-summary"]), ("index.html", MARKERS["emulator-summary"]))):
        raise UpdateError("bootstrap 只能用于尚未添加生成区块标记的页面")
    pages["android-studio.html"] = _replace_all_downloads_container(
        pages["android-studio.html"], "studio", render_releases("studio", studio)
    )
    pages["android-emulator.html"] = _replace_all_downloads_container(
        pages["android-emulator.html"], "emulator", render_releases("emulator", emulator)
    )
    pages["index.html"] = _replace_index_section(
        pages["index.html"], "android-studio", "studio-summary", "studio", studio
    )
    pages["index.html"] = _replace_index_section(
        pages["index.html"], "android-emulator", "emulator-summary", "emulator", emulator
    )
    changed: list[str] = []
    for name, page in pages.items():
        if page != paths[name].read_text(encoding="utf-8"):
            paths[name].write_text(page, encoding="utf-8")
            changed.append(name)
    return changed


def _validate_transition(old: Sequence[Release], new: Sequence[Release], kind: str) -> None:
    if not old:
        return
    minimum = max(1, int(len(old) * MIN_COUNT_RATIO))
    if len(new) < minimum:
        raise UpdateError(f"{kind} 条目数异常下降: 旧 {len(old)}，新 {len(new)}，最低允许 {minimum}")
    if _release_order_key(new[0]) < _release_order_key(old[0]):
        raise UpdateError(f"{kind} 最新版本倒退: 旧 {old[0].name}，新 {new[0].name}")


def parse_repository_emulator(xml_text: str) -> list[dict[str, object]]:
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError as exc:
        raise UpdateError(f"Repository XML 解析失败: {exc}") from exc
    packages: list[dict[str, object]] = []
    for package in root.iter():
        if not package.tag.endswith("remotePackage") or package.attrib.get("path") != "emulator":
            continue
        revision = ".".join(
            element.text.strip()
            for element in package.iter()
            if element.tag.endswith(("major", "minor", "micro")) and element.text
        )
        channel = ""
        for element in package.iter():
            if element.tag.endswith("channelRef"):
                channel = element.attrib.get("ref", "")
                break
        archives: dict[str, int] = {}
        for archive in package.iter():
            if not archive.tag.endswith("archive"):
                continue
            url_element = next((item for item in archive.iter() if item.tag.endswith("url")), None)
            size_element = next((item for item in archive.iter() if item.tag.endswith("size")), None)
            if url_element is None or size_element is None or not url_element.text or not size_element.text:
                continue
            try:
                archives[Path(url_element.text.strip()).name] = int(size_element.text.strip())
            except ValueError as exc:
                raise UpdateError(f"Repository XML 的 emulator size 不是整数: {size_element.text!r}") from exc
        if revision and channel and archives:
            packages.append({"revision": revision, "channel": channel, "archives": archives})
    if not packages:
        raise UpdateError("Repository XML 中没有找到 emulator 包")
    return packages


def _version_from_emulator_name(name: str) -> str:
    match = VERSION_RE.search(name)
    if not match:
        raise UpdateError(f"无法从 Emulator 版本名解析版本号: {name}")
    return match.group(0)


def _version_key(version: str) -> tuple[int, ...]:
    return tuple(int(part) for part in version.split("."))


def validate_emulator_repository(releases: Sequence[Release], xml_text: str) -> list[dict[str, str]]:
    packages = parse_repository_emulator(xml_text)
    checks: list[dict[str, str]] = []
    for channel, channel_ref in (("stable", "channel-0"), ("beta", "channel-1")):
        candidate = next((release for release in releases if release.channel == channel), None)
        if candidate is None:
            continue
        version = _version_from_emulator_name(candidate.name)
        package = next(
            (item for item in packages if item["revision"] == version and item["channel"] == channel_ref),
            None,
        )
        if package is None:
            newer_packages = [
                item
                for item in packages
                if item["channel"] == channel_ref
                and _version_key(str(item["revision"])) > _version_key(version)
            ]
            if newer_packages:
                repository_version = max(
                    (str(item["revision"]) for item in newer_packages),
                    key=_version_key,
                )
                checks.append(
                    {
                        "channel": channel,
                        "version": version,
                        "status": "repository-newer",
                        "repository_version": repository_version,
                    }
                )
                continue
            raise UpdateError(f"Repository XML 未找到 {channel} Emulator {version} 的交叉校验包")
        archives = package["archives"]
        assert isinstance(archives, dict)
        for download in candidate.downloads:
            if download.filename not in archives:
                raise UpdateError(f"Repository XML 缺少 {download.filename}")
            size_match = re.search(r"\d+", download.size)
            if size_match is None or int(size_match.group(0)) != archives[download.filename]:
                raise UpdateError(
                    f"Repository XML 与归档页大小不一致: {download.filename} "
                    f"({download.size} != {archives[download.filename]})"
                )
        checks.append({"channel": channel, "version": version, "status": "matched"})
    if not checks:
        raise UpdateError("Emulator frame 没有可用于 Repository XML 交叉校验的 Stable/Beta 条目")
    return checks


def _fetch(url: str, timeout: int = 30) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status = getattr(response, "status", 200)
            if status != 200:
                raise UpdateError(f"官方请求返回 HTTP {status}: {url}")
            content = response.read()
    except (urllib.error.URLError, TimeoutError) as exc:
        raise UpdateError(f"官方请求失败: {url}: {exc}") from exc
    if len(content) < 200:
        raise UpdateError(f"官方响应过短，疑似错误页: {url}")
    try:
        return content.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise UpdateError(f"官方响应不是 UTF-8: {url}") from exc


class FrameLinkParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.urls: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        for key, value in attrs:
            if key.lower() not in {"href", "src"} or not value or ".frame" not in value:
                continue
            self.urls.append(value)


def discover_frame_url(archive_html: str, kind: str) -> str:
    parser = FrameLinkParser()
    parser.feed(archive_html)
    parser.close()
    candidates: list[str] = []
    for raw_url in parser.urls:
        absolute = urllib.parse.urljoin("https://developer.android.com/", raw_url)
        if f"/frame/studio/{kind}_" in absolute and absolute.endswith(".frame"):
            candidates.append(absolute)
    if not candidates:
        raise UpdateError(f"没有从 {kind} 归档入口发现官方 frame")
    parsed = urllib.parse.urlsplit(candidates[-1])
    if parsed.hostname != "developer.android.com":
        raise UpdateError(f"frame 域名不在白名单: {candidates[-1]}")
    return candidates[-1]


def load_sources(offline_fixtures: bool, script_path: Path) -> tuple[str, str, str, dict[str, str]]:
    if offline_fixtures:
        fixture_dir = script_path.parent.parent / "tests" / "fixtures"
        paths = {
            "studio_frame": fixture_dir / "studio-frame.html",
            "emulator_frame": fixture_dir / "emulator-frame.html",
            "repository": fixture_dir / "repository2.xml",
        }
        try:
            contents = {name: path.read_text(encoding="utf-8") for name, path in paths.items()}
        except OSError as exc:
            raise UpdateError(f"无法读取 fixture: {exc}") from exc
        return (
            contents["studio_frame"],
            contents["emulator_frame"],
            contents["repository"],
            {"studio": "fixture", "emulator": "fixture", "repository": "fixture"},
        )
    studio_entry = _fetch(STUDIO_ARCHIVE_URL)
    emulator_entry = _fetch(EMULATOR_ARCHIVE_URL)
    studio_frame_url = discover_frame_url(studio_entry, "archive")
    emulator_frame_url = discover_frame_url(emulator_entry, "emulator_archive")
    return (
        _fetch(studio_frame_url),
        _fetch(emulator_frame_url),
        _fetch(REPOSITORY_URL),
        {"studio": studio_frame_url, "emulator": emulator_frame_url, "repository": REPOSITORY_URL},
    )


def _summary(releases: Sequence[Release], duplicates: int, previous_count: int | None) -> dict[str, object]:
    return {
        "count": len(releases),
        "duplicates_filtered": duplicates,
        "previous_count": previous_count,
        "latest": releases[0].name if releases else None,
        "latest_date": releases[0].date_display if releases else None,
    }


def run_update(
    site_dir: Path,
    mode: str,
    offline_fixtures: bool,
    script_path: Path,
) -> dict[str, object]:
    studio_frame, emulator_frame, repository_xml, source_urls = load_sources(offline_fixtures, script_path)
    studio, studio_duplicates = parse_releases(studio_frame, "Android Studio")
    emulator, emulator_duplicates = parse_releases(emulator_frame, "Android Emulator")
    repository_checks = validate_emulator_repository(emulator, repository_xml)
    paths = {name: site_dir / name for name in TARGET_FILES}
    try:
        original_pages = {name: path.read_text(encoding="utf-8") for name, path in paths.items()}
    except OSError as exc:
        raise UpdateError(f"无法读取 site 页面: {exc}") from exc

    if mode == "bootstrap":
        changed = bootstrap_site(site_dir, studio, emulator)
        return {
            "changed": bool(changed),
            "changed_files": changed,
            "studio": _summary(studio, studio_duplicates, None),
            "emulator": _summary(emulator, emulator_duplicates, None),
            "repository_cross_validation": repository_checks,
            "source_urls": source_urls,
            "mode": mode,
        }

    old_studio_text = _marked_body(original_pages["android-studio.html"], "studio")
    old_emulator_text = _marked_body(original_pages["android-emulator.html"], "emulator")
    old_studio, _ = parse_releases(old_studio_text, "现有 Android Studio", accept_all_devsite_expandables=True)
    old_emulator, _ = parse_releases(old_emulator_text, "现有 Android Emulator", accept_all_devsite_expandables=True)
    _validate_transition(old_studio, studio, "Android Studio")
    _validate_transition(old_emulator, emulator, "Android Emulator")

    updated_pages = dict(original_pages)
    updated_pages["android-studio.html"] = _replace_marker(
        updated_pages["android-studio.html"], "studio", render_releases("studio", studio)
    )
    updated_pages["android-emulator.html"] = _replace_marker(
        updated_pages["android-emulator.html"], "emulator", render_releases("emulator", emulator)
    )
    updated_pages["index.html"] = _replace_marker(
        updated_pages["index.html"], "studio-summary", render_releases("studio", studio[:2])
    )
    updated_pages["index.html"] = _replace_marker(
        updated_pages["index.html"], "emulator-summary", render_releases("emulator", emulator[:2])
    )
    changed_files = [name for name in TARGET_FILES if updated_pages[name] != original_pages[name]]
    if mode == "write":
        for name in changed_files:
            paths[name].write_text(updated_pages[name], encoding="utf-8")
    return {
        "changed": bool(changed_files),
        "changed_files": changed_files,
        "studio": _summary(studio, studio_duplicates, len(old_studio)),
        "emulator": _summary(emulator, emulator_duplicates, len(old_emulator)),
        "repository_cross_validation": repository_checks,
        "source_urls": source_urls,
        "mode": mode,
    }


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-dir", type=Path, default=Path("site"))
    parser.add_argument("--mode", choices=("check", "write", "bootstrap"), default="check")
    parser.add_argument("--offline-fixtures", action="store_true")
    parser.add_argument("--report-json", type=Path)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _build_parser().parse_args(argv)
    try:
        report = run_update(
            site_dir=args.site_dir,
            mode=args.mode,
            offline_fixtures=args.offline_fixtures,
            script_path=Path(__file__).resolve(),
        )
        if args.report_json:
            args.report_json.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(report, ensure_ascii=False, indent=2))
        if args.mode == "check" and report["changed"]:
            return 2
        return 0
    except UpdateError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
