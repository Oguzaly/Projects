import requests
import json
import psycopg2

db_host = '10.98.225.186'
db_name = 'atlas_db'
db_user = 'saatcms'
db_pass = 'cms123'
port = '5000'



conn=psycopg2.connect(dbname=db_name,user=db_user,password=db_pass,host=db_host,port=port)
cur=conn.cursor()

cur.execute('select *from atlas_cms_vod.content ')

# url = ""
#
# payload = json.dumps({
#   "contentType": "Film",
#   "metadata": {
#     "videoFormats": [
#       "HD"
#     ],
#     "year": 2022
#   },
#   "name": "Test - TestContent",
#   "type": "MOVIE"
# })
# headers = {
#   'Content-Type': 'application/json'
# }

# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)
#
# parsejson =json.loads(payload)
# print(parsejson)
# print('########################3')
# print(parsejson["name"])
# print('########################3')
#
# parsejson["name"] ='Testooo'
#
# print('########################3')
# print(parsejson["name"])
# print(parsejson)
