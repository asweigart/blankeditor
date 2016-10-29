import random

LETTERS = 'abcdefghijklmnopqrstuvwxyz'

class Caesar():
	def encode(self, plaintext):
		ciphertext = ''
		plaintext = plaintext.lower()

		for symbol in plaintext:
			# check if symbol is a letter
			if symbol not in LETTERS:
				continue

			# encrypt symbol
			symbolIndex = LETTERS.index(symbol)
			encryptedIndex = symbolIndex + 3
			encryptedIndex %= len(LETTERS)
			ciphertext += LETTERS[encryptedIndex]

		return ciphertext

	def decode(self, ciphertext):
		plaintext = ''
		ciphertext = ciphertext.lower()

		for symbol in ciphertext:
			# check if symbol is a letter
			if symbol not in LETTERS:
				continue

			# decrypt symbol
			symbolIndex = LETTERS.index(symbol)
			decryptedIndex = symbolIndex - 3
			decryptedIndex %= len(LETTERS)
			plaintext += LETTERS[decryptedIndex]

		return plaintext		

class Cipher():
	def __init__(self, key=''):
		if key == '':
			# generate a pseudorandom key
			for i in range(100):
				key += random.choice(LETTERS)


		if not (key.islower() and key.isalpha()):
			raise ValueError('They key must be all lowercase letters only.')

		self.key = key # e.g. 'pizza'

	def encode(self, plaintext):
		ciphertext = ''

		for index, symbol in enumerate(plaintext):
			ciphertext += self.shift_encode(symbol, index % len(self.key))

		return ciphertext

	def decode(self, ciphertext):
		plaintext = ''

		for index, symbol in enumerate(ciphertext):
			plaintext += self.shift_decode(symbol, index % len(self.key))

		return plaintext

	


	def shift_encode(self, symbol, nthSubkey):
		if symbol not in LETTERS:
			return ''

		symbolIndex = LETTERS.index(symbol)
		encryptedIndex = symbolIndex + LETTERS.index(self.key[nthSubkey])
		encryptedIndex %= len(LETTERS) # wrap around
		return LETTERS[encryptedIndex]

	def shift_decode(self, symbol, nthSubkey):
		if symbol not in LETTERS:
			return ''

		symbolIndex = LETTERS.index(symbol)
		decryptedIndex = symbolIndex - LETTERS.index(self.key[nthSubkey])
		decryptedIndex %= len(LETTERS) # wrap around
		return LETTERS[decryptedIndex]