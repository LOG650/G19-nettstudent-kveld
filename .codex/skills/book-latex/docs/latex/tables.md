# Typesetting Tables

## Abstract

This tutorial explains the typesetting of tables. Topics covered include row composition, font size, alignment and formatting of individual cells, line breaks, column declarations, design with lines and vertical spacing, formal table structure, alignment of number columns, use of units and currency amounts, subdivision of table headers, rotating table fields, definition of new column types, use of emphasis, old-style numerals and subheadings within a table, design with sans-serif fonts, customization of table captions, stretching to text width, and use of grids.

Using numerous examples, it is shown how to design tables that are readable, unambiguous, and clear. This is accomplished using various additional packages.

---

## General Table rules

Use the following rules on a general basis when creating tablesin latex:

1. Always use tabularx package
2. Use \footnotesize
3. Avoid vertical lines
4. Column headers always in bold, same if there are row headers as welll.
5. Avoid “boxing up” cells, usually 3 horizontal lines are enough: above, below, and after heading (see examples in this guide)
6. Avoid double horizontal lines
7. Enough space between rows
8. As a rule when in doubt: Align left
9. Also the first column gets a header
10. Remove space to the vertical edges: `\begin{tabular}{@{}lll@{}}…`
11. For smaller font size for caption, you can add this after you load the `caption` package:
    1. `\usepackage{caption} `
    2. `\captionsetup{font=small}`
12. IMPORTANT: Use hierarchical tables when there are multiple categories of rows or columns - this makes readability drastically better

## Hierarchical tables

Choose among:

1. One level of hierarchy: x-axis only
2. One level of hierarchy: x-axis and y-axis

```latex
\usepackage{booktabs}
\usepackage{tabularx}

\newcommand{\ra}[1]{\renewcommand{\arraystretch}{#1}}

\begin{table*}
\centering
\ra{1.3}

\begin{tabularx}{\textwidth}{@{}rrrrcrrrcrrr@{}}
\toprule
  & \multicolumn{3}{c}{$w = 8$}  & \phantom{abc}
  & \multicolumn{3}{c}{$w = 16$} & \phantom{abc}
  & \multicolumn{3}{c}{$w = 32$} \\
\cmidrule{2-4}\cmidrule{6-8}\cmidrule{10-12}
  & $t=0$ & $t=1$ & $t=2$ &&
    $t=0$ & $t=1$ & $t=2$ &&
    $t=0$ & $t=1$ & $t=2$ \\
\midrule

$dir=1$\\
$c$ & 0.0790  & 0.1692  & 0.2945  && 0.3670  & 0.7187  & 3.1815  && -1.0032 & -1.7104 & -21.7969 \\
$c$ & -0.8651 & 50.0476 & 5.9384  && -9.0714 & 297.0923& 46.2143 && 4.3590  & 34.5809 & 76.9167 \\
$c$ & 124.2756& -50.9612& -14.2721&& 128.2265& -630.5455& -381.0930&& -121.0518& -137.1210& -220.2500 \\

$dir=0$\\
$c$ & 0.0357  & 1.2473  & 0.2119  && 0.3593  & -0.2755 & 2.1764  && -1.2998 & -3.8202 & -1.2784 \\
$c$ & -17.9048& -37.1111& 8.8591  && -30.7381& -9.5952 & -3.0000 && -11.1631& -5.7108 & -15.6728 \\
$c$ & 105.5518& 232.1160& -94.7351&& 100.2497& 141.2778& -259.7326&& 52.5745 & 10.1098 & -140.2130 \\

\bottomrule
\end{tabularx}

\caption{Caption}
\end{table*}
```

## Row Composition

*Table 1 demonstrates basic row composition with a two-column layout showing categories and descriptions.*

- Use smaller font sizes for tables:

```latex
\begin{table}
  \footnotesize
  \begin{tabular}{...}
```

- No justified text in narrow columns. Better (array.sty):

```latex
\newcolumntype{v}[1]{%
  >{\raggedright\hspace{0pt}}p{#1}%
}
```

