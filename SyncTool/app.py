import requests
from openpyxl import Workbook,load_workbook
import psycopg2

db_host = '10.98.225.186'
db_name = 'atlas_db'
db_user = 'saatcms'
db_pass = 'cms123'
port = '5000'
conn=psycopg2.connect(dbname=db_name,user=db_user,password=db_pass,host=db_host,port=port)
cur=conn.cursor()
cur.execute("select guid,content_status from atlas_cms_vod.content where type='MOVIE' and (not content_status='NoActiveLicense')")
frsh =cur.fetchall()
with open('C:/Users/HP/Desktop/playground/SyncTool/status.csv','a') as f:
    for i in frsh:
        url = "http://10.98.225.184:8084/mw/api/getcontentinfo?id="+'{}'.format(i)+"&type=1"
        payload={}
        headers = {}
        response = requests.request("GET", url, headers=headers, data=payload)
        print(response.text)
        type=str(i[0])+','+str(i[1])+','+ response.text
        f.write(type+'\n')
