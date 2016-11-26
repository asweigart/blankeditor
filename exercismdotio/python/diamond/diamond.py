def make_diamond(maxLetter):
    # special case for 'A'
    if maxLetter == 'A':
        return 'A\n'

    wingSpaces = (ord(maxLetter) - 65) * ' '
    lines = [wingSpaces + 'A' + wingSpaces] # begins with a single 'A'
    for letterNum in range(66, ord(maxLetter) + 1):
        wingSpaces = (ord(maxLetter) - letterNum) * ' '
        inBetweenSpaces = (1 + (letterNum - 66) * 2) * ' '
        lines.append(wingSpaces + chr(letterNum) + inBetweenSpaces + chr(letterNum) + wingSpaces)

    for letterNum in range(ord(maxLetter) - 1, 65, -1):
        wingSpaces = (ord(maxLetter) - letterNum) * ' '
        inBetweenSpaces = (1 + (letterNum - 66) * 2) * ' '
        lines.append(wingSpaces + chr(letterNum) + inBetweenSpaces + chr(letterNum) + wingSpaces)

    wingSpaces = (ord(maxLetter) - 65) * ' '
    lines.append(wingSpaces + 'A' + wingSpaces) # ends with a single 'A'

    return '\n'.join(lines) + '\n'

