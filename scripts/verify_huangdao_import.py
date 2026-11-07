#!/usr/bin/env python3
"""Check published imports, body integrity, rendered entries, links and chart data."""
import hashlib
import json
import re
from datetime import datetime
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
manifest = json.loads((ROOT / "docs/huangdao-migration.json").read_text())
errors = []
baseline = [a for a in manifest["selection"] if a["selected"]]
revision_path = ROOT / "docs/huangdao-article-revisions.json"
revisions = json.loads(revision_path.read_text()) if revision_path.is_file() else None
if revisions:
    current = {a["id"]: a for a in revisions["articles"]}
    if len(revisions["articles"]) != len(baseline) or set(current) != {a["id"] for a in baseline}:
        errors.append("Revisions must cover exactly the existing imported articles")
    for original in baseline:
        latest = current.get(original["id"], {})
        for key in ("slug", "post", "url", "publishedAt", "sourceUrl"):
            if latest.get(key) != original[key]:
                errors.append(f"Immutable import field changed: {original['slug']} {key}")
    selected = revisions["articles"]
else:
    selected = baseline


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links, self.images, self.ids = [], [], set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "img":
            self.images.append(attrs.get("src", ""))


def output(url):
    path = ROOT / "_site" / unquote(urlsplit(url).path).lstrip("/")
    for candidate in (path, Path(str(path) + ".html"), path / "index.html"):
        if candidate.is_file():
            return candidate
    return None


archive = (ROOT / "_site/workOutline/index.html").read_text()
tags = (ROOT / "_site/tags/index.html").read_text()
index = "\n".join(p.read_text() for p in [ROOT / "_site/index.html", *sorted((ROOT / "_site").glob("page*/index.html"))])
for a in selected:
    source = (ROOT / a["post"]).read_text()
    front = dict((k, json.loads(v)) for k, v in
                 (line.split(": ", 1) for line in source.split("---", 2)[1].strip().splitlines()))
    for key, value in (("title", a["title"]), ("author", a["author"]), ("date", a["publishedAt"])):
        if front.get(key) != value:
            errors.append(f"Metadata changed: {a['slug']} {key}")
    if revisions:
        expected = {"excerpt": a["summary"], "source_revision": a["revision"],
                    "source_updated_at": a["sourceUpdatedAt"], "last_modified_at": a["sourceUpdatedAt"],
                    "source_body_sha256": a["bodySha256"], "source_verified_at": revisions["checkedAt"],
                    "source_category": a["sourceCategory"], "source_reference": a["sourceReference"],
                    "categories": ["ai"], "rootCate": "work"}
        for key, value in expected.items():
            if front.get(key) != value:
                errors.append(f"Revision metadata changed: {a['slug']} {key}")
        if front.get("addons") == ["related"] and a["author"] == "荒岛书生":
            errors.append(f"Personal author introduction still hidden: {a['slug']}")
        if "<!-- source-note:start -->" not in source or source.index("<!-- source-note:start -->") < source.index("<!-- source-body:end -->"):
            errors.append(f"Missing source note at end of article: {a['slug']}")
        if "迁移核对：" in source:
            errors.append(f"Obsolete migration introduction: {a['slug']}")
        if a.get("editorialNote") and a["editorialNote"] not in source:
            errors.append(f"Missing author-commentary identity: {a['slug']}")
    if datetime.fromisoformat(a["publishedAt"].replace("Z", "+00:00")) > datetime.fromisoformat(manifest["checkedAt"]):
        errors.append(f"Future article imported: {a['slug']}")
    body = source.split("<!-- source-body:start -->\n", 1)[1].split("\n<!-- source-body:end -->", 1)[0]
    if hashlib.sha256(body.encode()).hexdigest() != a["adaptedBodySha256"]:
        errors.append(f"Adapted body changed: {a['slug']}")
    restored = re.sub(r"<!-- migrated-chart:([^:]+):start -->.*?<!-- migrated-chart:\1:end -->",
                      lambda m: "```site-chart\n" + m[1] + "\n```", body, flags=re.S)
    if hashlib.sha256(restored.encode()).hexdigest() != a["bodySha256"]:
        errors.append(f"Original body integrity failed: {a['slug']}")
    for name, text in (("archive", archive), ("tags", tags), ("blog", index)):
        if a["url"] not in Page(text).links:
            errors.append(f"Missing {name} entry: {a['url']}")
    built = output(a["url"])
    if not built:
        errors.append(f"Missing article: {a['url']}")
        continue
    html = built.read_text()
    page = Page(html)
    if "markdown-toc" not in page.ids or a["author"] not in html:
        errors.append(f"Missing TOC/author: {a['slug']}")
    if "language-site-chart" in html or "```" in html or "{%" in html:
        errors.append(f"Unrendered markup: {a['slug']}")
    for url in page.images + page.links:
        parts = urlsplit(url)
        if parts.scheme or parts.netloc:
            continue
        target = output(url) if parts.path else built
        if not target:
            errors.append(f"Missing local link/image: {a['slug']} -> {url}")
        elif parts.fragment and target.suffix == ".html" and unquote(parts.fragment) not in Page(target.read_text()).ids:
            errors.append(f"Missing fragment: {a['slug']} -> {url}")
    for chart in a["chartIds"]:
        if "/assets/img/huangdao/" + chart + ".png" not in page.images:
            errors.append(f"Missing rendered chart: {chart}")

data_path = ROOT / "assets/data/huangdao/aa-november-2026.json"
if hashlib.sha256(data_path.read_bytes()).hexdigest() != manifest["figureDataSha256"]:
    errors.append("Figure data differs from the source snapshot")
data = json.loads(data_path.read_text())
chart_html = output("/ai/artificial-analysis-index-guide").read_text()
for row in data["rows"]:
    for value in (row["name"], str(row["displayScore"]), f'{row["costUsd"]:.2f}'):
        if value not in chart_html:
            errors.append(f"Missing chart table data: {value}")
for private in (".migration-work", "docs/huangdao-migration.json", "docs/huangdao-article-revisions.json", "backend", "content"):
    if (ROOT / "_site" / private).exists():
        errors.append(f"Unexpected build input published: {private}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"PASS: {len(selected)} imports; current source bodies, original dates/URLs, revision metadata, TOCs, blog/archive/tag entries, local links/images and all 8 chart rows preserved.")
