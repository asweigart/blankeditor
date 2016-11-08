def intro(verseNumber):
	ordinals = {1: 'first',
				2: 'second',
				3: 'third',
				4: 'fourth',
				5: 'fifth',
				6: 'sixth',
				7: 'seventh',
				8: 'eighth',
				9: 'ninth',
				10: 'tenth',
				11: 'eleventh',
				12: 'twelfth'}
	return 'On the %s day of Christmas my true love gave to me, ' % (ordinals[verseNumber])

def verse(verseNumber):
	verseMapping = {1: 'a Partridge in a Pear Tree.\n',
					2: 'two Turtle Doves, ',
					3: 'three French Hens, ',
					4: 'four Calling Birds, ',
					5: 'five Gold Rings, ',
					6: 'six Geese-a-Laying, ',
					7: 'seven Swans-a-Swimming, ',
					8: 'eight Maids-a-Milking, ',
					9: 'nine Ladies Dancing, ',
					10: 'ten Lords-a-Leaping, ',
					11: 'eleven Pipers Piping, ',
					12: 'twelve Drummers Drumming, '}
	lyrics = [intro(verseNumber)]

	if verseNumber == 1:
		lyrics.append(verseMapping[1])
		return ''.join(lyrics)

	for eachVerseNum  in range(verseNumber, 1, -1):
		lyrics.append(verseMapping[eachVerseNum])
	lyrics.append('and ' + verseMapping[1])

	return ''.join(lyrics)


def verses(startVerse, stopVerse):
	lyrics = []
	for eachVerse in range(startVerse, stopVerse + 1):
		lyrics.append(verse(eachVerse) + '\n')

	return ''.join(lyrics)

def sing():
	return verses(1, 12)