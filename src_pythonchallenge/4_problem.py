import requests, re

fiveDigitsPattern = re.compile('(\d+)')
code = '63579' # first page was '12345'

while True:
    print('Downloading: ' + code)
    res = requests.get('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=' + code)
    assert res.status_code == 200 # check that the webpage loaded without error

    print(res.text)
    print('\n\n')
    code = fiveDigitsPattern.search(res.text).group(1)
