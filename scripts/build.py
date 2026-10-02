#!/usr/bin/env python3
"""Build portable, instruction-only skill packages using the standard library."""
import hashlib
import json
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VERSION = "1.0.0"
NAME = "logic-xray"


def runtime_files():
    paths = [ROOT / "SKILL.md", ROOT / "LICENSE", ROOT / "agents/openai.yaml"]
    paths += sorted((ROOT / "references").glob("*.md"))
    return {str(path.relative_to(ROOT)): path.read_bytes() for path in paths}


def write_zip(path, files, prefix=""):
    path.parent.mkdir(exist_ok=True)
    with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(prefix + name, (2026, 10, 2, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)


def workbuddy_skill(text):
    if not text.startswith("---\n"):
        raise ValueError("Missing skill frontmatter")
    _, header, body = text.split("---", 2)
    fields = {
        "display_name": "逻辑透视镜（logic-xray）",
        "display_name_en": "logic-xray",
        "description_zh": "拆解社交平台正文与评论的证据和推理，提出有依据、可回答的反问。",
        "description_en": "Audit arguments in social posts and comments; draft answerable, evidence-linked questions.",
        "version": VERSION,
        "author": "logic-xray contributors",
    }
    extra = "\n".join(key + ": " + json.dumps(value, ensure_ascii=False)
                      for key, value in fields.items())
    return "---\n" + header.strip() + "\n" + extra + "\n---" + body


def main():
    dist = ROOT / "dist"
    files = runtime_files()
    write_zip(dist / f"{NAME}-codex-{VERSION}.zip", files, NAME + "/")
    wb = dict(files)
    wb.pop("agents/openai.yaml")
    wb["SKILL.md"] = workbuddy_skill(files["SKILL.md"].decode("utf-8")).encode("utf-8")
    write_zip(dist / f"{NAME}-workbuddy-{VERSION}.zip", wb)
    sums = []
    for platform in ("codex", "workbuddy"):
        path = dist / f"{NAME}-{platform}-{VERSION}.zip"
        sums.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}")
    (dist / "SHA256SUMS").write_text("\n".join(sums) + "\n", encoding="utf-8")
    print(json.dumps({"version": VERSION, "packages": 2,
                      "references": len(list((ROOT / "references").glob("*.md")))},
                     ensure_ascii=False))


if __name__ == "__main__":
    main()
