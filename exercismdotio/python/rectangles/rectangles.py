import itertools, logging
logging.basicConfig(level=logging.DEBUG)

X = 0
Y = 1

def count(lines=''):
	if len(lines) == 0 or type(lines) == str:
		return 0 


	# store lines as a 2D map
	twoDMap = {}
	height = len(lines)
	width = len(lines[0])

	for y in range(len(lines)):
		for x in range(len(lines[y])):
			twoDMap[(x, y)] = lines[y][x]

	# find all the + (these are the corners)
	corners = []
	for x in range(width):
		for y in range(height):
			if twoDMap[(x, y)] == '+':
				corners.append((x,y))

	# get every combination of 4 corners from my list of corners
	rects = set() # rects is possibly connected rectangles. (Check for connecting lines later.)
	breakOut = False
	for fourCorners in itertools.combinations(corners, 4):
		for a, b, c, d in itertools.permutations(fourCorners):
			# a-b
			# | |
			# c-d
			if a[Y] == b[Y] and c[Y] == d[Y] and a[X] == c[X] and b[X] == d[X]:
				# a, b, c, and d are corners that line up to be a rectangle
				# now check if there are | and - that connect these corners

				breakOut = False

				# check if a and b are connected
				for x in range(min(a[X], b[X]) + 1, max(a[X], b[X])):
					if twoDMap[ (x, a[Y]) ] not in ('-', '+'):
						breakOut = True
						break
				if breakOut:
					break

				# check if c and d are connected
				for x in range(min(c[X], d[X]) + 1, max(c[X], d[X])):
					if twoDMap[ (x, c[Y]) ] not in ('-', '+'):
						breakOut = True
						break
				if breakOut:
					break

				# check if a and c are connected
				for y in range(min(c[Y], a[Y]) + 1, max(c[Y], a[Y])):
					if twoDMap[ (c[X], y) ] not in ('|', '+'):
						breakOut = True
						break
				if breakOut:
					break

				# check if b and d are connected
				for y in range(min(b[Y], d[Y]) + 1, max(b[Y], d[Y])):
					if twoDMap[ (b[X], y) ] not in ('|', '+'):
						breakOut = True
						break
				if breakOut:
					break

				rects.add(frozenset((a, b, c, d)))
				break
		if breakOut:
			break

	return len(rects)