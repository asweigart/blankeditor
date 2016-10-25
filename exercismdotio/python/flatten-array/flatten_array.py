import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)
# nested = [1, [2, [3, 4], 5], 6]
# result = [1, 2, 3, 4, 5, 6]

def flatten(nested):
	result = []

	for index, value in enumerate(nested):
		logging.debug('%s %s' % (index, value))
		if type(value) == list or type(value) == tuple:
			result.extend( flatten(value) )
		else:
			result.append(value)

	result = [x for x in result if x != None]
	return result