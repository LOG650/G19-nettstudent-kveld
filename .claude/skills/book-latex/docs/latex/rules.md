# Latex rules

## Images

Always use `figures/name-of-image.png` when refering to an image

## Preamble

1. ALWAYS use the latex/localsetting.tex file to:

   1. Add new latex packages
   2. Define new/redefine commands or environments

## Figures

1. ALWAYS use `figures/name-of-image.png` when refering to an image
2. ALWAYS use `width=0.8\textwidth` unless otherwise stated
3. ALWAYS us the `book image` command to create
   1. Any figure used in the book
   2. Diagrams
   3. Graphs
   4. Flowcharts
   5. ETc
4. ALWAYS read @docs/images/image-prompts.md before creating the prompt to the `book image` command.
5. ALWAYS add captions to a figure in latex

## Mathematics

1. ALWAYS prefer `\begin{equation}...\end{equation}` for `$$...$$` or `\[...\]`
2. ALWAYS prefer `$...$` for `\(...\)`

## Tables

1. Follow the instructions in @.claude/skill/docs/latex/tables.md to write tables in latex

## Never  split single lines from a paragraph

DONT write

```markdown
Figuren visualiserer rådataene  som en tidsserie, med en tilpasset lineær trendlinje.

Fra plottet kan vi identifisere følgende karakteristikker:
```

DO write:

```

Figuren visualiserer rådataene  som en tidsserie, med en tilpasset lineær trendlinje. Fra plottet kan vi identifisere følgende karakteristikker:
```
