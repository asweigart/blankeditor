#! python3

import sys
print(sys.version)
import string

def is_pangram(sentence):
	sentence = sentence.lower()
	
	for letter in string.ascii_lowercase:
		if letter not in sentence:
			return False
	return True