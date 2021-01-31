# Line-Zodiac-StickerLink
Source Line's Official Website;
<p align="justify">
https://store.line.me/stickershop/showcase/top/en<br>
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
# Line-Zodiac-StickerLink
Source Zodiac's Official Website;
<p>https://www.gunlukburc.net/gunluk-burc-yorumlari/koc.html
https://www.gunlukburc.net/gunluk-burc-yorumlari/ikizler.html
https://www.gunlukburc.net/gunluk-burc-yorumlari/boga.html
https://www.gunlukburc.net/gunluk-burc-yorumlari/yengec.html
https://www.gunlukburc.net/gunluk-burc-yorumlari/terazi.html
https://www.gunlukburc.net/gunluk-burc-yorumlari/akrep.html
https://www.gunlukburc.net/gunluk-burc-yorumlari/oglak.html
https://www.gunlukburc.net/gunluk-burc-yorumlari/yay.html
https://www.gunlukburc.net/gunluk-burc-yorumlari/balık.html
https://www.gunlukburc.net/gunluk-burc-yorumlari/basak.html
https://www.gunlukburc.net/gunluk-burc-yorumlari/aslan.html</p>

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
          burcurl = ['https://www.gunlukburc.net/gunluk-burc-yorumlari/koc.html',
                      'https://www.gunlukburc.net/gunluk-burc-yorumlari/ikizler.html',
                      'https://www.gunlukburc.net/gunluk-burc-yorumlari/boga.html',
                      'https://www.gunlukburc.net/gunluk-burc-yorumlari/yengec.html',
                      'https://www.gunlukburc.net/gunluk-burc-yorumlari/terazi.html',
                      'https://www.gunlukburc.net/gunluk-burc-yorumlari/akrep.html',
                      'https://www.gunlukburc.net/gunluk-burc-yorumlari/oglak.html',
                      'https://www.gunlukburc.net/gunluk-burc-yorumlari/yay.html',
                      'https://www.gunlukburc.net/gunluk-burc-yorumlari/balık.html',
                      'https://www.gunlukburc.net/gunluk-burc-yorumlari/basak.html',
                      'https://www.gunlukburc.net/gunluk-burc-yorumlari/aslan.html']
          urls = random.choice(burcurl)
          request = requests.get(urls).text

          soup = BeautifulSoup(request,'html.parser')
          for ret in soup.find_all('h3', attrs={'class': 'd-block'}):
              tolg.ResurEDNogegasSEMktreByc(hey1,"Günlük burç Yorumları, Sırasıyla: \n\n{}".format(ret.find_next('p').text))
      except:
          pass
```
