import psycopg2
from openpyxl import load_workbook,Workbook


db_host = '****'
db_name = '****'
db_user = '****'
db_pass = '****'
port = '****'
conn=psycopg2.connect(dbname=db_name,user=db_user,password=db_pass,host=db_host,port=port)
cur=conn.cursor()
cur1= conn.cursor()
cur.execute("select child_count from atlas_cms_vod.content where type='SEASON' and content_status = 'Published' limit 10")
cur1.execute("select parent_id ,count(*) from atlas_cms_vod.content where parent_id in(select id from atlas_cms_vod.content where type='SEASON' and content_status = 'Published' limit 10)and content_status ='Published'group by parent_id")
frsh=cur.fetchall()
frsh2=cur1.fetchall()
for i in range(1,10):
    print (frsh[i][0])
    print (frsh2[0][i])
