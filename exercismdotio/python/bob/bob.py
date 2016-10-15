#
# Skeleton file for the Python "Bob" exercise.
#


def hey(what):
	what = what.strip()
	if what == '':
		return 'Fine. Be that way!'		
	elif what == what.upper() and any([character.isalpha() for character in what]):
		return 'Whoa, chill out!'
	elif what.endswith('?'):
		return 'Sure.'
	else:
		return 'Whatever.'
