import logging
logging.basicConfig(level=logging.DEBUG)
#logging.disable(logging.CRITICAL)

def getLetterCount(stringInQuestion):
	letterCount = {}

	for letter in stringInQuestion:
		if letter.isalpha():
			# add `letter` to `letterCount` dictionary
			letterCount.setdefault(letter, 0)
			letterCount[letter] += 1
	logging.debug(letterCount)	

	return letterCount

def isAnagram(string1, string2):
	# Returns True if `string1` and `string2` are anagrams; otherwise returns False
	# We are ignoring case and whitespace

	string1 = string1.lower()
	string2 = string2.lower()

	return getLetterCount(string1) == getLetterCount(string2)





print('Clint Eastwood and Old West Action:')
print(isAnagram('Clint Eastwood', 'Old West Action'))
print()

print('Astronomers and Moon starer:')
print(isAnagram('Astronomers', 'Moon starer'))
print()

print('Vacation Times and I\'m Not as Active')
print(isAnagram('Vacation Times', "I'm Not as Active"))