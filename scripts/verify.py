#!/usr/bin/env python3
"""Verify distributable resources, links and package parity, not model accuracy."""
import hashlib
import json
import re
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build import NAME, ROOT, VERSION, runtime_files, workbuddy_skill


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def main():
    files = runtime_files()
    skill = files["SKILL.md"].decode("utf-8")
    require(skill.startswith("---\n"), "Skill frontmatter missing")
    header = skill.split("---", 2)[1]
    require(re.search(r"^name: " + NAME + r"$", header, re.M), "Skill name mismatch")
    require(f'version: "{VERSION}"' in header, "Skill version mismatch")
    require(len(list((ROOT / "references").glob("*.md"))) == 6, "Reference count mismatch")
    interface = (ROOT / "agents/openai.yaml").read_text(encoding="utf-8")
    require("$" + NAME in interface, "Default invocation missing")

    checked_links = 0
    for path in [ROOT / "README.md", ROOT / "SKILL.md", ROOT / "CONTRIBUTING.md"] + sorted((ROOT / "docs").glob("*.md")) + sorted((ROOT / "references").glob("*.md")):
        text = path.read_text(encoding="utf-8")
        require("/Users/" not in text and "/Volumes/" not in text, "Private machine path in public file")
        require("[TODO:" not in text, "Unfinished scaffold")
        for href in re.findall(r"\[[^\]\n]+\]\(([^)\n]+)\)", text):
            parts = urlsplit(href)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            target = (path.parent / unquote(parts.path)).resolve()
            require(target.is_file(), f"Broken link: {path.relative_to(ROOT)} -> {href}")
            checked_links += 1

    checksums = (ROOT / "dist/SHA256SUMS").read_text(encoding="utf-8")
    results = []
    for platform in ("codex", "workbuddy"):
        path = ROOT / "dist" / f"{NAME}-{platform}-{VERSION}.zip"
        expected = dict(files)
        prefix = NAME + "/" if platform == "codex" else ""
        if platform == "workbuddy":
            expected.pop("agents/openai.yaml")
            expected["SKILL.md"] = workbuddy_skill(skill).encode("utf-8")
        with zipfile.ZipFile(path) as archive:
            require(archive.testzip() is None, "Invalid ZIP")
            require(set(archive.namelist()) == {prefix + k for k in expected}, "Missing or extra ZIP resources")
            for name, data in expected.items():
                require(archive.read(prefix + name) == data, f"Package drift: {platform}/{name}")
            packaged = archive.read(prefix + "SKILL.md").decode("utf-8")
            require(packaged.split("---", 2)[2] == skill.split("---", 2)[2], "Platform body differs")
            if platform == "workbuddy":
                top = packaged.split("---", 2)[1]
                for field in ("description_zh", "description_en", "version", "author"):
                    require(re.search(r"^" + field + r": \".+\"$", top, re.M), f"WorkBuddy field missing: {field}")
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        require(f"{digest}  {path.name}" in checksums, "Checksum mismatch")
        results.append({"platform": platform, "sha256": digest, "integrity": "passed"})
    print(json.dumps({"status": "passed", "version": VERSION,
                      "local_links": checked_links, "packages": results,
                      "note": "File checks do not establish platform execution or model accuracy."},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