This produces ragged-right text of the specified width, with hyphenation possible even in the first word.

- Cell break with `\\`, line break with `\tabularnewline`
- `\addlinespace` for group separation (from booktabs.sty)

---

## Multi-Column Row Composition

*Table 2 shows a multi-column layout for declension tables (nominative, genitive, dative, accusative cases).*

- Use the `*` command:

```latex
\begin{tabular}{*{4}{l}}
```

---

## Table Composition with Lines

*Table 3 demonstrates proper table composition with horizontal rules separating the header from the body.*

- Tables have head rules (`\toprule`), neck rules (`\midrule`), and foot rules (`\bottomrule`)
- Avoid overhanging lines with `@{}`:

```latex
\begin{tabular}{@{}*{4}{l}@{}}
```

---

## Application of Lines

*Table 4 shows monthly data across years (1965-1968) with proper decimal alignment.*

- Align numbers first at the decimal separator, then left-aligned (dcolumn.sty):

```latex
\makeatletter
\newcolumntype{d}[1]{%
  >{\DC@{.}{,}{#1}}l<{\DC@end}%
}
\makeatother
```

In this example: `d{4.0}`

- Using a decimal point in the table source code avoids incompatibility of dcolumn.sty with the FAQ trick
- Column assignment with trimmed `\cmidrule` lines:

```latex
\cmidrule(r){1-1}\cmidrule(lr){2-2}%
  \cmidrule(lr){3-3}\cmidrule(lr){4-4}%
  \cmidrule(l){5-5}
```

---

## Font Sizes

*Table 5 presents telephone call statistics for various German cities, demonstrating the use of smaller fonts in headers.*

- Set header 1-2 sizes smaller, necessary column types:

```latex
\newcolumntype{N}{>{\scriptsize}l}
\newcolumntype{V}[1]{%
  >{\scriptsize\raggedright\hspace{0pt}}p{#1}%
}
```

- Format override with `\multicolumn`:

```latex
\multicolumn{1}{@{}N}{Location} &
...
\multicolumn{1}{V{6em}@{}}{%
  Long-distance calls in subscriber trunk dialing%
} \\
```

---

## Structuring with Space in Table Footer

*Table 6 shows fuse inserts with switch types, weights, and prices, using vertical space for visual grouping.*

- Units in the table header (units.sty)
- `\addlinespace` after neck line and before foot line
- For missing cents in d-columns use `$---$`

---

## Structuring with Lines in Table Footer

*Table 7 presents the same data as Table 6 but uses horizontal lines instead of space for group separation.*

- Significantly less space required
- Creates a more formal, harder visual effect

---

## Subdivided Table Header

*Table 8 shows monthly data split by gender (Women/Men) with years as sub-columns.*

- For marking "subsets", for example:

```latex
\multicolumn{1}{@{}N}{Month} &
\multicolumn{2}{N}{Women} &
\multicolumn{2}{N@{}}{Men} \\
\cmidrule(lr){2-3}\cmidrule(l){4-5}
  &
  \multicolumn{1}{N}{1967} &
  \multicolumn{1}{N}{1968} &
  \multicolumn{1}{N}{1967} &
  \multicolumn{1}{N@{}}{1968} \\
\cmidrule(r){1-1}...
```

---

## Text Amount in Table Header

*Table 9 demonstrates handling large amounts of text in headers, with explanatory text and units on separate rows.*

- Explanations after head line, units before neck line, allocate space to parent fields
- A multi-line field next to multiple single-line fields or lines:

```latex
\newcommand{\armultirow}[3]{%
  \multicolumn{#1}{#2}{%
    \begin{picture}(0,0)%
      \put(0,0){%
        \begin{tabular}[t]{@{}#2@{}}%
          #3%
        \end{tabular}%
      }%
    \end{picture}%
  }%
}%
```

- Subsequent rows *must* remain empty! No space reservation! No vertical fine-tuning like with multirow.sty needed:

