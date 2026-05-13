#!/usr/bin/env python3
"""
Post-process the vis.js proximity map (stage4_proximity.html) so it fits
the hero iframe cleanly.

What it changes (idempotent — re-run anytime the source is regenerated):

  - #mynetwork: drops the 1px lightgray border (clashes with the page
    background) and changes the fixed 780px height to fill the iframe.
  - Injects a small <script> that refits the network after stabilisation
    and whenever the window resizes, so nodes don't drift outside the
    visible canvas.

Run:
    python3 tools/postprocess_proximity_map.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MAP_PATH = ROOT / "assets" / "figures" / "stage4_proximity.html"

STYLE_MARKER = "<!-- ai-finance-plus-map-style -->"
STYLE_BLOCK = f"""{STYLE_MARKER}
<style>
  html, body {{ margin: 0; padding: 0; height: 100%; background: transparent; }}
  /* Hide the pyvis loading bar entirely — we never want to show it. */
  #loadingBar, #bar, #border, #text {{ display: none !important; }}
  /* Strip the lightgray border on the network canvas — clashes with
     the warm-gray page background. */
  #mynetwork {{
    border: 0 !important;
    background: transparent !important;
  }}
  /* Bootstrap card wrapper from pyvis: drop the white box + shadow + border. */
  .card, .card-body {{
    border: 0 !important;
    background: transparent !important;
    box-shadow: none !important;
    padding: 0 !important;
  }}
  /* Center wrapper if present */
  body > center, center {{ display: block; }}
</style>"""

FIT_MARKER = "<!-- ai-finance-plus-map-fit -->"
FIT_SCRIPT = f"""{FIT_MARKER}
<script>
(function() {{
  function safeFit() {{
    if (typeof network === 'undefined' || !network || !network.fit) return;
    try {{ network.fit({{ animation: false }}); }} catch (e) {{}}
  }}

  function attach() {{
    if (typeof network === 'undefined' || !network) {{
      setTimeout(attach, 100);
      return;
    }}
    network.once('stabilizationIterationsDone', function() {{ safeFit(); }});
    if (typeof network.redraw === 'function') {{
      // First-paint fallback (in case stabilization fired before this attached).
      setTimeout(safeFit, 400);
      setTimeout(safeFit, 1200);
    }}
    window.addEventListener('resize', safeFit);
  }}

  if (document.readyState === 'complete') attach();
  else window.addEventListener('load', attach);
}})();
</script>"""


def process(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    original = text

    # Replace prior marker blocks if present, so script-template updates
    # actually take effect on re-run.
    text = re.sub(
        re.escape(STYLE_MARKER) + r"\s*<style>.*?</style>",
        "",
        text,
        count=1,
        flags=re.DOTALL,
    )
    text = re.sub(
        re.escape(FIT_MARKER) + r"\s*<script>.*?</script>",
        "",
        text,
        count=1,
        flags=re.DOTALL,
    )

    # Disable scroll-wheel zoom so the map doesn't hijack the page scroll.
    # Panning (drag) and node-drag stay enabled.
    text = text.replace('"zoomView": true', '"zoomView": false')
    text = text.replace('"zoomView":true', '"zoomView":false')

    # Inject style override at end of <head>.
    if "</head>" in text:
        text = text.replace("</head>", STYLE_BLOCK + "\n</head>", 1)
    # Inject fit hook at end of <body>.
    if "</body>" in text:
        text = text.replace("</body>", FIT_SCRIPT + "\n</body>", 1)

    if text != original:
        path.write_text(text, encoding="utf-8")
        return True
    return False


def main() -> int:
    if not MAP_PATH.is_file():
        print(f"Not found: {MAP_PATH}", file=sys.stderr)
        return 1
    changed = process(MAP_PATH)
    print(f"{'updated' if changed else 'unchanged'}: {MAP_PATH.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
