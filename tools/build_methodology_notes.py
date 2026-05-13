#!/usr/bin/env python3
"""
Build methodology sub-pages from markdown sources.

Reads `notes/methodology_source/*.md` and renders each as a standalone
HTML page under `methodology/<group>/` that shares the site's
stylesheets.

The mapping from source file to output URL is configured in NOTES.
Each output page carries:

  - <head> identical to references.html (fonts + four stylesheets),
    plus a MathJax 3 include so $...$ and $$...$$ render as math.
  - .page-header strip with site link and "Back" arrow.
  - .subpage main column wrapping a .note-body that holds the
    rendered markdown.
  - A small in-page subnav so notes in the same group link to each
    other.

Math handling. The python-markdown library would munge LaTeX (e.g.
`v_u` becomes `v<em>u</em>`). We protect math regions by replacing
$$...$$ and $...$ with placeholders before markdown runs, then
restoring them in the rendered HTML. MathJax then picks them up
client-side.

Cross-references. Specific `Fx_*.md` mentions in prose are rewritten
to inline arrow-links + a standalone button paragraph (CROSS_REFS).

Re-run anytime markdown changes:

    /Users/marcosfabian/Documents/Documents/GitHub/AI_in_finance/.venv/bin/python3 \
        tools/build_methodology_notes.py
"""

from __future__ import annotations

import re
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
OUT_DIR = ROOT / "methodology"

# Ordered. Order within a group drives subnav order; groups stay separate.
NOTES = [
    # ---- F0: Section 01 (Scope and data collection) ----
    {
        "group": "F0",
        "source": "F0_methodology_selection.md",
        "out": "F0/methodology.html",
        "label": "Methodology",
        "title": "Methodology of selection",
        "eyebrow": "Section 01 · Methodology",
    },
    {
        "group": "F0",
        "source": "F0_database_architecture.md",
        "out": "F0/database_architecture.html",
        "label": "Database architecture",
        "title": "Database architecture",
        "eyebrow": "Section 01 · Database architecture",
    },
    {
        "group": "F0",
        "source": "F0_codebook.md",
        "out": "F0/codebook.html",
        "label": "Codebook",
        "title": "Codebook",
        "eyebrow": "Section 01 · Codebook",
    },
    # ---- F1: Section 02 (Trends in policy attention) ----
    {
        "group": "F1",
        "source": "F1_technical_note.md",
        "out": "F1/methodology.html",
        "label": "Methodology",
        "title": "Trends in policy attention — methodological note",
        "eyebrow": "Section 02 · Methodology",
    },
    {
        "group": "F1",
        "source": "F1_anchor_selection.md",
        "out": "F1/anchor_selection.html",
        "label": "Anchor selection",
        "title": "Anchor selection",
        "eyebrow": "Section 02 · Anchor selection",
    },
    # ---- F2: Section 03 (Attention landscape) ----
    {
        "group": "F2",
        "source": "F2_technical_note.md",
        "out": "F2/methodology.html",
        "label": "Methodology",
        "title": "Attention landscape — methodological note",
        "eyebrow": "Section 03 · Methodology",
    },
]

# Specific cross-references rewritten in the source markdown before
# rendering. Key is the literal Markdown phrase to find, value is the
# replacement Markdown (will be processed normally afterward).
CROSS_REFS = {
    "documented in `F1_anchor_selection.md`":
        "documented in the anchor selection note.\n\n"
        "[Anchor selection &rarr;](anchor_selection.html){: .arrow-link}",
}


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
  <link rel="stylesheet" href="../../styles/components.css" />

  <!-- MathJax 3 — render $...$ and $$...$$ as math. -->
  <script>
    window.MathJax = {{
      tex: {{
        inlineMath: [["$", "$"]],
        displayMath: [["$$", "$$"]],
        processEscapes: true
      }},
      svg: {{ fontCache: "global" }}
    }};
  </script>
  <script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js"></script>"""


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

{subnav}
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


