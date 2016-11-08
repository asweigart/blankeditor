def song(startVerse, stopVerse=0):
    verses = []
    for verseNumber in range(startVerse, stopVerse - 1, -1):
        verses.append(verse(verseNumber) + '\n')
    return ''.join(verses)

def verse(verseNumber):
    if verseNumber == 0:
        return ("No more bottles of beer on the wall, no more bottles of beer.\n" 
            "Go to the store and buy some more, " 
            "99 bottles of beer on the wall.\n")
    elif verseNumber == 1:
        return ("1 bottle of beer on the wall, 1 bottle of beer.\n" 
            "Take it down and pass it around, " 
            "no more bottles of beer on the wall.\n")
    elif verseNumber == 2:
        return ("2 bottles of beer on the wall, 2 bottles of beer.\n"
            "Take one down and pass it around, "
            "1 bottle of beer on the wall.\n")
    else:
        return ("%s bottles of beer on the wall, %s bottles of beer.\n"
            "Take one down and pass it around, "
            "%s bottles of beer on the wall.\n" % (verseNumber, verseNumber, verseNumber - 1))

