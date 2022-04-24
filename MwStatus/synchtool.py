import requests
import psycopg2



db_host = '10.98.225.186'
db_name = 'atlas_db'
db_user = 'saatcms'
db_pass = 'cms123'
port = '5000'



conn=psycopg2.connect(dbname=db_name,user=db_user,password=db_pass,host=db_host,port=port)
cur=conn.cursor()

cur.execute("select guid,type from atlas_cms_vod.content where type='EPISODE' or type='MOVIE' limit 10")
frsh =cur.fetchall()
for i in frsh:
    print(i[0])


    with open('C:/Users/HP/Desktop/içerik.csv','a') as f:

        if i[1] == 'EPISODE':
            row=('{}'.format(i[0])+','+'2')
            f.write(row+'\n')

        else :
            row=('{}'.format(i[0])+','+'1')
            f.write(row+'\n')






# url = "http://10.98.225.184:8084/mw/api/getcontentinfo?id=000621859&type=1"
#
# payload={}
# headers = {}
#
# response = requests.request("GET", url, headers=headers, data=payload)
#
# print(response.text)
