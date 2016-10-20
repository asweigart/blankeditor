ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
REVERSED = 'zyxwvutsrqponmlkjihgfedcba'

def encode(plaintext):
	ciphertext = []
	plaintext = plaintext.lower()
	for symbol in plaintext:
		# handle numbers
		if symbol in '0123456789':
			ciphertext.append(symbol)
			continue

		index = ALPHABET.find(symbol)
		if index == -1:
			continue

		ciphertext.append(REVERSED[index])

	ciphertext = ''.join(ciphertext) # ciphertext is one giant string (without the spaces every 5 chars)
	ciphertextGroups = []
	for index in range(0, len(ciphertext), 5):
		ciphertextGroups.append(ciphertext[index:index+5])

	return ' '.join(ciphertextGroups)


def decode(ciphertext):
	plaintext = []
	for symbol in ciphertext:
		if symbol == ' ':
			continue
		index = REVERSED.index(symbol)

		plaintext.append(ALPHABET[index])

	return ''.join(plaintext)