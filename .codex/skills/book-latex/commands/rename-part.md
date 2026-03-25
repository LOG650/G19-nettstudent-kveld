# Rename Part

Changes the slug and title of an existing part.

## Required Information

| Field | Description | Ask if missing |
|-------|-------------|----------------|
| `index` | Part index (e.g., `2`) | Yes |
| `new_slug` | New URL-friendly name | Yes |
| `new_title` | New display title | Yes |

## Workflow

1. **Locate part** - Find part by index
2. **Rename folder** - If slug changes
3. **Update aggregator** - Update paths and title in bodymatter aggregator
4. **Compile the whole book**: `book compile` if any compilation error:
   1. Understand and locate the error
   2. Make changes to fix the error
   3. Recompile the book
   4. Repeat until the error is fixed
5. **Check cross-references** - Search the compilation log to see if there are any broken cross-references due to this change

## LaTeX Implementation

### 1. Rename Folder (if slug changes)
```
latex/200-bodymatter/part<NN>-<old-slug>/
-> latex/200-bodymatter/part<NN>-<new-slug>/
```

### 2. Aggregator file name stays same
`part<NN>.tex` - only the folder name changes

### 3. Update bodymatter.tex

Change path:
```latex
\subfile{part<NN>-<old-slug>/part<NN>.tex}
```
to:
```latex
\subfile{part<NN>-<new-slug>/part<NN>.tex}
```

If title changes:
```latex
\part{<Old Title>}
```
to:
```latex
\part{<New Title>}
```

## Files NOT Needing Updates

- Child chapter files (they reference `../../main.tex`, not the part folder name)
- Section files (they reference `../../../main.tex`)