```latex
...
\multicolumn{2}{N}{Without Fuses} &
\armultirow{1}{V{5em}@{}}{%
  Maximum permissible grounding resistance at contact voltage%
} \\
\\
\\
\cmidrule(lr){3-4}
  &
  &
  \multicolumn{1}{N}{Type} &
  \multicolumn{1}{N}{Price} \\
  &
  \multicolumn{1}{N}{\unit{V}} &
  &
  \multicolumn{1}{N}{DM} \\
\cmidrule(r){1-1}...
```

---

## Rotated Header

*Table 10 shows a table with rotated column headers for technical specifications (operating voltage, extinction voltage, etc.).*

- Only rotate fields in the table header as a last resort (readable from the right), column type (rotating.sty):

```latex
\newcolumntype{R}[1]{%
  >{\begin{turn}{90}\begin{minipage}{#1}%
      \scriptsize\raggedright\hspace{0pt}}l%
  <{\end{minipage}\end{turn}}%
}
```

- In the example:

```latex
\cmidrule(lr){2-7}
  &
  \multicolumn{1}{R{6em}}{Operating...} &
  ...
  \multicolumn{1}{R{6em}}{Weight ...} &
  \multicolumn{1}{N@{}}{DM} \\
\cmidrule(r){1-1}...
```

---

## Cathode Drop Arresters

*Table 11 presents a complex rotated table with voltage protection specifications for networks.*

- Declaration: `@{}nd{1.1}*{3}{d{1.2}}d{1.1}d{3.2}@{}`
- Example row: `H 484--2 & 2 & 2.3 & 2.5 & 2.9 & 2 & 252.$---$ \\`

---

## Overview of Time Characteristic Distribution

*Table 12 shows a wide rotated table comparing latency times, half-value times, and peak times across different material sources.*

---

## Components for L-System 125

*Table 13 lists components with order numbers and prices for four-wire and five-wire systems.*

- Use of `\armultirow`:

```latex
...\cmidrule(l){4-5}
  &
  \armultirow{1}{V{3.5em}}{Order No.} &
  \multicolumn{1}{V{2.5em}}{Price} &
  \armultirow{1}{V{3.5em}}{Order No.} &
  \multicolumn{1}{V{2.5em}@{}}{Price} \\
  &
  &
  \multicolumn{1}{V{2em}}{DM} &
  &
  \multicolumn{1}{V{2.5em}@{}}{DM} \\
\cmidrule(r){1-1}...
```

---

## Frequency Converter Inserts

*Table 14 shows frequency converter specifications with channel ranges and construction types.*

- Declaration: `@{}nnd{2.0}@{$\!$--}d{2.0}d{3.0}nd{1.0}@{$\!$--}d{2.0}d{3.0}n@{}`
- Use of `\armultirow`:

```latex
\multicolumn{8}{N}{For Converting} &
\armultirow{1}{V{2.5em}@{}}{Construction Type} \\
\cmidrule(lr){2-9}
```

---

## Star-Delta Switch K 7435

*Table 15 presents switch size specifications with power consumption and voltage data.*

- Use of `\armultirow`:

```latex
\toprule
\armultirow{1}{@{}V{4em}}{Switch Size} &
\multicolumn{4}{N}{Power Consumption} &
\multicolumn{1}{N}{Voltage} &
\armultirow{1}{V{5.5em}@{}}{%
  Extra charge for different voltages%
} \\
\cmidrule(lr){2-5}
```

---

## Technical Data for House Connection Boxes

*Table 16 shows list numbers, rated current, pole count, and connection specifications.*

- Declaration: `@{}*{3}{d{3.0}}d{2.0}*{3}{f}n@{}`
- Column type for formulas: `\newcolumntype{f}{>{$}l<{$}}`
- Example row:

```latex
406 & 416 & 426 & 25 & 3+\mathrm{Mp} & 4\times16 & 4\times16 & Pg 21 \\
```

---

## Physicians in Medical Institutions

*Table 17 displays a complex rotated table showing physician statistics across different medical institutions.*

