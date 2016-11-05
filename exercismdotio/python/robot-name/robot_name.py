import itertools
import random


class Robot():
	NEXT_NAME_NUMS = iter(range(1000))
	NEXT_NAME_LETTERS = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=2)
	LAST_NAME_LETTER = next(NEXT_NAME_LETTERS)

	def getNextName():
		try:
			num = next(Robot.NEXT_NAME_NUMS)
			letter = Robot.LAST_NAME_LETTER
		except StopIteration:
			try:
				letter = next(Robot.NEXT_NAME_LETTERS)
				Robot.LAST_NAME_LETTER = letter
			except StopIteration:
				Robot.NEXT_NAME_LETTERS = itertools.product('ABCDEFGHIJKLMNOPQRSTUVWXYZ', repeat=2)
				letter = next(Robot.NEXT_NAME_LETTERS)
				Robot.LAST_NAME_LETTER = letter
			Robot.NEXT_NAME_NUMS = iter(range(1000))
			num = next(Robot.NEXT_NAME_NUMS)

		return ''.join(letter) + str(num).zfill(3)

	def __init__(self):
		self.reset()

	def reset(self):
		if random.randint(0, 1) == 0:
			self.name = Robot.getNextName()
		else:
			Robot.getNextName()
			self.name = Robot.getNextName()
			