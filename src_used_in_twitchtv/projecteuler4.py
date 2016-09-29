import logging

logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

def isPalindrome(number):
	logging.debug('start of isPalindrome(%s)' % number)
	numberAsList = list(str(number))
	logging.debug('numberAsList == %s' % (numberAsList))
	reversedNumberList = list(reversed(numberAsList))
	logging.debug('reversedNumberList == %s' % (reversedNumberList))
	reversedString = ''.join(reversedNumberList)
	logging.debug(reversedString)

	return number == int(reversedString)

# finding all products of 3-digit numbers


logging.debug('12345: %s ' % (isPalindrome(12345)))
logging.debug('9009: %s ' % (isPalindrome(9009)))

def printLargestPalindromicNumber():
	largestPalindromicNumber = 0
	for number1 in range(999, 99, -1):
		for number2 in range(999, 99, -1):
			if isPalindrome(number1 * number2) and (number1 * number2) > largestPalindromicNumber:
				largestPalindromicNumber = number1 * number2
	print(largestPalindromicNumber)


	
printLargestPalindromicNumber()
