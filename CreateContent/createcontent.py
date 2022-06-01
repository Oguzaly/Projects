from openpyxl import Workbook,load_workbook
import requests
wp=load_workbook('C:/Users/HP/Desktop/playground/CreateContent/createvod.xlsx')
ws=wp.active

for i in range(1,10) :
    name = ws['A{}'.format(i)].value

    url = "http://10.98.228.146:8090/contents"

    payload = "{\r\n    \"contentType\": \"Film\",\r\n    \"metadata\": {\r\n        \"videoFormats\": [\r\n            \"HD\"\r\n        ],\r\n        \"year\": 2022\r\n    },\r\n    \"name\": \""+'{}'.format(name)+"\",\r\n    \"type\": \"MOVIE\"\r\n}"
    headers = {
      'Content-Type': 'text/plain'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)
