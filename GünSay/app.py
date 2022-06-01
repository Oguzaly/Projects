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






cur.execute("select distinct c.id,c.guid,c.name,pp.end_time as planendtime,l.end_time as lisansendtime from atlas_cms_vod.plan_profile pp left join atlas_cms_vod.license l on pp.license_id = l.id left join atlas_cms_vod.content c on c.id =pp.content_id where to_timestamp(pp.end_time/1000)::date > to_timestamp(l.end_time/1000)::date and not( c.content_status ='NoActiveLicense' )")

frsh =cur.fetchall()
print (len(frsh))

with open ('C:/Users/HP/Desktop/playground/GünSay/resut.csv','a') as f:

    for i in range(0,len(frsh)):

        if (frsh[i][4] == frsh[i][3]- 86340000) :

            #type= (frsh[i][2],'1 gün fark var')
            print('{}'.format(frsh[i][0])+','+'{}'.format(frsh[i][2]))
            f.write('{}'.format(frsh[i][0])+','+'{}'.format(frsh[i][2])+'\n')

        else :

            print('Konudışı')
