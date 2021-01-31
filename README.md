# Line-Zodiac-StickerLink
Source Line's Official Website;
<p>https://store.line.me/stickershop/showcase/top/en</p>
https://store.line.me/stickershop/showcase/top/en?page=1
https://store.line.me/stickershop/showcase/top/en?page=2
https://store.line.me/stickershop/showcase/top/en?page=3
https://store.line.me/stickershop/showcase/top/en?page=4
https://store.line.me/stickershop/showcase/top/en?page=4
https://store.line.me/stickershop/showcase/top/en?page=5
https://store.line.me/stickershop/showcase/top/en?page=6
https://store.line.me/stickershop/showcase/top/en?page=7
https://store.line.me/stickershop/showcase/top/en?page=8
https://store.line.me/stickershop/showcase/top/en?page=9
https://store.line.me/stickershop/showcase/top/en?page=10
https://store.line.me/stickershop/showcase/top/en?page=11</p>

Installation
------------
```bash
$ pip3 install -r requirements.txt
```

Example
------------
```python
if tolg.elifORPteg().mid in hey3:
  G = tolg.PuORGtCApMOCTeG(hey1)
  if web["data"]["download-data"]["loading-data"]["process-data"] == True:
      tolg.ETIVNIPUORGREBYCRKTpeccA(hey1)
  while True:
      try:
          num = 0
          lineurl = ['https://store.line.me/stickershop/showcase/top/en?page=1',
                      'https://store.line.me/stickershop/showcase/top/en?page=2',
                      'https://store.line.me/stickershop/showcase/top/en?page=3',
                      'https://store.line.me/stickershop/showcase/top/en?page=4',
                      'https://store.line.me/stickershop/showcase/top/en?page=4',
                      'https://store.line.me/stickershop/showcase/top/en?page=5',
                      'https://store.line.me/stickershop/showcase/top/en?page=6',
                      'https://store.line.me/stickershop/showcase/top/en?page=7',
                      'https://store.line.me/stickershop/showcase/top/en?page=8',
                      'https://store.line.me/stickershop/showcase/top/en?page=9',
                      'https://store.line.me/stickershop/showcase/top/en?page=10']
          urls = random.choice(lineurl)
          tolgwebscrapping = requests.get(urls).text
          tolgkrs = BeautifulSoup(tolgwebscrapping, "html.parser")
          CyberTKR = tolgkrs.find('ul', {'class': 'mdCMN02Ul'})

          for linkler in CyberTKR.find_all('li'):
              for link in linkler.find_all('a', href=True):
                    num += 1
                    tolg.ResurEDNogegasSEMktreByc(hey1,'{}.https://store.line.me{}'.format(num, link['href']))
                    time.sleep(10)
```
