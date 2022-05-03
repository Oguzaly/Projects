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

cur.execute("select guid,type from atlas_cms_vod.content where (type='EPISODE' or type='MOVIE') and content_status='Published'")
frsh =cur.fetchall()
for i in frsh:
    print(i[0])


    with open('C:/Users/HP/Desktop/playground/MwStatus/içerik.csv','a') as f:

        if i[1] == 'EPISODE':
            row=('{}'.format(i[0])+','+'2')
            f.write(row.text +'\n')

        else :
            row=('{}'.format(i[0])+','+'1')
            f.write(row.text +'\n')


#
# wp = load_workbook('C:/Users/HP/Desktop/playground/MwStatus/içerik.csv')
# ws = wp.active
#
#
# for i in range(1,35):
#
#     print(i.value)

# url = "http://10.98.225.184:8084/mw/api/getcontentinfo?id=000621859&type=1"
#
# payload={}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)
