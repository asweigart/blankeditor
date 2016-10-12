import logging
logging.basicConfig(level=logging.DEBUG)


def slowWayOfSolving():
	#num = 8756438
	longestSeqLength = 0
	longestSeqStartingNum = 0
	for startingNum in range(1, 1000001):
		if startingNum % 10000 == 0:
			logging.debug('Starting Number %s' % (startingNum))
		num = startingNum
		collatzSeqLength = 1

		while num != 1:
			if num % 2 == 0:
				# is even
				num = num // 2
			else:
				# is odd
				num = 3 * num + 1
			collatzSeqLength += 1

		if collatzSeqLength > longestSeqLength:
			longestSeqLength = collatzSeqLength
			longestSeqStartingNum = startingNum
	return longestSeqStartingNum

def fastWayOfSolving():
	longestSeqLength = 0
	longestSeqStartingNum = 0

	lengthsCache = {1: 1}
	
	for startingNum in range(1, 1000001):
		if startingNum % 10000 == 0:
			logging.debug('Starting Number %s' % (startingNum))
		num = startingNum
		collatzSeqLength = 1

		while num != 1:
			if num % 2 == 0:
				# is even
				num = num // 2
			else:
				# is odd
				num = 3 * num + 1

			if num in lengthsCache:
				collatzSeqLength += lengthsCache[num]
				lengthsCache[startingNum] = collatzSeqLength
				break

			collatzSeqLength += 1
		lengthsCache[startingNum] = collatzSeqLength
		
		#logging.debug(lengthsCache)

		if collatzSeqLength > longestSeqLength:
			longestSeqLength = collatzSeqLength
			longestSeqStartingNum = startingNum
	return longestSeqStartingNum

print(fastWayOfSolving())