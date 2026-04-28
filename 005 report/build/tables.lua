-- Pandoc Lua-filter for rapport-bygging.
--
-- Strategi:
--   * Tildel like kolonnebredder (1/n) i tabeller slik at pandoc genererer
--     p{}-kolonner som bryter linjer i stedet for å renne ut til høyre.
--   * Inline-kode (`xxx`) konverteres globalt til `\splitcode{xxx}`,
--     definert i header.tex med seqsplit. Det gir tegn-for-tegn brytbare
--     identifikatorer (`RandomForestRegressor`, `fit_intercept=True`)
--     uten visuell endring når plassen holder.
--   * Inne i tabellens body (ikke head/foot) får i tillegg lange "ord"
--     i ren tekst (ubrudte strenger > 14 tegn uten naturlige bryte-punkter)
--     brytbar form via `\splitword{...}`. Headers brekkes naturlig på
--     orddeling og hyphenation.
--   * Ord med naturlige bryte-punkter (`-`, `_`, `.`, `/`, `=`) får ikke
--     `\splitword` — LaTeX bryter ved tegnet selv og bevarer norsk
--     hyphenation.
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

local LONG_WORD_THRESHOLD = 14
local LANDSCAPE_THRESHOLD = 10

-- Ord som inneholder ett av disse tegnene har naturlige bryte-punkter
-- og trenger ikke kunstig tegn-for-tegn-bryting.
local function has_natural_break(text)
  return text:find("[%-_./=]") ~= nil
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

local function break_long_str(s)
  if utf8.len(s.text) > LONG_WORD_THRESHOLD and not has_natural_break(s.text) then
    return pandoc.RawInline("latex", "\\splitword{" .. escape_latex(s.text) .. "}")
  end
end

-- Walker som anvender break_long_str på alle Str-elementer innenfor
-- en liste med Block-elementer (typisk innholdet i en TableBody).
local function break_long_words_in_blocks(blocks)
  local out = {}
  for _, block in ipairs(blocks) do
    out[#out + 1] = pandoc.walk_block(block, { Str = break_long_str })
  end
  return out
end

-- Anvender splitword bare på body-radene i hver TableBody (ikke head/foot).
local function break_long_words_in_body(body)
  local function process_rows(rows)
    for _, row in ipairs(rows) do
      for _, cell in ipairs(row.cells) do
        cell.contents = break_long_words_in_blocks(cell.contents)
      end
    end
  end
  process_rows(body.body)
  return body
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

  -- Bryt lange ubrudte ord bare i tabellens body, ikke head/foot.
  for _, body in ipairs(t.bodies) do
    break_long_words_in_body(body)
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
