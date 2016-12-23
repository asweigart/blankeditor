-- 3d printer program by Al Sweigart
-- Runs in ComputerCraft

--[[
To use this program, run "3dprint <blueprint file>" from the turtle's shell.

The blueprint is a text file with the following format:

* A legend section, where a single letter represents a type of block
* A section for the bottommost layer, showing the blocks used.
* A section for the next layer up, and so on.
* Sections are ended by a line with nothing but a ~ character.
* You can get the block name by running turtle.getItemDetail() on the turtle's inventory.
* Periods are blank spaces.
* The turtle starts at the top left corner of the blueprint, building in front and to its left.

Example blueprint file for a small cobblestone pyramid with a stonebrick peak:
C=minecraft:cobblestone
B=minecraft:stonebrick
~
CCCCC
CCCCC
CCCCC
CCCCC
CCCCC
~
....
.CCC
.CCC
.CCC
~
...
...
..S
~








]]


-- NOTE: copy/pasted from my "hare" program
function sweepField(forward, left, sweepFunc)
  local x = 0
  local y = 0
  local i

  while true do
    -- moving forward AWAY from the home space
    while y < forward - 1 do
      if sweepFunc ~= nil then
        sweepFunc(x, y)
      end

      if not turtle.forward() then return false end
      y = y + 1
    end

    -- call the sweep function at the furthest row from the home space
    if sweepFunc ~= nil then
      sweepFunc(x, y)
    end

    -- check if this is the last column
    if x == left - 1 then
      break
    end

    -- turn left to next
    turtle.turnLeft()
    if not turtle.forward() then return false end
    x = x + 1
    turtle.turnLeft()

    -- moving forward TOWARDS from the home space
    while y > 0 do
      if sweepFunc ~= nil then
        sweepFunc(x, y)
      end

      if not turtle.forward() then return false end
      y = y - 1
    end

    -- call the sweep function at the closest row from the home space
    if sweepFunc ~= nil then
      sweepFunc(x, y)
    end

    -- check if this is the last column
    if x == left - 1 then
      break
    end

    -- turn right to next
    turtle.turnRight()
    if not turtle.forward() then return false end
    x = x + 1
    turtle.turnRight()
  end

  -- move back to the home space
  if left % 2 == 0 then
    -- even number of columns traversed means we ended closest to the home row
    turtle.turnLeft()
    for i = 1, left - 1 do
      if not turtle.forward() then return false end
    end
    turtle.turnLeft()
  else
    -- odd number of columns traversed means we ended furtherst from the home row
    for i = 1, forward - 1 do
      if not turtle.back() then return false end
    end
    turtle.turnRight()
    for i = 1, left - 1 do
      if not turtle.forward() then return false end
    end
    turtle.turnLeft()
  end

  return true
end


-- NOTE: copy/pasted from my "hare" program
-- findItem() returns inventory slot 
-- that has the named item, or nil if not found
function findItem(name)
  local slot, item

  -- first try to find an exact name match
  for slot = 1, 16 do
    item = turtle.getItemDetail(slot)
    if item ~= nil and item['name'] == name then
      return slot
    end
  end

  -- don't try a similar match if name
  -- has a colon (like "minecraft:")
  if string.find(name, ':') ~= nil then
    return nil  -- couldn't find item
  end

  -- next try to find a similar name match
  for slot = 1, 16 do
    item = turtle.getItemDetail(slot)
    if item ~= nil and string.find(item['name'], name) then
      return slot
    end
  end

  return nil  -- couldn't find item
end


-- NOTE: copy/pasted from my "hare" program
-- selectItem() selects the inventory
-- slot with the named item, returns
-- true if found and false if not
function selectItem(name)
  -- selects inventory slot that has the named item
  -- return true if found, false if not found
  local slot = findItem(name)

  if slot ~= nil then
    turtle.select(slot)
    return true
  else
    return false -- couldn't find item
  end
end


-- NOTE: copy/pasted from my "act" program
function split(str)
  -- splits a string into an array of strings
  -- Example: 'a b c' -> {'a', 'b', 'c'}
  local result, word

  result = {}
  -- Note: The gmatch() function is
  -- beyond the scope of this book.
  for word in str:gmatch("%w+") do 
    table.insert(result, word) 
  end
  return result
end


function getTurtleInventoryCounts()
  local currentInventory = {}
  local slot
  for slot = 1, 16 do
    local itemDetails = turtle.getItemDetail(slot)
    if itemDetails ~= nil then
      if currentInventory[itemDetails['name']] == nil then
        currentInventory[itemDetails['name']] = itemDetails['count']
      else
        currentInventory[itemDetails['name']] = currentInventory[itemDetails['name']] + itemDetails['count']
      end
    end
  end
  return currentInventory
end  


function buildBlockFunction(x, y)
  -- currentLayer is a global variable we can use for the layer number
  if bp[x .. ',' .. y .. ',' .. currentLayer] == nil then
    -- no block at this position, so just return
    return
  end

  local blockName = legend[bp[x .. ',' .. y .. ',' .. currentLayer]]
  if selectItem(blockName) == false then
    error('Could not find a ' .. blockName .. ' block in inventory.')
  end

  turtle.placeDown()
end




