from openpyxl import Workbook,load_workbook
import requests
import json


wp=load_workbook('C:/Users/HP/Desktop/playground/CreateContent/temp/createvod.xlsx')
ws=wp.active




def CreateContent():

    for i in range(1,10) :

        #
        # cdrId= ws['A{}'.format(i)].value
        name = ws['A{}'.format(i)].value
        # year = ws['C{}'.format(i)].value
        #
        print(name)
      #  print(i)
        url = "http://10.98.228.146:8090/contents"
        payload = json.dumps({
          "contentType": "Film",
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
