import functools
#import logging

#logging.basicConfig(level=logging.DEBUG)
#logging.disable(logging.CRITICAL)

@functools.lru_cache(None)
def g(N):
	#logging.debug('g(%s) start' % (N))
	if N == 1:
		#logging.debug('g(1) returns 1')
		return 1 # this is just the chain {1}

	totalNumberOfChains = 0
	midpointOfN = N // 2
	for i in range(midpointOfN, 0, -1):
		if N % i != 0:
			#logging.debug('i of %s skipped' % (i))
			continue

		#logging.debug('calling g(i) where i is %s' % (i))
		totalNumberOfChains += g(i)

	#logging.debug('g(%s) returns %s' % (N, totalNumberOfChains))
	return totalNumberOfChains


def calculateAnswerForProblem548():
	finalResult = 0
	for n in range(10 ** 4):
		if g(n) == n:
			finalResult += n
	print(finalResult)

#import cProfile
#cProfile.run('calculateAnswerForProblem548()')

print(g( 3**2 *  5**3 *  7**4))
print(g( 5**2 * 11**3 *  7**4))