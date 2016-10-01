import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)

def isAnagram(string1, string2):
	# Returns True if `string1` and `string2` are anagrams; otherwise returns False
	# We are ignoring case and whitespace
	string1 = string1.lower()
	string2 = string2.lower()
	letterCount1 = {}
	letterCount2 = {}

	for letter in string1:
		if letter.isalpha():
			# add `letter` to `letterCount` dictionary
			letterCount1.setdefault(letter, 0)
			letterCount1[letter] += 1
	logging.debug(letterCount1)

	for letter in string2:
		if letter.isalpha():
			# add `letter` to `letterCount` dictionary
			letterCount2.setdefault(letter, 0)
			letterCount2[letter] += 1
	logging.debug(letterCount2)

	return letterCount1 == letterCount2





print('Clint Eastwood and Old West Action:')
print(isAnagram('Clint Eastwood', 'Old West Action'))
print()

print('Astronomers and Moon starer:')
print(isAnagram('Astronomers', 'Moon starer'))
print()

print('Vacation Times and I\'m Not as Active')
print(isAnagram('Vacation Times', "I'm Not as Active"))