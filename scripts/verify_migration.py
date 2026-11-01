#!/usr/bin/env python3
"""One-time acceptance check for the Hydejack migration against the original commit."""
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BEFORE = "7734176f35ee4e5ff3fce957b1a067c1b0ff4c17"
CONTENT = ["_posts", "assets/images", "about_me_en.md", "about_me_zh.md", "contact.md", "donate.md"]

def git(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)

files = git("ls-tree", "-rz", "--name-only", BEFORE, "--", *CONTENT).decode().rstrip("\0").split("\0")
errors = []
for name in files:
    path = ROOT / name
    original = git("show", f"{BEFORE}:{name}")
    current = path.read_bytes() if path.is_file() else None
    # Allow the contact title/layout change and the user-requested WeChat ID update.
    if name == "contact.md" and current is not None:
        original = original.split(b"---", 2)[2].replace(b"ID: ldx765514164   ", b"ID: codedoctor<br>", 1)
        current = current.split(b"---", 2)[2]
    if current != original:
        errors.append(f"Original content differs: {name}")
routes = json.loads((ROOT / "scripts/legacy-post-routes.json").read_text())
for name, entry in routes.items():
    source = ROOT / name
    if hashlib.sha256(source.read_bytes()).hexdigest() != entry["source_sha256"]:
        errors.append(f"Post source changed: {name}")
    url = entry["url"].lstrip("/")
    output = ROOT / "_site" / url
    candidates = [output, Path(str(output) + ".html"), output / "index.html"]
    if not any(p.is_file() for p in candidates):
        errors.append(f"Original URL missing from build: {entry['url']}")
for name in ("add-transition.png", "modify-video-saturation.png"):
    original = ROOT / "assets/images/work/lightworks" / name
    alias = ROOT / "_site/images/work/lightworks" / name
    if not alias.is_file() or alias.read_bytes() != original.read_bytes():
        errors.append(f"Legacy image URL not restored: /images/work/lightworks/{name}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {len(files)} original content sources preserved (contact title/layout/WeChat ID updated); all {len(routes)} published post URLs exist.")
