import logging
logging.basicConfig(level=logging.DEBUG)

SUBLIST = 'sublist'
SUPERLIST = 'superlist'
EQUAL = 'equal'
UNEQUAL = 'unequal'

def check_lists(needle, haystack, _makeRecursiveCall=True):
	for haystackStart in range(len(haystack) - len(needle) + 1):
		#logging.debug(haystackStart)
		#logging.debug(haystack[haystackStart:])
		foundMatch = True
		for needleIndex, needleChar in enumerate(needle):
			if needleChar != haystack[haystackStart + needleIndex]:
				foundMatch = False
				break

		if foundMatch and len(needle) == len(haystack):
			return EQUAL
		elif foundMatch:
			return SUBLIST

	if _makeRecursiveCall:
		if check_lists(haystack, needle, False) == SUBLIST:
			return SUPERLIST

	return UNEQUAL


