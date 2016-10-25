
class Garden():
	def __init__(self, plants, students=('Alice', 'Bob', 'Charlie', 'David', 
										 'Eve', 'Fred', 'Ginny', 'Harriet', 
										 'Ileana', 'Joseph', 'Kincaid', 'Larry')):
		self.row1, self.row2 = plants.split('\n')
		self.students = sorted(students)

	@staticmethod
	def getPlantName(plantAbbrev):
		return {'V': 'Violets',
				'G': 'Grass',
				'C': 'Clover',
				'R': 'Radishes'}[plantAbbrev]

	def plants(self, studentName):
		studentIndex = self.students.index(studentName)

		return [Garden.getPlantName(self.row1[studentIndex * 2]), 
				Garden.getPlantName(self.row1[studentIndex * 2 + 1]),
				Garden.getPlantName(self.row2[studentIndex * 2]),
				Garden.getPlantName(self.row2[studentIndex * 2 + 1])]
