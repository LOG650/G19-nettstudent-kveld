---
name: book-latex
description: Manage book projects - create/edit parts, chapters, sections. Use when user wants to add, rename, delete, or reorganize book structure elements. Triggers on "new chapter", "add section", "rename part", "delete appendix", "move chapter".
allowed-tools: Read, Glob, Grep, Edit, Write, Bash, AskUserQuestion
---
# Book Latex Skill

## Purpose

Write structured book projects with parts, chapters, sections, and appendices with the Latex typewriting langauge.

## Parameters

{prompt} = $ARGUMENT

## Workflow

For the given {prompt} to change the content of the report:

1. Read necessary background files (if not already read)
   1. @docs/book-structure-guide.md to learn about the general structure
   2. @docs/subfile.md to learn about the subfile latex package and how its used in this report
2. Locate which tex files to change using the `secXX` slug (e.g., sec01, sec02, sec03).
3. Make the changes following our preferred rules in @.claude\skills\book-latex\docs\latex\rules.md. Anything NOT covered by these rules: Always follow latex best practices.
4. When DONE with all the changes, run `book compile secXX` to compile the specific section and check for errors. If there are errors, fix them and compile again until successful.
5. Run the `book outline` command
6. Make a short summary of what was done

## Book metadata

| Key                 | Value                                                                   |
| ------------------- | ----------------------------------------------------------------------- |
| {book-title}        | Kvantitative metoder i logistikk - implementert via KI                  |
| Book subtitle       | Kompendium: LOG650 Forskningsprosjekt: Logistikk og kunstig intelligens |
| Book description    |                                                                         |
| Book authors        | Bård-Inge Pettersen, Per Kristian Rekdal                               |
| Book year           | 2026                                                                    |
| Book edition        | 1                                                                       |
| {book-color-scheme} | @.claude\skills\book-latex\docs\themes\default.md                       |
| {book-language}     | Norsk                                                                   |

## CLI Commands

There are TWO types of commands the user can call for these commands:

1. book CLI commands - the book CLI is a python click application that is already installed and ready to use
2. structure commands - strucutral commands where you change the outline of the book and where you execute a workflow instead of running a CLI command

### Compile Commands

All commands must be run from the **project root directory**.

This is a **report project** with a flat structure (no parts or chapters). Sections are compiled using the `secXX` slug pattern.

| Task                 | CLI                    | Description                                      |
| -------------------- | ---------------------- | ------------------------------------------------ |
| Compile full report  | `book compile`         | Compiles the entire report (main.tex)            |
| Compile section 1    | `book compile sec01`   | Compiles section 01 (sec01-innledning.tex)       |
| Compile section 2    | `book compile sec02`   | Compiles section 02 (sec02-kontekst.tex)         |
| Compile section 3    | `book compile sec03`   | Compiles section 03 (sec03-teori.tex)            |
| Outline structure    | `book outline`         | Generates latex/ tree to outline.md              |

### Target Notation

This project uses **slug-based targeting** with section files named `secXX-name.tex`.

| Command                | Meaning              | Example Path                          |
| ---------------------- | -------------------- | ------------------------------------- |
| `book compile`         | Full report          | main.tex                              |
| `book compile sec01`   | Section 1            | 200-bodymatter/sec01-innledning.tex   |
| `book compile sec02`   | Section 2            | 200-bodymatter/sec02-kontekst.tex     |
| `book compile sec03`   | Section 3            | 200-bodymatter/sec03-teori.tex        |
| `book compile sec04`   | Section 4            | 200-bodymatter/sec04-metode.tex       |
| `book compile sec05`   | Section 5            | 200-bodymatter/sec05-empiri.tex       |
| `book compile sec06`   | Section 6            | 200-bodymatter/sec06-analyse.tex      |
| `book compile sec07`   | Section 7            | 200-bodymatter/sec07-avslutning.tex   |

**Examples:**

```bash
book compile           # Compile full report
book compile sec01     # Compile section 1 (Innledning)
book compile sec03     # Compile section 3 (Teori)
book compile sec07     # Compile section 7 (Avslutning)
```

### Image Commands

Generate and edit images using AI (requires GEMINI_API_KEY in .env).

#### Instructions

1. You have to generate the prompt to create a new/update an existing image.
2. Read @.claude\skills\book-latex\docs\images\image-prompts.md to learn about how to make a great "prompt":
3. A new image must be saved in the figures folder belonging to the .tex file that has the image. This is decided thorugh the x.x.x format or from the slug of the tex file.
4. Always append the following rules to the beginning of the input prompt when running the `book image` command (unless otherwise specified in the actual prompt):
   1. Background must ALWAYS be WHITE unless otherwise specified
   2. No title in the image, unless otherwise specified
   3. No frame around the image, unless otherwise specified
   4. ALWAYS write text in the {book-langauge} as defined in the Book Metadata section above.
   5. ONLY use INFOGRAPHICS colors from the selected  {book-color-scheme} defined in the Book Metadata section above.
      1. DO NOT use any other colors than these colors.
      2. USE "fill" colors and "stroke" colors correctly

