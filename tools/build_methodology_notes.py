#!/usr/bin/env python3
"""
Build methodology sub-pages from markdown sources.

Reads `notes/methodology_source/*.md` and renders each as a standalone
HTML page under `methodology/` that shares the site's stylesheets.

The mapping from source file to output URL is configured in NOTES below.
Each output page carries:

  - <head> identical to references.html (fonts + four stylesheets)
  - .page-header strip with site link and "Back" arrow
  - .subpage main column wrapping a .note-body that holds the rendered
    markdown
  - A small in-page subnav so the three F0 notes link to each other

Re-run anytime the markdown changes:

    /Users/marcosfabian/Documents/Documents/GitHub/AI_in_finance/.venv/bin/python3 \
        tools/build_methodology_notes.py

Idempotent. Re-runs overwrite the generated HTML.
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import markdown
except ImportError:
    sys.stderr.write(
        "markdown package not found. Install in the sibling venv:\n"
        "  /Users/marcosfabian/Documents/Documents/GitHub/AI_in_finance/.venv/bin/pip install markdown\n"
    )
    sys.exit(1)


ROOT = Path(__file__).resolve().parent.parent
SOURCE_DIR = ROOT / "notes" / "methodology_source"
OUT_DIR = ROOT / "methodology" / "F0"

# Ordered. Order drives both subnav order and section-1 button order.
NOTES = [
    {
        "source": "F0_methodology_selection.md",
        "out": "methodology.html",
        "label": "Methodology",
        "title": "Methodology of selection",
        "eyebrow": "Section 01 · Methodology",
    },
    {
        "source": "F0_database_architecture.md",
        "out": "database_architecture.html",
        "label": "Database architecture",
        "title": "Database architecture",
        "eyebrow": "Section 01 · Database architecture",
    },
    {
        "source": "F0_codebook.md",
        "out": "codebook.html",
        "label": "Codebook",
        "title": "Codebook",
        "eyebrow": "Section 01 · Codebook",
    },
]


HEAD_BLOCK = """  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title} — AI in Financial Policy</title>
  <meta name="description" content="{description}" />

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link
    href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=Inter:wght@400;500;600&display=swap"
    rel="stylesheet"
  />

  <link rel="stylesheet" href="../../styles/tokens.css" />
  <link rel="stylesheet" href="../../styles/base.css" />
  <link rel="stylesheet" href="../../styles/layout.css" />
  <link rel="stylesheet" href="../../styles/components.css" />"""


PAGE_TMPL = """<!doctype html>
<html lang="en">
<head>
{head}
</head>

<body>
  <header class="page-header">
    <div class="page-header__inner">
      <p class="page-header__site"><a href="../../index.html">AI in Financial Policy</a></p>
      <a class="arrow-link" href="../../index.html" aria-label="Back to the main page">&larr; Back</a>
    </div>
  </header>

  <main class="subpage subpage--wide">
    <p class="eyebrow">{eyebrow}</p>
    <h1 class="subpage__title">{title}</h1>

    <nav class="subnav" aria-label="Section 01 methodology notes">
{subnav_links}
    </nav>

    <article class="note-body">
{body}
    </article>
  </main>

  <footer class="site-footer">
    <div class="container">
      <p>Demo — methods preview. Results are illustrative; the methodology is the deliverable.</p>
    </div>
  </footer>
</body>
</html>
"""


def render_markdown(text: str) -> str:
    """Convert markdown -> HTML with sensible defaults.

    Drop the leading top-level H1 if it duplicates the page title (we
    already render the title via .subpage__title)."""
    # Strip the first H1 line, since the page renders its own title.
    lines = text.splitlines()
    cleaned = []
    h1_dropped = False
    for line in lines:
        if not h1_dropped and line.lstrip().startswith("# ") and not line.lstrip().startswith("## "):
            h1_dropped = True
            continue
        cleaned.append(line)
    text = "\n".join(cleaned).lstrip("\n")

    return markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists"],
        output_format="html5",
    )


def subnav_html(active_out: str) -> str:
    items = []
    for n in NOTES:
        is_active = n["out"] == active_out
        cls = "subnav__item subnav__item--active" if is_active else "subnav__item"
        href = n["out"]
        items.append(f'      <a class="{cls}" href="{href}">{n["label"]}</a>')
    return "\n".join(items)


def description_for(note: dict) -> str:
    return f"Methodology note: {note['title'].lower()} — AI in Financial Policy demo."


def main() -> int:
    if not SOURCE_DIR.is_dir():
        print(f"missing: {SOURCE_DIR}", file=sys.stderr)
        return 1
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for note in NOTES:
        src = SOURCE_DIR / note["source"]
        if not src.is_file():
            print(f"missing source: {src}", file=sys.stderr)
            continue
        md_text = src.read_text(encoding="utf-8")
        body = render_markdown(md_text)
        page = PAGE_TMPL.format(
            head=HEAD_BLOCK.format(
                title=note["title"],
                description=description_for(note),
            ),
            eyebrow=note["eyebrow"],
            title=note["title"],
            subnav_links=subnav_html(note["out"]),
            body=body,
        )
        out_path = OUT_DIR / note["out"]
        out_path.write_text(page, encoding="utf-8")
        print(f"built: {out_path.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
