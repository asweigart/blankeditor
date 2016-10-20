import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

def slices(fullString, substringLength):
	if substringLength > len(fullString) or substringLength == 0:
		raise ValueError()

	series = []
	# '012345'  3  length 6, return 4 series
	for index in range(0, len(fullString) - substringLength + 1):
		logging.debug(list(fullString[index:index+substringLength]))

		series.append(list(fullString[index:index+substringLength]))
		for numericStringIndex in range(len(series[-1])):
			series[-1][numericStringIndex] = int(series[-1][numericStringIndex])

		logging.debug(series[-1])
	return series
