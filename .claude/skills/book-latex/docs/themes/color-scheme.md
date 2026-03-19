# Color System Usage Guide (Print-First Book)

This guide describes **what each named color is for** and how to use it consistently across a print-first book layout (chapters, headings, tables, callouts, and infographics).

The palette is built around:

- **Neutrals** (typography + structure)
- **Brand/UI colors** (navigation + emphasis)
- **Data series colors** (infographics) with **dark companions** for print clarity

## Color Categories Overview

| Category                       | Color Names                                                |
| ------------------------------ | ---------------------------------------------------------- |
| **Neutrals**             | `ink`, `inkmuted`, `rule`, `panel`, `paper`      |
| **Brand/UI**             | `primary`, `secondary`, `accent`                     |
| **Infographics fill**    | `s1`, `s2`, `s3`, `s4`, `s5`                     |
| **Infographics stroke** | `s1dark`, `s2dark`, `s3dark`, `s4dark`, `s5dark` |

---

## Neutrals

### `ink` — Main text / strongest contrast

**Use for**

- Body text
- Figure captions (if not muted)
- Footnotes if you want maximum readability
- Inline math / code (if not using special styling)

**Avoid**

- Large filled areas (can look too heavy); use a panel tint or rich black strategy if needed.

---

### `inkmuted` — Secondary text

**Use for**

- Captions (especially long captions)
- Footnotes / endnotes
- Table notes
- Secondary labels in figures (axis labels, minor annotations)

**Avoid**

- Anything critical that must be readable at small size under weak print conditions.

---

### `rule` — Lines and subtle structure

**Use for**

- Table rules (light separators)
- Figure frames / thin outlines
- Divider lines between sections
- UI separators (TOC, side notes, headers/footers separators)

**Avoid**

- Text (contrast too low)
- Important boundaries that must stand out (use `primary` or `ink`).

---

### `panel` — Soft background blocks

**Use for**

- Callout box backgrounds (examples, definitions, notes)
- Table zebra striping (very subtle)
- Figure background panels
- Highlight regions behind diagrams

**Avoid**

- Very large continuous areas on many pages (can add “gray fog” to the book).

---

### `paper` — Page background

**Use for**

- Default background
- Negative space inside figures and tables

**Note**

- In print, “paper” becomes the actual paper color; keep designs robust to slightly warm/cool paper stocks.

---

## Brand / UI Colors

### `primary` — Navigation + hierarchy anchor

**Use for**

- Chapter numbers
- Part/chapter title accents (rules, small ornaments)
- H1/H2 heading accents (small bars, bullets, left margin markers)
- Key figure titles or figure label accents
- Emphasis lines (important separators, stronger table header rules)

**Avoid**

- Long text blocks in `primary` (fatiguing)
- Tiny text on `primary` backgrounds unless contrast is tested.

---

### `secondary` — Supporting UI accent

**Use for**

- H3/H4 markers (small icons, bullets, subtle rules)
- Links (if printed as color)
- Minor navigation elements (running headers, section markers)
- Subtle callout accents (icon + title line)

**Avoid**

- Competing with `primary` in the same element—choose one lead color per element.

---

### `accent` — Attention / highlight

**Use for**

- “Key idea” badges
- Important callout titles (“Remember”, “Pitfall”, “Exam tip”)
- Special highlights in diagrams (one focal point per figure)
- Occasional emphasis in chapter openers

**Avoid**

- Overuse (if everything is accent, nothing is)
- Using as the default heading color (that’s `primary`’s job)

**Tip**

- Accent works best at **5–10%** of visual weight on a spread.

---

## Data Series Colors (Infographics)

These are your **pastel fills**. They are intended primarily for **areas**, not text.

### `s1` — Series 1 fill (pastel blue)

**Use for**

- Bars/areas/bubbles for category 1
- Background banding in charts
- Card fills in infographics

**Pair with**

- `s1dark` for outlines, icons, legend text, small labels

---

### `s2` — Series 2 fill (pastel mint)

**Use for**

- Category 2 in charts
- Secondary background panels inside figures

**Pair with**

- `s2dark` for outlines and labels

---

### `s3` — Series 3 fill (pastel orange)

**Use for**

- Category 3
- Positive emphasis in charts (but keep it consistent with your semantics)

**Pair with**

- `s3dark` (important for print; orange can wash out without a dark stroke)

---

### `s4` — Series 4 fill (pastel purple)

**Use for**

- Category 4
- “Different group” or “alternative scenario” in charts

**Pair with**

- `s4dark` for outlines and legend text

---

### `s5` — Series 5 fill (pastel coral)

**Use for**

- Category 5
- Often good for “human/behavioral” category in mixed technical visuals

**Pair with**

- `s5dark` for print-safe readability

---

## Data Series Dark Companions (Print-Safe)

These are the **stroke / text versions** of each pastel series. Use them wherever contrast matters.

### `s1dark`, `s2dark`, `s3dark`, `s4dark`, `s5dark`

**Use for**

- Thin outlines around pastel shapes
- Legend markers + legend text
- Small labels inside colored shapes
- Icons placed on pastel backgrounds
- Chart elements (axis emphasis, series lines)

**Avoid**

- Large blocks of dark color (use sparingly, like `primary`)

---

## Layout Rules (Recommended)

### Contrast and legibility (print-first)

- Do **not** set small text in pastel colors.
- Use `ink` or `series_dark` for any text under ~11pt.
- Ensure thin lines are not too light: prefer `rule` for subtle lines and `primary/ink/series_dark` for important boundaries.

### One lead color per element

- Headings: use `primary` as the main signal
- Support signals: `secondary`
- Attention moment: `accent`
- Data meaning: `s1–s5` with `s1dark–s5dark`

### Consistency in charts

- Keep `s1–s5` mapped to the same meaning across the book.
- Use only **one** accent moment per chart (e.g., highlight one point using `accent`).

---

## Quick Reference

- **Text:** `ink`, `inkmuted`
- **Lines/structure:** `rule`
- **Box backgrounds:** `panel`
- **Main design identity:** `primary`
- **Secondary identity:** `secondary`
- **Highlights:** `accent`
- **Infographic fills:** `s1–s5`
- **Infographic outlines/text:** `s1dark–s5dark`

---
