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
-- Terskel for å rotere brede tabeller til landskap. Ingen tabell har lenger
-- så mange kolonner (Tabell 9.1 er restrukturert til 8 kolonner for å stå i
-- portrett; 6.2 og 7.2 har også 8). Beholdes som sikring mot framtidige
-- svært brede tabeller.
local LANDSCAPE_THRESHOLD = 11

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

-- Returnerer true hvis en header-celle inneholder den gitte tekstbiten.
-- Brukes til å kjenne igjen den teksttunge Tabell 9.1 (modellprofil) uten å
-- hardkode tabellrekkefølge. Må kalles før header-ord brytes med \splitword,
-- ellers gjemmes teksten i RawInline og stringify finner den ikke.
local function header_contains(t, needle)
  for _, row in ipairs(t.head.rows) do
    for _, cell in ipairs(row.cells) do
      for _, block in ipairs(cell.contents) do
        if pandoc.utils.stringify(block):find(needle, 1, true) then
          return true
        end
      end
    end
  end
  return false
end

function Table(t)
  local ncols = #t.colspecs
  if ncols == 0 then
    return nil
  end

  -- Tabell 9.1 (modellprofil) har to korte tallkolonner, to vinnerkolonner
  -- og tre brede prosakolonner. Den kjennes igjen på «Hovedsvakhet»-headeren
  -- og får en eksplisitt breddeprofil med smale ledende kolonner og brede
  -- tekstkolonner; ellers ville lik bredde gjøre prosakolonnene for smale.
  -- Den må detekteres her, før header-ord eventuelt brytes med \splitword.
  local textheavy = (ncols == 8) and header_contains(t, "svakhet")

  if textheavy then
    -- Modell-rolle, RMSE, MAPE, Vinner-måneder, Vinner-segmenter,
    -- Tolk-barhet, Hoved-styrke, Hoved-svakhet. Summerer til 1,0 slik at
    -- tabellen fyller full tekstbredde på linje med de øvrige tabellene.
    local widths = {0.12, 0.08, 0.08, 0.10, 0.11, 0.09, 0.21, 0.21}
    for i = 1, ncols do
      t.colspecs[i][2] = widths[i]
    end
  else
    local width = 1.0 / ncols
    for i = 1, ncols do
      t.colspecs[i][2] = width
    end
  end

  -- Bryt lange ubrudte ord. Hovedheaderen ligger på t.head.rows
  -- (terskel 10); intermediate header-rader på body.head (sjelden brukt)
  -- og data-rader på body.body får body-terskelen (14). foot prosesseres
  -- ikke siden rapporten ikke bruker foot-rader i tabellene.
  -- For den teksttunge Tabell 9.1 hoppes \splitword over helt: cellene er
  -- norsk prosa uten kode-identifikatorer, så babels orddeling gir penere
  -- linjebryting enn tegn-for-tegn-splitting i de smale kolonnene.
  if not textheavy then
    process_rows(t.head.rows, break_long_str_header)
    for _, body in ipairs(t.bodies) do
      process_rows(body.head, break_long_str_header)
      process_rows(body.body, break_long_str_body)
    end
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