---

## Performance Data of the Capri

*Table 18 shows automotive performance data including displacement, power, acceleration, top speed, and fuel consumption.*

- Declaration: `@{}d{4.0}d{2.0}d{2.1}B{3.0}d{2.1}n@{}`
- Bold in table header without new column type:

```latex
\multicolumn{1}{>{\bfseries}V{4.5em}}{%
  Top Speed%
} &
...
\multicolumn{1}{>{\bfseries}N}{\unitfrac{km}{h}} &
```

- Emphasis in footer through bold, column type:

```latex
\makeatletter
\newcolumntype{B}[1]{%
  >{\boldmath\DC@{.}{,}{#1}}l<{\DC@end}%
}
\makeatother
```

---

## Alternative Table Orientation

*Table 19 shows the same Capri data in a rotated/transposed format with rows and columns swapped.*

- The first two columns ("legend") smaller
- Separate column for units
- Otherwise no sensible column declaration possible
- Error-prone, cumbersome manual formatting (`\textbf` for each cell of the "Top Speed" row)
- Despite many lines (formal hardness), higher space requirement and greater lack of clarity

---

## Old-Style Numerals

*Table 20 demonstrates the use of old-style (lowercase) numerals in tables.*

- Old-style numerals (0123456789, with `\oldstylenums{...}`) are more distinguishable than lining numerals (01234567890)
- Relatively unfamiliar for classicist antiqua (Computer Modern Roman)
- Typical for Renaissance or Baroque antiqua, but only contained in the "expert sets" of the fonts
- Group separation with `\addlinespace`
- Further structuring through "subheadings"
- Declaration: `@{}v{7em}i{4.0}i{3.0}i{5.0}n@{}`
- Column type:

```latex
\makeatletter
\newcolumntype{i}[1]{%
  >{\DC@{.}{,}{#1}\mathnormal\bgroup}l%
  <{\egroup\DC@end}%
}
\makeatother
```

- Use of `\armultirow`:

```latex
\armultirow{1}{@{}v{7em}}{%
  Through belongs want and%
} &
1994 & 87 & 46475 & \oldstylenums{957} one \\
```

---

## Sans-Serif Variant

*Table 21 presents the same data as Table 20 but using sans-serif fonts throughout.*

- Sans-serif for clearer separation between floating tables and main text:

```latex
\begin{table}
  \sffamily
```

- Customization of table caption (caption2.sty):

```latex
\renewcommand{\captionfont}{%
  \normalfont\sffamily\itshape\footnotesize
}
\renewcommand{\captionlabelfont}{%
  \normalfont\sffamily\bfseries\footnotesize
}
```

- Column type:

```latex
\newcolumntype{s}[1]{%
  >{\DC@{.}{,}{#1}\mathsf\bgroup}l%
  <{\egroup\DC@end}%
}
```

---

## Right-Cleared Space

*Table 22 demonstrates a table stretched to full column width with extra space on the right.*

- Emphasizes the text block width
- Declaration (tabularx.sty):

```latex
\begin{tabularx}{\columnwidth}{%
  @{}nd{1.1}d{3.5}d{1.3}@{}%
}
```

- Column type in header (`\multicolumn{1}{x@{}}{equal man}`):

```latex
\newcolumntype{x}{%
  >{\scriptsize\raggedright\hspace{0pt}}X%
}
```

---

## Superordinate System Through Lines

*Table 23 shows a table using horizontal lines to create equal-height "compartments" for a grid-like structure.*

- Equal-height "compartments"
- Calmer than design with indentation
- Calmer than horizontal lines with uneven spacing
- Error-prone manual work when inserting `\tabularnewline`

---

## References

