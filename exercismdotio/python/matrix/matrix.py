
class Matrix():
	def __init__(self, matrixString):
		self.rows = matrixString.split('\n')
		for rowIndex in range(len(self.rows)):
			self.rows[rowIndex] = self.rows[rowIndex].split(' ')
			for elemIndex in range(len(self.rows[rowIndex])):
				self.rows[rowIndex][elemIndex] = int(self.rows[rowIndex][elemIndex])

		self.columns = []
		for columnIndex in range(len(self.rows[0])):
			currentColumn = []
			for rowIndex in range(len(self.rows)):
				currentColumn.append(self.rows[rowIndex][columnIndex])
			self.columns.append(currentColumn)



