
def calculate(wordProblem):
	if not wordProblem.startswith('What is '):
		raise ValueError()

	if not wordProblem.endswith('?'):
		raise ValueError()

	wordProblem = wordProblem[8:-1]
	wordProblem = wordProblem.replace('multiplied by', 'multiplied_by')
	wordProblem = wordProblem.replace('divided by', 'divided_by')
	wordProblem = wordProblem.split()

	# check that the word problem has integers and operations only
	expectInteger = True
	for word in wordProblem:
		int(expectInteger) # raises ValueError if not an integer
		
		if not expectInteger and word not in ('plus', 'minus', 'multiplied_by', 'divided_by'):
			raise ValueError()
		expectInteger = not expectInteger

	# solve the word problem
	total = int(wordProblem[0])
	for index, word in enumerate(wordProblem):
		if index % 2 == 0:
			continue # skip the numbers

		if word == 'plus':
			total += int(wordProblem[index + 1])
		elif word == 'minus':
			total -= int(wordProblem[index + 1])
		elif word == 'multiplied_by':
			total *= int(wordProblem[index + 1])
		elif word == 'divided_by':
			total /= int(wordProblem[index + 1])

	return total