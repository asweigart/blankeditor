# string building with a string (bad)
spam = 'hello world'
uppercaseVersion = ''

for letter in spam:
	uppercaseVersion += letter.upper()

print(uppercaseVersion)



# string building with a list (good)
spam = 'hello world'
uppercaseVersion = []
for letter in spam:
	#uppercaseVersion.append(letter.upper())
	uppercaseVersion += letter.upper()

print(''.join(uppercaseVersion))