#### Commands

| Task           | CLI (after install)                            | Standalone (no install)                                           |
| -------------- | ---------------------------------------------- | ----------------------------------------------------------------- |
| Generate image | `book image new --path "path.png" "prompt"`  | generates a new image according to prompt, and saves it to --path |
| Edit image     | `book image edit --path "path.png" "prompt"` | edits an existing image at --path and overwrites it               |

**Examples:**

These examples just shows how to use the

```bash
book image new --path "figures/flowchart.png" "A process diagram showing order fulfillment"
book image new -p "charts/sales.png" -r 4K "Bar chart comparing Q1-Q4 sale"
book image edit --path "figures/logo.png" "Change background to blue"
```

**Resolution options:** 1K (default), 2K, 4K

**Note:** `edit` overwrites the original image file.

## Structure Commands

For structural operations, load the corresponding command file from `commands/`:

| Command         | Description                      | File                          |
| --------------- | -------------------------------- | ----------------------------- |
| New Part        | Append a new part at the end     | @/commands/new-part.md        |
| Insert Part     | Insert part at specific position | @/commands/insert-part.md     |
| Rename Part     | Change part slug/title           | @/commands/rename-part.md     |
| Delete Part     | Remove part and contents         | @/commands/delete-part.md     |
| Swap Parts      | Exchange two parts               | @/commands/swap-part.md       |
| New Chapter     | Append chapter to a part         | @/commands/new-chapter.md     |
| Insert Chapter  | Insert chapter at position       | @/commands/insert-chapter.md  |
| Rename Chapter  | Change chapter slug/title        | @/commands/rename-chapter.md  |
| Delete Chapter  | Remove chapter and contents      | @/commands/delete-chapter.md  |
| Move Chapter    | Move chapter between parts       | @/commands/move-chapter.md    |
| Swap Chapters   | Exchange two chapters            | @/commands/swap-chapters.md   |
| New Section     | Append section to a chapter      | @/commands/new-section.md     |
| Insert Section  | Insert section at position       | @/commands/insert-section.md  |
| Rename Section  | Change section slug/title        | @/commands/rename-section.md  |
| Delete Section  | Remove section                   | @/commands/delete-section.md  |
| Move Section    | Move section between chapters    | @/commands/move-section.md    |
| Swap Sections   | Exchange two sections            | @/commands/swap-sections.md   |
| New Appendix    | Append new appendix              | @/commands/new-appendix.md    |
| Insert Appendix | Insert appendix at position      | @/commands/insert-appendix.md |
| Rename Appendix | Change appendix slug/title       | @/commands/rename-appendix.md |
| Delete Appendix | Remove appendix                  | @/commands/delete-appendix.md |

Each command file contains the complete workflow including LaTeX-specific implementation details.

## Research Command

Systematic literature search using parallel subagents for academic research.

### Workflow

1. **Define context**
   - Read the project's research questions and theoretical framework
   - Identify theoretical perspectives to cover
   - Clarify with user: sources per search, time period, focus areas

2. **Create search plan**
   - Organize search strings into thematic groups (A, B, C, D, E...)
   - 2-5 search strings per group
   - Use academic search phrases with quotes for exact phrases
   - Example: `"organizational change" university policy`

3. **Run parallel subagents**
   - Launch 3-5 subagents simultaneously (one per search string)
   - Each subagent uses WebSearch to find sources
   - Subagents work independently and return structured results

4. **Save results**
   - Each subagent creates one markdown file
   - Filename: `lit-[group][number]-[short-description].md`
   - Save path: `docs/refs/`

### Subagent Output Format

Each subagent produces a file with the following structure:

```markdown
# Literature Search: [Search String]

## Search Parameters
- **Search string:** [exact search string]
- **Date:** [date]

---

## Sources Found (3-5 most relevant)

### Source 1: [Author et al. (Year)]

**APA Reference:**
> [Full APA 7 reference]

**Main Argument:**
[2-3 sentences about the article's main findings/argument]

**Relevance to Project:**
[1-2 sentences about how this relates to the project's topic]

**Key Concepts:**
- [concept 1]
- [concept 2]
- [concept 3]

---

## Summary

This search contributed [X] relevant sources to the literature review.

### Key Sources and Their Contribution

| Reference | Why This Source Matters |
|-----------|------------------------|
| Author1 et al. (Year) | [1 sentence explaining specific contribution to your argument] |
| Author2 et al. (Year) | [1 sentence explaining specific contribution to your argument] |
| Author3 et al. (Year) | [1 sentence explaining specific contribution to your argument] |

### APA References (Copy-Ready)

Author1, A. B., & Author2, C. D. (Year). Title of article. Journal Name, Volume(Issue), Pages. https://doi.org/xxx

Author3, E. F. (Year). Title of book chapter. In G. H. Editor (Ed.), Book title (pp. xx-xx). Publisher.

## Knowledge Gaps Identified
[Any gaps in the literature that were observed]
```

