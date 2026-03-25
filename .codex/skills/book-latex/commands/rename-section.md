# Rename Section

Changes the slug and title of an existing section.

## Required Information

| Field | Description | Ask if missing |
|-------|-------------|----------------|
| `index` | Section index (e.g., `2.1.2`) | Yes |
| `new_slug` | New URL-friendly name | Yes |
| `new_title` | New display title | Yes |

## Workflow

1. **Locate section** - Find section by index
2. **Rename file** - If slug changes
3. **Update section content** - Label and title
4. **Update aggregator** - Update path in chapter file
5. **Update cross-references** - Search project for old label references
6. **Compile the whole book**: `book compile` if any compilation error:
   1. Understand and locate the error
   2. Make changes to fix the error
   3. Recompile the book
   4. Repeat until the error is fixed
7. **Check cross-references** - Search the compilation log to see if there are any broken cross-references due to this change

## LaTeX Implementation

### 1. Rename File (if slug changes)
```
sec<NN>-<old-slug>.tex -> sec<NN>-<new-slug>.tex
```

### 2. Update Section File Content

Label:
```latex
\label{sec:<chapter>:<old-slug>}
```
to:
```latex
\label{sec:<chapter>:<new-slug>}
```

Title (if changed):
```latex
\section{<Old Title>}
```
to:
```latex
\section{<New Title>}
```

### 3. Update Chapter Aggregator

In `ch<XX>-<chapter-slug>.tex`:
```latex
\subfile{sec<NN>-<old-slug>.tex}
```
to:
```latex
\subfile{sec<NN>-<new-slug>.tex}
```

## Cross-Reference Updates

Search entire project and update:
- `\ref{sec:<chapter>:<old-slug>}` -> `\ref{sec:<chapter>:<new-slug>}`
- `\hyperref[sec:<chapter>:<old-slug>]` -> `\hyperref[sec:<chapter>:<new-slug>]`