local SECTION_END_MARK = '~'

local cliArgs = {...}
local blueprintFile = cliArgs[1]

local i, bpNumLayers, slot

if blueprintFile == nil then
  print('Usage: 3dprint <blueprintFile>')
  return
end

-- validate the blueprint file
if not fs.exists(blueprintFile) then
  error('Cannot find blueprint file ' .. blueprintFile)
end

legend = {} -- contains all the legend information from the blueprint file, NOTE: this is a global variable

-- parse the blueprint's key
bpNumLayers = 0
local fp = fs.open(blueprintFile, 'r')
local line = fp.readLine()
while line ~= SECTION_END_MARK do
  -- check for early end of file
  if line == nil then
    error('Unexpected end of file in legend section.')
  end

  -- check that there's an equal sign
  if string.sub(line, 2, 2) ~= '=' then
    error('No equal sign in legend section line: ' .. line)
  end

  -- make sure a block name is after the equal sign
  if string.len(string.sub(line, 3)) == 0 then
    error('No block name given for key: ' .. string.sub(line, 1, 1))
  end

  -- Ex. if line is 'C=minecraft:cobblestone', key is 'C' and value is 'minecraft:cobblestone'
  legend[string.sub(line, 1, 1)] = string.sub(line, 3)

  line = fp.readLine()
end


bp = {} -- NOTE: this is a global variable
local bpLayerSizes = {} -- keys '<layerNum>width' for width and '<layerNum>length' for length of each layer

print('Parsing blueprint...')

-- parse the layers of the blueprint
local bpchar, x, y, z
z = 0
while true do
  --print('layer: ' .. z)
  -- read in a single layer section

  bpLayerSizes[z .. 'maxx'] = 0
  bpLayerSizes[z .. 'maxy'] = 0

  line = fp.readLine()
  if line == nil then
    --print('end of file')
    break
  end

  y = 0
  -- read in all the lines for this layer
  while line ~= SECTION_END_MARK do
    --print('line y: ' .. y)
    -- read in each character from the line
    for i = 1, string.len(line) do
      x = i - 1
      --print('char x: ' .. x)
      local bpchar = string.sub(line, i, i)
      if bpchar ~= '.' then -- ignore periods in the blueprint file
        bp[x .. ',' .. y .. ',' .. z] = bpchar
        --print(x .. ',' .. y .. ',' .. z .. '=' .. bpchar)

        -- check to see if we should expand the size in bpLayerSizes
        if x > bpLayerSizes[z .. 'maxx'] then
          bpLayerSizes[z .. 'maxx'] = x
        end
        if y > bpLayerSizes[z .. 'maxy'] then
          bpLayerSizes[z .. 'maxy'] = y
        end
        
      end
    end

    line = fp.readLine()
    if line == nil then
      error('Unexpected end of file in layer ' .. z)
    end
    y = y + 1
  end

  bpNumLayers = bpNumLayers + 1
  z = z + 1
end
fp.close()


-- start building

currentLayer = 0  -- NOTE: this is a global variable
local coordinates, blockChar, itemDetails, blockName, numBlocksNeeded 
while currentLayer < bpNumLayers do
  print('Building layer ' .. currentLayer .. '...')
  
  turtle.up() -- move up first to build this layer

  -- do an inventory check to see if you can build the current layer

  -- count up the kinds of blocks and amount needed of each kind for the current layer
  currentLayerBlockNeeds = {}
  for coordinates, blockChar in pairs(bp) do
    -- coordinates is going to be an xyz coordinate string, ex. '2,60,0'
    coordinates = split(coordinates)
    if tonumber(coordinates[3]) == currentLayer then
      -- these coordinates are for the current layer
      if currentLayerBlockNeeds[legend[blockChar]] == nil then
        currentLayerBlockNeeds[legend[blockChar]] = 1
      else
        currentLayerBlockNeeds[legend[blockChar]] = currentLayerBlockNeeds[legend[blockChar]] + 1
      end
    end
  end

  -- count up the kinds of blocks and amount of each kind in the turtle's inventory
  currentInventory = getTurtleInventoryCounts()

  -- compare currentLayerBlockNeeds with currentInventory to make sure we have enough blocks of each type
  for blockName, numBlocksNeeded in pairs(currentLayerBlockNeeds) do
    local numBlocksHave
    if currentInventory[blockName] == nil then
      numBlocksHave = 0
    else 
      numBlocksHave = currentInventory[blockName]
    end

    if numBlocksHave < numBlocksNeeded then
      -- we don't have enough blocks, calculate how many more we need
      print('Need ' .. (numBlocksNeeded - numBlocksHave) .. ' more ' .. blockName)

      while true do
        -- keep waiting until the player adds the needed blocks
        os.sleep(1)
        currentInventory = getTurtleInventoryCounts() -- recheck the inventory numbers
        if currentInventory[blockName] ~= nil and currentInventory[blockName] >= numBlocksNeeded then
          break
        end
      end
    end
  end
  

  -- we have enough blocks to begin building this layer
  sweepField(bpLayerSizes[currentLayer .. 'maxy'] + 1, bpLayerSizes[currentLayer .. 'maxx'] + 1, buildBlockFunction)
  
  currentLayer = currentLayer + 1
end