### Filename Convention

| Group | Example Filename |
|-------|------------------|
| A: Main theory | `lit-A1-main-theory.md` |
| B: Perspective 1 | `lit-B2-perspective-one.md` |
| C: Perspective 2 | `lit-C1-perspective-two.md` |
| E: Context | `lit-E1-regional-context.md` |

### Example Usage

**User:** "Do a literature search on organizational change in higher education"

**Claude:**
1. Reads project context (research questions, theoretical framework)
2. Proposes search plan with groups and search strings
3. Gets user approval
4. Launches 10-15 parallel subagents
5. Collects results in `docs/refs/`
6. Summarizes findings and identifies knowledge gaps

### Parameters

| Parameter | Description | Default |
|-----------|-------------|---------|
| Sources per search | Number of sources each subagent finds | 3-5 |
| Time period | Publication years for sources | 2015-present |
| Source types | Type of publications | Peer-reviewed articles |
| Language | Search language | English |

### Tips

- Use quotes for exact phrases: `"institutional isomorphism"`
- Combine theoretical terms with context: `"policy implementation" university`
- Include key researcher names: `DiMaggio Powell organizational field`
- Search both general and specific terms
- Prioritize sources from: higher education sector, similar institutions, parallel situations, comparable reforms

## Missing Arguments Rule

**Always use `AskUserQuestion`** when required information is missing:

- **Part/Chapter/Section/Appendix operations**: Ask for slug and title if not provided
- **Insert operations**: Ask for position if not specified
- **Move operations**: Ask for target location if not provided

## Color Scheme

### Default Color Scheme

| Category                              | Color name    | Hex         | Short description                                                 |
| ------------------------------------- | ------------- | ----------- | ----------------------------------------------------------------- |
| **Neutrals**                    | `ink`       | `#1F2933` | Main text color (print-safe near-black).                          |
| **Neutrals**                    | `inkmuted`  | `#556270` | Secondary text (captions, footnotes, minor labels).               |
| **Neutrals**                    | `rule`      | `#CBD5E1` | Light structural lines (table rules, dividers, frames).           |
| **Neutrals**                    | `panel`     | `#F4F7FB` | Soft background tint for boxes and subtle shading.                |
| **Neutrals**                    | `paper`     | `#FFFFFF` | Page/background base (maps to paper stock in print).              |
| **Brand / UI**                  | `primary`   | `#1F6587` | Primary identity color for chapter/heading accents and key rules. |
| **Brand / UI**                  | `secondary` | `#307453` | Supporting accent for subheads, links, minor navigation cues.     |
| **Brand / UI**                  | `accent`    | `#5A2C77` | Attention color for “key idea” highlights and special callouts. |
| **Infographics (fills)**        | `s1`        | `#8CC8E5` | Pastel blue fill for series/category 1 in infographics.           |
| **Infographics (fills)**        | `s2`        | `#97D4B7` | Pastel mint fill for series/category 2 in infographics.           |
| **Infographics (fills)**        | `s3`        | `#F6BA7C` | Pastel orange fill for series/category 3 in infographics.         |
| **Infographics (fills)**        | `s4`        | `#BD94D7` | Pastel purple fill for series/category 4 in infographics.         |
| **Infographics (fills)**        | `s5`        | `#ED9F9E` | Pastel coral fill for series/category 5 in infographics.          |
| **Infographics (strokes/text)** | `s1dark`    | `#1F6587` | Stroke/label color for s1 (outlines, legend text, small labels).  |
| **Infographics (strokes/text)** | `s2dark`    | `#307453` | Stroke/label color for s2 (outlines, legend text, small labels).  |
| **Infographics (strokes/text)** | `s3dark`    | `#9C540B` | Stroke/label color for s3 (keeps orange readable in print).       |
| **Infographics (strokes/text)** | `s4dark`    | `#5A2C77` | Stroke/label color for s4 (outlines, legend text, small labels).  |
| **Infographics (strokes/text)** | `s5dark`    | `#961D1C` | Stroke/label color for s5 (outlines, legend text, small labels).  |

IMPORTANT: WHEN you consider which color to use when writing latex, read this document: @.claude/skill/docs/latex/themes/color-scheme.md
