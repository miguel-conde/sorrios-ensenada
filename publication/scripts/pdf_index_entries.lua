-- Give the generated `.index-entry` Divs a PDF-only presentation boundary.
-- HTML keeps using the existing SCSS class; data, order and locators are not
-- changed here.

function Div(div)
  if not div.classes:includes("index-entry") then
    return nil
  end

  local blocks = pandoc.List({
    pandoc.RawBlock("latex", "\\begin{PublicationIndexEntry}"),
  })
  blocks:extend(div.content)
  blocks:insert(pandoc.RawBlock("latex", "\\end{PublicationIndexEntry}"))
  return blocks
end
