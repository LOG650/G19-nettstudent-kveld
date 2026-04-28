-- Pandoc Lua filter: gjør brede tabeller lesbare i pdflatex.
-- Strategi:
--   * Tildel like kolonnebredder (1/n) slik at pandoc genererer p{}-kolonner
--     som bryter linjer i stedet for å renne ut til høyre.
--   * Tabeller med >= 8 kolonner roteres til landskap via pdflscape.

function Table(t)
  local ncols = #t.colspecs
  if ncols == 0 then
    return nil
  end

  local width = 1.0 / ncols
  for i = 1, ncols do
    t.colspecs[i][2] = width
  end

  if ncols >= 8 then
    return {
      pandoc.RawBlock('latex', '\\begin{landscape}'),
      t,
      pandoc.RawBlock('latex', '\\end{landscape}')
    }
  end

  return t
end