1. Barroca, L.: *A style option for rotated objects in LaTeX*, Aug. 1995. Version 2.10.
2. Carlisle, D.: *The dcolumn package*, Sept. 1996. Version 1.04.
3. Carlisle, D.: *The tabularx package*, May 1998. Version 2.06.
4. Fear, S.: *Publication quality tables in LaTeX*, Nov. 1995. Version 1.00.
5. Fiebig, D.: "Table Typesetting." Technical Publication Series F11, Industrial Union Printing and Paper, Stuttgart, 1971.
6. Leichter, J.: *multirow.sty*, May 1994. Version 1.2.
7. Mittelbach, F.; Carlisle, D.: *A new implementation of LaTeX's tabular and array environment*, May 1998. Version 2.31.
8. Raichle, B.; Hafner, T.; Niepraschk, R.: "Questions and Answers (FAQ) about the Typesetting System TeX and DANTE, German-Speaking TeX User Group e.V.", Aug. 1998. Version 42.
9. Reichert, A.: "Floating Objects - the Right Lubrication.", Oct. 1997.
10. Reichert, A.: *units.sty - nicefrac.sty*. Dusseldorf, Aug. 1998. Version 0.9b.
11. Sommerfeldt, H. A.: *The caption package*, Apr. 1995. Version 1.4b.
12. Sommerfeldt, H. A.: *The caption package*, Oct. 1995. Version 2.0.
13. Willberg, H. P.; Forssman, F.: *Reading Typography*. Hermann Schmidt, Mainz, 1997.

---

## Summary of Key Packages

| Package      | Purpose                                                                                                  |
| ------------ | -------------------------------------------------------------------------------------------------------- |
| `array`    | Extended column type definitions with `>{}` and `<{}`                                                |
| `booktabs` | Professional table lines (`\toprule`, `\midrule`, `\bottomrule`, `\cmidrule`, `\addlinespace`) |
| `dcolumn`  | Decimal-aligned number columns                                                                           |
| `tabularx` | Tables stretched to specified width                                                                      |
| `rotating` | Rotated table elements                                                                                   |
| `units`    | Proper unit formatting                                                                                   |
| `caption2` | Caption customization                                                                                    |
| `multirow` | Cells spanning multiple rows                                                                             |

## Key Column Type Definitions

```latex
% Ragged-right paragraph column
\newcolumntype{v}[1]{%
  >{\raggedright\hspace{0pt}}p{#1}%
}

% Decimal-aligned column (point in source, comma in output)
\makeatletter
\newcolumntype{d}[1]{%
  >{\DC@{.}{,}{#1}}l<{\DC@end}%
}
\makeatother

% Small header column
\newcolumntype{N}{>{\scriptsize}l}

% Small ragged-right paragraph column
\newcolumntype{V}[1]{%
  >{\scriptsize\raggedright\hspace{0pt}}p{#1}%
}

% Rotated column
\newcolumntype{R}[1]{%
  >{\begin{turn}{90}\begin{minipage}{#1}%
      \scriptsize\raggedright\hspace{0pt}}l%
  <{\end{minipage}\end{turn}}%
}

% Formula column (math mode)
\newcolumntype{f}{>{$}l<{$}}

% Bold decimal column
\makeatletter
\newcolumntype{B}[1]{%
  >{\boldmath\DC@{.}{,}{#1}}l<{\DC@end}%
}
\makeatother

% Old-style numeral decimal column
\makeatletter
\newcolumntype{i}[1]{%
  >{\DC@{.}{,}{#1}\mathnormal\bgroup}l%
  <{\egroup\DC@end}%
}
\makeatother

% Sans-serif decimal column
\newcolumntype{s}[1]{%
  >{\DC@{.}{,}{#1}\mathsf\bgroup}l%
  <{\egroup\DC@end}%
}

% Expandable column for tabularx
\newcolumntype{x}{%
  >{\scriptsize\raggedright\hspace{0pt}}X%
}
```

## Multi-Row Helper Command

```latex
\newcommand{\armultirow}[3]{%
  \multicolumn{#1}{#2}{%
    \begin{picture}(0,0)%
      \put(0,0){%
        \begin{tabular}[t]{@{}#2@{}}%
          #3%
        \end{tabular}%
      }%
    \end{picture}%
  }%
}
```
