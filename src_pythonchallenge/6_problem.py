import re, zipfile

theZip = zipfile.ZipFile('c:\\Users\\Al\\Downloads\\channel.zip')

numberPattern = re.compile(r'(\d+)')
fileContentPattern = re.compile(r'Next nothing is \d+')
num = '90052'

while True:
    content = theZip.open(num + '.txt').read().decode('ascii')
    #print(num)
    #print(content)


    match = numberPattern.search(content)
    assert match is not None

    assert fileContentPattern.search(content) is not None

    #print('MATCH: ' + match.group(1))
    #print('\n\n')

    print(theZip.getinfo(num + '.txt').comment.decode('ascii'), end='')

    num = match.group(1)
