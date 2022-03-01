from openpyxl import Workbook,load_workbook
import psycopg2
import xlsxwriter
import requests

#Prod
#
# db_host = '10.98.225.186'
# db_name = 'atlas_db'
# db_user = 'saatcms'
# db_pass = 'cms123'
# port = '5000'
#

#Staging

db_host = '10.98.228.149'
db_name = 'atlas_db'
db_user = 'saatcms'
db_pass = 'cms123'
port = '5000'

conn=psycopg2.connect(dbname=db_name,user=db_user,password=db_pass,host=db_host,port=port)
cur=conn.cursor()

cur.execute("select *from atlas_cms_vod.plan_profile where content_id in (select id  from atlas_cms_vod.content where type='SEASON' and content_status='Published' and id not in (select distinct parent_id from atlas_cms_vod.content where parent_id in (select id from atlas_cms_vod.content where type='SEASON' and content_status='Published' )and type='EPISODE' and content_status='Published'order by parent_id ))")
frsh =cur.fetchall()

#http://10.98.225.178:8090/     :   Prod
#http://10.98.228.146:8090/     :   Stanging

for i in frsh:
    #print(i[0])
    url="http://10.98.228.146:8090/planprofiles/"+'{}'.format(i[0])+"/deactivate"
    #print(url)

    headers = {}
    payload = {}

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

    print("                 ")
