import requests
import psycopg2
from openpyxl import Workbook,load_workbook
from time import sleep

db_host = '10.98.225.186'
db_name = 'atlas_db'
db_user = 'saatcms'
db_pass = 'cms123'
port = '5000'



conn=psycopg2.connect(dbname=db_name,user=db_user,password=db_pass,host=db_host,port=port)
cur=conn.cursor()
while (True):

#    cur.execute("select status,count(*) from atlas_cms_vod.plan_profile where content_id in (select id from atlas_cms_vod.content where parent_series_id ='4165173' or id ='4165173') group by status")
    cur.execute("select content_status ,count(*) from atlas_cms_vod.content where parent_series_id ='4165173' or id ='4165173' group by content_status;")

    frsh =cur.fetchall()
    print(frsh)
    sleep(5)
