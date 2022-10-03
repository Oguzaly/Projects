import requests
import psycopg2
from openpyxl import Workbook,load_workbook

db_host = '10.98.225.186'
db_name = 'atlas_db'
db_user = 'saatcms'
db_pass = 'cms123'
port = '5000'

conn=psycopg2.connect(dbname=db_name,user=db_user,password=db_pass,host=db_host,port=port)
cur=conn.cursor()

cur.execute("select c.guid,c.type,c.name  from atlas_cms_vod.content c left join atlas_cms_vod.content_licence cl on cl.cnt_id = c.id left join atlas_cms_vod.license l on l.id =cl.lc_id where to_timestamp(end_time/1000)::date >'2022-06-01' and c.content_status='NoActiveLicense'")
frsh =cur.fetchall()
for i in frsh:
    print(i[0])

    with open('C:/Users/HP/Desktop/playground/MwStatus/içerik.csv','a') as f:

        if i[1] == 'EPISODE':
            url = "http://10.98.225.184:8084/mw/api/getcontentinfo?id="+'{}'.format(i[0])+"&type=2"
            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            print(response.text)
            row=('{}'.format(i[0])+','+'2'+','+response.text)
            f.write(row +'\n')
        else :
            url = "http://10.98.225.184:8084/mw/api/getcontentinfo?id="+'{}'.format(i[0])+"&type=1"
            payload={}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            print(response.text)
            row=('{}'.format(i[0])+','+'1')
            f.write(row +'\n'+','+response.text)
