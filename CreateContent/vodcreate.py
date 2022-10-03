from openpyxl import Workbook,load_workbook
import requests
import json
import random
import pprint

class namegenerate:
    # Aynı ismin birden fazla kullanılmasına izin verilmediği zaman bu kullanılabilir
    def __init__(self):
            name_length = 32
            characters ='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
            name =""
            for index in range(name_length):
                name  = name + random.choice(characters)
            self.name = 'Test - ' + name

def CreateContent():
    isim1=namegenerate()
    url = "http://10.98.228.146:8090/contents"
    payload = json.dumps({
      +{}.format("contentType:" isim1.name)+
      "metadata": {
        "videoFormats": [
          "HD"
        ],
        "year": 2022
      },
      "name": "Test - TestContent",
      "type": "MOVIE"
    })
    headers = {
      'Content-Type': 'application/json'
    }
    parsejson = json.loads(payload)
    parsejson["name"] = '{}'.format(name)
    print(parsejson)
    gonder = json.dumps(parsejson)
    response = requests.request("POST", url, headers=headers, data=gonder)
    print(response.text)
    print('#########################################################################')
    print('################ Yeni İçerikler Oluşturuldu #############################')
    print('#########################################################################')

CreateContent()
