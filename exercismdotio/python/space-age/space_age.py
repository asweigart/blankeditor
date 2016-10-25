SECS_IN_EARTH_YEAR   = 365.25 * 24 * 60 * 60
SECS_IN_MERCURY_YEAR = 0.2408467 * SECS_IN_EARTH_YEAR
SECS_IN_VENUS_YEAR   = 0.61519726  * SECS_IN_EARTH_YEAR
SECS_IN_MARS_YEAR    = 1.8808158 * SECS_IN_EARTH_YEAR
SECS_IN_JUPITER_YEAR = 11.862615 * SECS_IN_EARTH_YEAR
SECS_IN_SATURN_YEAR  = 29.447498 * SECS_IN_EARTH_YEAR
SECS_IN_URANUS_YEAR  = 84.016846 * SECS_IN_EARTH_YEAR
SECS_IN_NEPTUNE_YEAR = 164.79132 * SECS_IN_EARTH_YEAR

class SpaceAge():
	def __init__(self, seconds):
		self.seconds = seconds

	def on_earth(self):
		return round(self.seconds  / SECS_IN_EARTH_YEAR, 2)

	def on_mercury(self):
		return round(self.seconds  / SECS_IN_MERCURY_YEAR, 2)

	def on_venus(self):
		return round(self.seconds  / SECS_IN_VENUS_YEAR, 2)

	def on_mars(self):
		return round(self.seconds  / SECS_IN_MARS_YEAR, 2)

	def on_jupiter(self):
		return round(self.seconds  / SECS_IN_JUPITER_YEAR, 2)

	def on_saturn(self):
		return round(self.seconds  / SECS_IN_SATURN_YEAR, 2)

	def on_uranus(self):
		return round(self.seconds  / SECS_IN_URANUS_YEAR, 2)

	def on_neptune(self):
		return round(self.seconds  / SECS_IN_NEPTUNE_YEAR, 2)
