-- Pandoc Lua-filter for rapport-bygging.
--
-- Strategi:
--   * Tildel like kolonnebredder (1/n) i tabeller slik at pandoc genererer
--     p{}-kolonner som bryter linjer i stedet for å renne ut til høyre.
--   * Inline-kode (`xxx`) konverteres globalt til `\splitcode{xxx}`,
--     definert i header.tex med seqsplit. Det gir tegn-for-tegn brytbare
--     identifikatorer (`RandomForestRegressor`, `fit_intercept=True`)
--     uten visuell endring når plassen holder.
--   * Inne i tabellens body OG header får lange "ord" i ren tekst
--     brytbar form via `\splitword{...}`. Headers bruker en lavere
--     terskel (10 tegn) enn body (14 tegn), siden header-celler ofte
--     er smalere og parameternavn som `min_samples_leaf` / `max_features`
--     ellers renner ut i nabokolonnen.
--   * Bare hyphen (`-`) og slash (`/`) regnes som naturlige bryte-punkter.
--     LaTeX bryter ikke automatisk på `_`, `.` eller `=`, så ord som
--     inneholder disse må fortsatt gjennom `\splitword`.
--   * Tabeller med ≥ 10 kolonner roteres til landskap via pdflscape.
--     Terskelen er valgt slik at Tabell 9.1 (10 kolonner med tre lange
--     tekstkolonner) går i landskap, mens Tabell 6.2 og 7.2 (8 kolonner)
--     forblir i portrett.

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

local LONG_WORD_THRESHOLD_BODY   = 14
local LONG_WORD_THRESHOLD_HEADER = 10
local LANDSCAPE_THRESHOLD = 10

-- Bare hyphen og slash brytes automatisk av LaTeX. Underscore, punktum
-- og likhetstegn må gjennom \splitword for å bryte i smale kolonner.
local function has_natural_break(text)
  return text:find("[%-/]") ~= nil
end

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

local function make_break_long_str(threshold)
  return function(s)
    if utf8.len(s.text) > threshold and not has_natural_break(s.text) then
      return pandoc.RawInline("latex", "\\splitword{" .. escape_latex(s.text) .. "}")
    end
  end
end

local break_long_str_body   = make_break_long_str(LONG_WORD_THRESHOLD_BODY)
local break_long_str_header = make_break_long_str(LONG_WORD_THRESHOLD_HEADER)

-- Walker som anvender en gitt str-walker på alle Str-elementer innenfor
-- en liste med Block-elementer (typisk innholdet i en TableBody).
local function break_long_words_in_blocks(blocks, walker)
  local out = {}
  for _, block in ipairs(blocks) do
    out[#out + 1] = pandoc.walk_block(block, { Str = walker })
  end
  return out
end

local function process_rows(rows, walker)
  for _, row in ipairs(rows) do
    for _, cell in ipairs(row.cells) do
      cell.contents = break_long_words_in_blocks(cell.contents, walker)
    end
  end
end

-- Wrapper inline-innholdet i en blokk (typisk Plain/Para i en header-celle)
-- i \textbf, slik at tittel-raden settes i fet skrift. Eventuelle RawInline
-- (`\splitword{}`/`\splitcode{}`) som allerede er satt inn, beholdes inne i
-- Strong-wrapperen.
local function bold_blocks(blocks)
  local out = {}
  for _, block in ipairs(blocks) do
    if block.t == "Plain" then
      out[#out + 1] = pandoc.Plain({ pandoc.Strong(block.content) })
    elseif block.t == "Para" then
      out[#out + 1] = pandoc.Para({ pandoc.Strong(block.content) })
    else
      out[#out + 1] = block
    end
  end
  return out
end

local function bold_header_rows(rows)
  for _, row in ipairs(rows) do
    for _, cell in ipairs(row.cells) do
      cell.contents = bold_blocks(cell.contents)
    end
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

  -- Bryt lange ubrudte ord. Hovedheaderen ligger på t.head.rows
  -- (terskel 10); intermediate header-rader på body.head (sjelden brukt)
  -- og data-rader på body.body får body-terskelen (14). foot prosesseres
  -- ikke siden rapporten ikke bruker foot-rader i tabellene.
  process_rows(t.head.rows, break_long_str_header)
  for _, body in ipairs(t.bodies) do
    process_rows(body.head, break_long_str_header)
    process_rows(body.body, break_long_str_body)
  end

  -- Sett tittel-raden(e) i fet skrift.
  bold_header_rows(t.head.rows)
  for _, body in ipairs(t.bodies) do
    bold_header_rows(body.head)
  end

  if ncols >= LANDSCAPE_THRESHOLD then
    return {
      pandoc.RawBlock("latex", "\\begin{landscape}"),
      t,
      pandoc.RawBlock("latex", "\\end{landscape}"),
    }
  end

  return t
end
