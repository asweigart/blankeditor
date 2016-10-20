NORTH = 'north'
EAST = 'east'
SOUTH = 'south'
WEST = 'west'

class Robot():
	def __init__(self, bearing=NORTH, startx=0, starty=0):
		self.coordinates = (startx, starty) # tuple of two integers for x and y
		self.bearing = bearing

	def turn_right(self):
		if self.bearing == NORTH:
			self.bearing = EAST
		elif self.bearing == EAST:
			self.bearing = SOUTH
		elif self.bearing == SOUTH:
			self.bearing = WEST
		elif self.bearing == WEST:
			self.bearing = NORTH

	def turn_left(self):
		if self.bearing == NORTH:
			self.bearing = WEST
		elif self.bearing == EAST:
			self.bearing = NORTH
		elif self.bearing == SOUTH:
			self.bearing = EAST
		elif self.bearing == WEST:
			self.bearing = SOUTH

	def advance(self):
		if self.bearing == NORTH:
			self.coordinates = (self.coordinates[0], self.coordinates[1] + 1)
		elif self.bearing == EAST:
			self.coordinates = (self.coordinates[0] + 1, self.coordinates[1])
		elif self.bearing == SOUTH:
			self.coordinates = (self.coordinates[0], self.coordinates[1] - 1)
		elif self.bearing == WEST:
			self.coordinates = (self.coordinates[0] - 1, self.coordinates[1])


	def simulate(self, actions):
		for action in actions:
			if action == 'L':
				self.turn_left()
			elif action == 'R':
				self.turn_right()
			elif action == 'A':
				self.advance()
			else:
				assert False, 'Invalid action string.'
