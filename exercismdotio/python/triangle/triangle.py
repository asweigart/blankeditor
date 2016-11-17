

class TriangleError(Exception):
	pass

class Triangle():
	def __init__(self, x, y, z):
		if x <= 0 or y <= 0 or z <= 0:
			raise TriangleError

		if not ((x + y > z) and (x + z > y) and (y + z > x)):
			raise TriangleError

		self.x = x
		self.y = y
		self.z = z



	def kind(self):
		if self.x == self.y == self.z:
			return 'equilateral'

		if (self.x == self.y) or (self.x == self.z) or (self.y == self.z):
			return 'isosceles'

		return 'scalene'
