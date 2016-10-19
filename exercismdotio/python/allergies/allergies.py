

class Allergies():
	def __init__(self, allergyScore):
		self.allergyScore = allergyScore
		self.lst = []

		# converts allergyScore to binary (as a string), cuts of '0b' prefix, and adds leading zeros:
		binScore = bin(self.allergyScore)[2:].zfill(8)

		if binScore[-1] == '1':
			self.lst.append('eggs')
		if binScore[-2] == '1':
			self.lst.append('peanuts')
		if binScore[-3] == '1':
			self.lst.append('shellfish')
		if binScore[-4] == '1':
			self.lst.append('strawberries')
		if binScore[-5] == '1':
			self.lst.append('tomatoes')
		if binScore[-6] == '1':
			self.lst.append('chocolate')
		if binScore[-7] == '1':
			self.lst.append('pollen')
		if binScore[-8] == '1':
			self.lst.append('cats')



	def is_allergic_to(self, substance):
		return substance.lower() in self.lst

