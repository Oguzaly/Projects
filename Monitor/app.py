import requests
import psycopg2
from openpyxl import Workbook,load_workbook
from time import sleep
import os

db_host = '10.98.225.186'
db_name = 'atlas_db'
db_user = 'saatcms'
db_pass = 'cms123'
port = '5000'



conn=psycopg2.connect(dbname=db_name,user=db_user,password=db_pass,host=db_host,port=port)
# conn1=psycopg2.connect(dbname=db_name,user=db_user,password=db_pass,host=db_host,port=port)

cur=conn.cursor()
cur1=conn.cursor()

parent_series_id =4167561,4165271,4164891,4164913,4164775,4164565,4164651,4164592

while (True):

#    cur.execute("select status,count(*) from atlas_cms_vod.plan_profile where content_id in (select id from atlas_cms_vod.content where parent_series_id ='4165173' or id ='4165173') group by status")
    cur.execute("select content_status,count(*) from atlas_cms_vod.content where parent_series_id in ("+'{}'+")group by content_status").format(str(parent_series_id))
    cur1.execute("select id,name  from atlas_cms_vod.content where parent_series_id in ("+'{}'+") and content_status ='IngestFailed'").format(str(parent_series_id))

    frsh =cur.fetchall()
    frsh1 =cur1.fetchone()

    print(frsh)
    print('-------------------------------------------------------------------------------------------------')
    while frsh1:
        frsh1 =cur1.fetchone()
        print(frsh1)

    sleep(5)
    os.system('cls')
