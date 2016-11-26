urls = '''map
lzo
kyn
jxm
iwl
hvk
guj
fti
esh
drg
cqf
bpe
aod
znc
ymb
xla
wkz
vjy
uix
thw
sgv
rfu
qet
pds
ocr
nbq'''.split('\n')

import requests

for url_suffix in urls:
    res = requests.get('http://www.pythonchallenge.com/pc/def/' + url_suffix + '.html')
    print(res.status_code)