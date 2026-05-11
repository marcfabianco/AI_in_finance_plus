# Demo page — design rules
*Project: BIS / FSI Policy Benchmarking application demo*

## Tone

Institutional. Conservative. Supervisor-readable. Quiet surfaces; color earns attention only where it carries information.

## Page flow & scroll

**Pattern: cinematic openers + natural-flow content** (NYT visual stories / Stripe docs / Pudding register).

- **Hero**: 100vh. Title, eyebrow, scroll hint. Scroll-fade reveal on entry.
- **Section openers** (each H2): 100vh "title card" — eyebrow + heading + 1–2 line lede only. Gives the panel rhythm. Fades in on entry.
- **Section body**: natural height, flows after the opener. Two-column grid (figure 7 / text 5, or 6 / 6) on wide; stacks on narrow.
- **Figure-led sub-sections**: near-full-viewport. Figure dominant, short paragraph + caption beside.
- **No scroll-snap.** Snap fights long-form reading and accessibility. Rhythm comes from the 100vh openers, not enforced snapping.
- **Mobile**: all grids collapse to single column; 100vh openers stay 100vh.

## Surfaces

| Role             | Hex       | Notes |
|------------------|-----------|-------|
| Page background  | `#EEEDE8` | warm light gray, base |
| Tint 1 (section) | `#E8E6E0` | one step darker, for alternating bands |
| Tint 2 (subtle)  | `#F4F2EC` | one step lighter, for hero fade target |
| Elevated surface | `#FFFFFF` | cards, tables, charts |

- Background carries **1–2% noise grain** (paper feel, not screen).
- **One hero section** may use a vertical fade `#EEEDE8` → `#F4F2EC`. Used once, never as a system.

## Text

| Role             | Hex       |
|------------------|-----------|
| Primary          | `#2A2A2A` |
| Secondary        | `#605C58` |
| Muted / dividers | `#A8A6A0` |

## Accents (one role each — never overlap)

| Role                         | Hex       |
|------------------------------|-----------|
| Titles, headings             | `#A8453C` (terracotta, dropped one step from `#BF4D43`) |
| Links, eyebrows, labels, nav | `#1F3A5F` (ink blue) |
| Spark only (rare callout)    | `#F5D0CC` (soft pink) |

## Rules

- **Terracotta**: titles only (H1–H3, paper titles, drop cap, H2 underline). Never a link, never a label.
- **Ink blue**: interactive + metadata only (links, eyebrows, small-caps labels, nav).
- **Soft pink**: retired as structural. Allowed at most once per page as a small spark (e.g., 40% tint highlight band on a chart). Never as text, divider, or side band.
- **Body**: always charcoal. Never terracotta, never blue.
- **Dividers**: cool gray at 20–25% opacity. No solid black rules.
- **White**: reserved for cards, tables, charts.

## Data viz

| Series role          | Hex       |
|----------------------|-----------|
| Primary (focal)      | `#1F3A5F` |
| Secondary            | `#A8453C` |
| Tertiary             | `#605C58` |
| Quaternary           | `#A8A6A0` |
| Reference / baseline | `#A8A6A0` dashed |
| Highlight band (rare)| `#F5D0CC` @ 40% |

- Chart background: `#FFFFFF` or transparent. Never page gray.
- Axis text: `#2A2A2A`, sans-serif, ≤ 12px.
- Gridlines: `#A8A6A0` @ 20%.
- Chart title: terracotta, serif, weight 600.
- Caption: warm gray, italic, 13px.

## Typography

- Display / titles: **Cormorant Garamond**, 500–700.
- Body / UI: **Inter**, 400–600.

## Scroll-in motion

- Fade + 8–12px rise. 600–800ms ease-out. ~80ms stagger.
- Never animate figures themselves — data appears instant; framing fades in around it.
- No parallax, scale-in, rotation, or scrubbed video.

## Out of palette

Allowed only when content requires it (e.g., a third data series on a chart). Otherwise stay in palette.

## Architecture & structure

**Static site, dependency-free.** HTML + CSS + vanilla JS. No framework, no bundler, no build step. GitHub Pages-ready from root.

**Environment.** No new venv. Local preview: `python3 -m http.server`. Python tooling for figure generation reuses sibling repo `AI_in_finance/.venv`.

**Folder layout.**

```
/                  index.html, README, .gitignore
styles/            tokens.css, base.css, layout.css, components.css
scripts/           reveal.js (and future small JS)
assets/            figures/, fonts/, icons/
notes/             design_rules.md, structure.md (internal, not served)
tools/             python helpers (reuses sibling .venv)
```

**CSS conventions.**
- All design tokens (color, type, spacing, motion) live in `styles/tokens.css` as CSS custom properties. Nothing else hardcodes hex or px.
- One file per concern: `base` (reset + typography), `layout` (grid + sections), `components` (reusable blocks).
- Classes named by role, not by appearance: `.section-opener`, `.eyebrow`, `.figure-caption` — never `.terracotta-bold-24`.

**JS conventions.**
- Vanilla, no dependencies. ES modules. One file per concern.
- Progressive enhancement: page must read fine with JS off.

**Assets.**
- Figures committed as PNG (small) and `.html` (interactive Plotly, if any). Source `.py` scripts that generate them live in `tools/` and reference the sibling repo's data.
- Fonts self-hosted in `assets/fonts/` (Cormorant Garamond, Inter) — no external CDN at runtime.

**Accessibility (non-negotiable).**
- Semantic HTML5 (`<header>`, `<main>`, `<section>`, `<article>`, `<nav>`, `<figure>`).
- Color contrast ≥ WCAG AA on all text/background pairs.
- All scroll-fade animations respect `prefers-reduced-motion`.
- Every figure has alt text or a text equivalent.
- Keyboard navigable; visible focus rings (ink-blue).
