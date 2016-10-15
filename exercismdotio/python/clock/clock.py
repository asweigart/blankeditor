class Clock():
	def __init__(self, hour, minute):
		self.hour = int(hour) % 24
		self.minute = int(minute)

		# handle `minute` > 60 by adding to `self.hour`:
		self.hour += minute // 60
		self.minute %= 60

		self.hour %= 24

	def __str__(self):
		return str(self.hour).zfill(2) + ':' + str(self.minute).zfill(2)

	def __eq__(self, rightHandValue):
		return self.hour == rightHandValue.hour and self.minute == rightHandValue.minute

	def __ne__(self, rightHandValue):
		return not self.__eq__(rightHandValue)

	def add(self, minutesToAdd):
		self.minute += minutesToAdd
		hoursToAdd = self.minute // 60
		self.minute %= 60
		self.hour += hoursToAdd
		self.hour %= 24

		return Clock(self.hour, self.minute)

