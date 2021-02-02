from linepy import *
from bs4 import BeautifulSoup
import requests
import traceback
import random , re
from urllib.request import urlopen

#=====================================================================
tolg = LINE("EMAIL","PASSWORD",appName="DESKTOPMAC\t6.5.2\tMac OS X\t10.16.5")

poll = OEPoll(tolg)

web = {
    'data': { 
        'download-data': { 
          'loading-data': { 
            'process-data': True,
        }
      }
   }
}

def tratSnoitarepo(laylay):
    try:
        # LEAVE ROOM
        if laylay.type in [22,24]:
              tolg.leaveRoom(laylay.param1)
        # LEAVE ROOM
        
        
        # Just invite to group for sticker link
        if laylay.type == 13 or laylay.type == 124:
            hey1 = laylay.param1
            hey2 = laylay.param2
            hey3 = laylay.param3
            if tolg.elifORPteg().mid in hey3:
              G = tolg.PuORGtCApMOCTeG(hey1)
              if web["data"]["download-data"]["loading-data"]["process-data"] == True:
                  tolg.ETIVNIPUORGREBYCRKTpeccA(hey1)
              while True:
                  try:
                      num = 0
                      lineurl = ['https://store.line.me/stickershop/showcase/top_creators/en?page=1',
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
                  except:
                      pass
    except Exception as error:
        print(error)
        traceback.print_tb(error.__traceback__)

def tolgstickeruns():
    while True:
        try:
            ops = poll.singleTrace(count=1)
            if ops != None:
                for laylay in ops:
                    tratSnoitarepo(laylay)
                    poll.setRevision(laylay.revision)
        except Exception as e:
            print(e)

if __name__ == "__main__":
    tolgstickeruns()