# --------- Math placeholders ---------------------------------------------------

MATH_BLOCK_TOKEN = "@@MATH_BLOCK_{}@@"
MATH_INLINE_TOKEN = "@@MATH_INLINE_{}@@"

# Display math: $$ ... $$, may span multiple lines
DISPLAY_RE = re.compile(r"\$\$(.+?)\$\$", re.DOTALL)
# Inline math: $ ... $ on a single line, not preceded/followed by another $
INLINE_RE = re.compile(r"(?<!\$)\$([^\$\n]+?)\$(?!\$)")


def protect_math(text: str):
    """Replace math regions with placeholders. Return (text, blocks, inlines)."""
    blocks: list[str] = []
    inlines: list[str] = []

    def _block_sub(m: re.Match) -> str:
        blocks.append(m.group(0))
        return MATH_BLOCK_TOKEN.format(len(blocks) - 1)

    def _inline_sub(m: re.Match) -> str:
        inlines.append(m.group(0))
        return MATH_INLINE_TOKEN.format(len(inlines) - 1)

    text = DISPLAY_RE.sub(_block_sub, text)
    text = INLINE_RE.sub(_inline_sub, text)
    return text, blocks, inlines


def restore_math(html: str, blocks: list[str], inlines: list[str]) -> str:
    for i, raw in enumerate(blocks):
        html = html.replace(MATH_BLOCK_TOKEN.format(i), raw)
    for i, raw in enumerate(inlines):
        html = html.replace(MATH_INLINE_TOKEN.format(i), raw)
    return html


# --------- Source transforms ---------------------------------------------------

def apply_cross_refs(text: str) -> str:
    for src, dst in CROSS_REFS.items():
        text = text.replace(src, dst)
    return text


def render_markdown(text: str) -> str:
    """Convert markdown -> HTML.

    Drops the source's leading top-level H1 because the page renders its
    own title via .subpage__title. Protects math regions through the
    markdown pass so LaTeX isn't munged by Markdown's italic/etc rules.
    """
    # Drop the leading H1 line.
    lines = text.splitlines()
    cleaned = []
    h1_dropped = False
    for line in lines:
        if (
            not h1_dropped
            and line.lstrip().startswith("# ")
            and not line.lstrip().startswith("## ")
        ):
            h1_dropped = True
            continue
        cleaned.append(line)
    text = "\n".join(cleaned).lstrip("\n")

    text = apply_cross_refs(text)
    text, blocks, inlines = protect_math(text)

    html = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "sane_lists", "attr_list"],
        output_format="html5",
    )

    return restore_math(html, blocks, inlines)


# --------- Subnav --------------------------------------------------------------

def subnav_for(group: str, active_out: str) -> str:
    siblings = [n for n in NOTES if n["group"] == group]
    if len(siblings) < 2:
        return ""
    items = []
    for n in siblings:
        is_active = n["out"] == active_out
        cls = "subnav__item subnav__item--active" if is_active else "subnav__item"
        # Each note's `out` is relative to OUT_DIR; siblings share a parent
        # folder, so the href is just the basename.
        href = Path(n["out"]).name
        items.append(f'      <a class="{cls}" href="{href}">{n["label"]}</a>')
    return (
        "    <nav class=\"subnav\" aria-label=\"Methodology notes\">\n"
        + "\n".join(items)
        + "\n    </nav>\n"
    )


# --------- Build ---------------------------------------------------------------

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
        body = render_markdown(src.read_text(encoding="utf-8"))
        out_path = OUT_DIR / note["out"]
        out_path.parent.mkdir(parents=True, exist_ok=True)
        page = PAGE_TMPL.format(
            head=HEAD_BLOCK.format(
                title=note["title"],
                description=description_for(note),
            ),
            eyebrow=note["eyebrow"],
            title=note["title"],
            subnav=subnav_for(note["group"], note["out"]),
            body=body,
        )
        out_path.write_text(page, encoding="utf-8")
        print(f"built: {out_path.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
