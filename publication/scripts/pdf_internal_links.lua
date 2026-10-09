-- Keep cross-document references readable in PDF without emitting broken .qmd
-- URI annotations. The PDF retains native linked contents, bookmarks and the
-- LaTeX page links generated for the nine indexes.

function Link(link)
  local path = link.target:match("^([^#?]+)")
  if path and path:match("%.qmd$") then
    return link.content
  end
end

function Pandoc(document)
  local blocks = pandoc.List()
  local compact_references = false
  for _, block in ipairs(document.blocks) do
    if block.t == "Header"
      and block.identifier == "referencias-cruzadas-4" then
      blocks:insert(pandoc.RawBlock("latex", "\\begingroup\\small"))
      compact_references = true
    end
    blocks:insert(block)
    if compact_references and block.t == "BulletList" then
      blocks:insert(pandoc.RawBlock("latex", "\\endgroup"))
      compact_references = false
    end
  end
  document.blocks = blocks
  return document
end
