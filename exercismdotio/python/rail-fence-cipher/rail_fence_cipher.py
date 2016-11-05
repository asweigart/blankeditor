import logging
logging.basicConfig(level=logging.DEBUG)
logging.disable(logging.CRITICAL)


def encode(plaintext, key):
	return ''.join(makeRails(plaintext, key))


def makeRails(text, key):
	rails = [''] * key
	railsIndex = 0
	goingDown = True
	
	for textSymbol in text:
		rails[railsIndex] += textSymbol

		if goingDown:
			railsIndex += 1
			if railsIndex == len(rails):
				goingDown = False
				railsIndex -= 2
		else:
			railsIndex -= 1
			if railsIndex == -1:
				goingDown = True
				railsIndex += 2
	return rails


def decode(ciphertext, key):
	# get the length of each rail
	railSizes = makeRails(ciphertext, key)
	logging.debug(railSizes)

	# replace string (which we don't care about) with the length of the string (which we do care about)
	for index in range(len(railSizes)):
		railSizes[index] = len(railSizes[index])

	logging.debug(railSizes)

	# lay out the ciphertext along the rails
	rails = []
	startIndex = 0
	for k in range(key):
		rails.append(ciphertext[startIndex:startIndex + railSizes[k]])
		startIndex += railSizes[k]

	logging.debug(rails)


	# move up and down along the rails to get the plaintext
	plaintext = ''
	railsIndex = 0
	goingDown = True
	
	while ''.join(rails) != '':
		# add first letter from the rail string to the final plaintext
		plaintext += rails[railsIndex][0]
		rails[railsIndex] = rails[railsIndex][1:]

		# move railsIndex either up or down
		if goingDown:
			railsIndex += 1
			if railsIndex == len(rails):
				railsIndex -= 2
				goingDown = False
		else:
			railsIndex -= 1
			if railsIndex == -1:
				railsIndex += 2
				goingDown = True

	return plaintext