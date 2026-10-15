-- Convert existing visible D/C/I/E/L marks into links to the canonical matrix.

local function matrix_target(identifier)
  -- Every visible evidence mark lives in a chapter two levels below the
  -- publication root (content/01-catastro or content/02-estudio).  Keeping
  -- this target explicit also makes it stable when Quarto invokes Pandoc
  -- with temporary or root-relative input paths.
  return "../../generated/matriz-evidencia.qmd#evidencia-" .. identifier:lower()
end

local function linked_mark(levels, identifiers)
  local output = pandoc.Inlines({pandoc.Str("[" .. levels .. ":"), pandoc.Space()})
  for index, identifier in ipairs(identifiers) do
    if identifier:match("^CAL%-%d%d%d$") then
      -- CAL identifiers belong to the separate calculation registry, not to
      -- the 111-entry D/C/I/E/L matrix.  Keep them visible without creating a
      -- false matrix destination.
      output:insert(pandoc.Str(identifier))
    else
      output:insert(pandoc.Link(identifier, matrix_target(identifier)))
    end
    if index < #identifiers then
      output:insert(pandoc.Str(","))
      output:insert(pandoc.Space())
    end
  end
  output:insert(pandoc.Str("]"))
  return output
end

local function transform(inlines)
  local output = pandoc.Inlines({})
  local index = 1
  while index <= #inlines do
    local item = inlines[index]
    local levels = item.t == "Str" and item.text:match("^%[([DCIEL/]+):$") or nil
    if not levels then
      output:insert(item)
      index = index + 1
    else
      local finish = index + 1
      local visible = item.text
      while finish <= #inlines do
        visible = visible .. " " .. pandoc.utils.stringify(inlines[finish])
        if inlines[finish].t == "Str" and inlines[finish].text:match("%]$") then
          break
        end
        finish = finish + 1
      end
      local identifiers = {}
      for identifier in visible:gmatch("[A-Z]+%-%d%d%d") do
        table.insert(identifiers, identifier)
      end
      if finish <= #inlines and #identifiers > 0 then
        output:extend(linked_mark(levels, identifiers))
        index = finish + 1
      else
        output:insert(item)
        index = index + 1
      end
    end
  end
  return output
end

function Para(block)
  block.content = transform(block.content)
  return block
end

function Plain(block)
  block.content = transform(block.content)
  return block
end
