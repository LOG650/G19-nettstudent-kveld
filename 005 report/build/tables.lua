-- Pandoc Lua-filter for rapport-bygging.
--
-- Strategi:
--   * Tildel like kolonnebredder (1/n) i tabeller slik at pandoc genererer
--     p{}-kolonner som bryter linjer i stedet for å renne ut til høyre.
--   * Tabeller med ≥ 8 kolonner roteres til landskap via pdflscape.
--   * Inline-kode (`xxx`) konverteres globalt til `\splitcode{xxx}`,
--     definert i header.tex med seqsplit. Det gir tegn-for-tegn brytbare
--     identifikatorer (`RandomForestRegressor`, `fit_intercept=True`)
--     uten visuell endring når plassen holder.
--   * Inne i tabeller får i tillegg lange "ord" i ren tekst (ubrudte
--     strenger > 14 tegn, som klassenavn uten backticks) brytbar form
--     via `\splitword{...}`.

local LATEX_ESCAPES = {
  ["\\"] = "\\textbackslash{}",
  ["{"]  = "\\{",
  ["}"]  = "\\}",
  ["$"]  = "\\$",
  ["&"]  = "\\&",
  ["%"]  = "\\%",
  ["#"]  = "\\#",
  ["_"]  = "\\_",
  ["^"]  = "\\textasciicircum{}",
  ["~"]  = "\\textasciitilde{}",
}

local LONG_WORD_THRESHOLD = 14

local function escape_latex(text)
  local pieces = {}
  for _, codepoint in utf8.codes(text) do
    local ch = utf8.char(codepoint)
    pieces[#pieces + 1] = LATEX_ESCAPES[ch] or ch
  end
  return table.concat(pieces)
end

function Code(c)
  return pandoc.RawInline("latex", "\\splitcode{" .. escape_latex(c.text) .. "}")
end

local function break_long_str(s)
  if utf8.len(s.text) > LONG_WORD_THRESHOLD then
    return pandoc.RawInline("latex", "\\splitword{" .. escape_latex(s.text) .. "}")
  end
end

function Table(t)
  local ncols = #t.colspecs
  if ncols == 0 then
    return nil
  end

  local width = 1.0 / ncols
  for i = 1, ncols do
    t.colspecs[i][2] = width
  end

  -- Bryt lange ubrudte ord inne i celler (klassenavn osv.)
  t = pandoc.walk_block(t, { Str = break_long_str })

  if ncols >= 8 then
    return {
      pandoc.RawBlock("latex", "\\begin{landscape}"),
      t,
      pandoc.RawBlock("latex", "\\end{landscape}"),
    }
  end

  return t
end
