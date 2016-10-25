local cmdArgs = {...}
local LENGTH = tonumber(cmdArgs[1])
local HEIGHT = tonumber(cmdArgs[2])
local WIDTH = tonumber(cmdArgs[3])

if cmdArgs[3] == nil then
	print('Usage: buildroom <length> <height> <width>')
	return
end

local i, j

turtle.up()
shell.run('buildfloor ' .. LENGTH .. ' ' .. WIDTH)

for j = 1, 2 do
	shell.run('buildwall ' .. (LENGTH - 1) .. ' ' .. WIDTH)
	turtle.forward()
	for i = 1, HEIGHT do
		turtle.down()
	end
	turtle.turnRight()


	shell.run('buildwall ' .. (WIDTH - 1) .. ' ' .. HEIGHT)
	turtle.forward()
	for i = 1, HEIGHT do
		turtle.down()
	end
	turtle.turnRight()
end

turtle.up()
shell.run('buildfloor ' .. LENGTH .. ' ' .. WIDTH)
