


class School():
	def __init__(self, name):
		self.name = name
		self.students = {} # keys are integer grades, values are lists of student names


	def grade(self, queryGrade):
		if queryGrade not in self.students:
			return []

		return self.students[queryGrade]


	def add(self, student, grade):
		self.students.setdefault(grade, [])

		self.students[grade].append(student)

	def sort(self):
		keys = list(self.students.keys())
		keys.sort()

		result = []
		for k in keys:
			studentNames = tuple(sorted(self.students[k]))
			result.append((k, studentNames))
		return result