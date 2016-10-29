import doctest


def translate(sentence):
    # break up `sentence` into individual words
    words = sentence.split()
    results = []

    for word in words:
        results.append(pigLatinWord(word))

    return ' '.join(results)


def pigLatinWord(normalWord):
    '''
    >>> pigLatinWord('apple')
    'appleay'
    >>> pigLatinWord('hello')
    'ellohay'
    '''
    # on each word, test if it begins wiht a vowel or consonent
    if normalWord[0] == 'a' or \
       normalWord[0] == 'e' or \
       normalWord[0] == 'i' or \
       normalWord[0] == 'o' or \
       normalWord[0] == 'u' or \
       normalWord[0:2] == 'xr' or \
       normalWord[0:2] == 'yt':
        # if it begins with a vowel, add 'ay'
        return normalWord + 'ay'

    else:
        if normalWord.startswith('qu'):
            return normalWord[2:] + 'quay'
        elif normalWord.startswith('ch'):
            return normalWord[2:] + 'chay'
        elif normalWord.startswith('sch'):
            return normalWord[3:] + 'schay'
        elif normalWord.startswith('squ'):
            return normalWord[3:] + 'squay'
        elif normalWord.startswith('thr'):
            return normalWord[3:] + 'thray'
        elif normalWord.startswith('th'):
            return normalWord[2:] + 'thay'
        else:
            # if it begins with a consonent, move first letter to end and add 'ay'
            return normalWord[1:] + normalWord[0] + 'ay'

doctest.testmod()