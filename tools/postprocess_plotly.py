#!/usr/bin/env python3
"""
Post-process Plotly HTML exports so they blend with the demo page.

What it changes (idempotent):
  - paper_bgcolor / plot_bgcolor   -> transparent
  - the chart <div> fixed size     -> 100% / 100%
  - injects a tiny <style> into <head> so html/body have no margin
    and the iframe content has no scrollbars

Run from the repo root or from anywhere — paths are resolved relative
to this file:

    python3 tools/postprocess_plotly.py

Re-run anytime the source figures are regenerated.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIG_DIR = ROOT / "assets" / "figures"

# Background replacements — covers Plotly template defaults and explicit overrides.
BG_REPLACEMENTS = [
    (r'"paper_bgcolor":"white"',   '"paper_bgcolor":"rgba(0,0,0,0)"'),
    (r'"paper_bgcolor":"#FFFFFF"', '"paper_bgcolor":"rgba(0,0,0,0)"'),
    (r'"paper_bgcolor":"#ffffff"', '"paper_bgcolor":"rgba(0,0,0,0)"'),
    (r'"plot_bgcolor":"#E5ECF6"',  '"plot_bgcolor":"rgba(0,0,0,0)"'),
    (r'"plot_bgcolor":"#FFFFFF"',  '"plot_bgcolor":"rgba(0,0,0,0)"'),
    (r'"plot_bgcolor":"#ffffff"',  '"plot_bgcolor":"rgba(0,0,0,0)"'),
    (r'"plot_bgcolor":"white"',    '"plot_bgcolor":"rgba(0,0,0,0)"'),
]

# Strip the layout-level fixed pixel width/height so the chart sizes to its
# container. Matches `,"width":N` / `,"height":N` only when N is the known
# chart-canvas size (3+ digits), to avoid clobbering trace-level widths
# like `"width":0.7` (bar-width fraction).
LAYOUT_DIM_RES = [
    re.compile(r',"width":\d{3,}(?=[,}])'),
    re.compile(r',"height":\d{3,}(?=[,}])'),
]

# Inject autosize:true into the layout if missing. Idempotent — guarded by
# the check below.
AUTOSIZE_ANCHOR_RE = re.compile(r'"paper_bgcolor":"rgba\(0,0,0,0\)"')

# Replace any fixed pixel-size on the Plotly graph div with 100% / 100%.
DIV_SIZE_RE = re.compile(
    r'(<div id="[^"]+" class="plotly-graph-div" style=")'
    r'height:\d+px;\s*width:\d+px;'
    r'(")'
)

# Forces a resize after window load, in case the chart was rendered before
# the iframe knew its final size.
RESIZE_MARKER = "<!-- ai-finance-plus-resize -->"
RESIZE_SCRIPT = f"""{RESIZE_MARKER}
<script>
(function() {{
  function resize() {{
    var divs = document.querySelectorAll('.plotly-graph-div');
    if (window.Plotly && divs.length) {{
      divs.forEach(function(d) {{
        try {{ window.Plotly.Plots.resize(d); }} catch (e) {{}}
      }});
    }}
  }}
  if (document.readyState === 'complete') resize();
  else window.addEventListener('load', resize);
  window.addEventListener('resize', resize);
}})();
</script>"""

# A minimal style block that makes the iframe contents fill the frame and
# kill the default body margin. Marker comment makes the script idempotent.
STYLE_MARKER = "<!-- ai-finance-plus-postprocess -->"
STYLE_BLOCK = f"""{STYLE_MARKER}
<style>
  html, body {{
    margin: 0;
    padding: 0;
    height: 100%;
    background: transparent;
    overflow: hidden;
  }}
  body > div {{ height: 100%; }}
  .plotly-graph-div {{ height: 100% !important; width: 100% !important; }}
</style>"""


def process(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    for pat, repl in BG_REPLACEMENTS:
        text = re.sub(pat, repl, text)

    for rx in LAYOUT_DIM_RES:
        text = rx.sub("", text)

    if '"autosize":true' not in text:
        text = AUTOSIZE_ANCHOR_RE.sub(
            '"autosize":true,"paper_bgcolor":"rgba(0,0,0,0)"',
            text,
            count=1,
        )

    text = DIV_SIZE_RE.sub(r'\1height:100%; width:100%;\2', text)

    if STYLE_MARKER not in text:
        text = text.replace("</head>", STYLE_BLOCK + "\n</head>", 1)

    if RESIZE_MARKER not in text:
        text = text.replace("</body>", RESIZE_SCRIPT + "\n</body>", 1)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> int:
    if not FIG_DIR.is_dir():
        print(f"No figures dir at {FIG_DIR}", file=sys.stderr)
        return 1
    htmls = sorted(FIG_DIR.glob("*.html"))
    if not htmls:
        print("No .html figures to process.")
        return 0
    for p in htmls:
        changed = process(p)
        print(f"{'updated' if changed else 'unchanged'}: {p.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
