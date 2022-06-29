import psycopg2
import smtplib
from email.message import EmailMessage
from pandas import DataFrame
import pandas as pd
from tabulate import tabulate

Email_user='oguzhan@saatteknoloji.com'
password='Oo1+1993'

#Prod

db_host = '10.98.225.186'
db_name = 'atlas_db'
db_user = 'saatcms'
db_pass = 'cms123'
port = '5000'


#Staging
# #
# db_host = '10.98.228.149'
# db_name = 'atlas_db'
# db_user = 'saatcms'
# db_pass = 'cms123'
# port = '5000'

conn=psycopg2.connect(dbname=db_name,user=db_user,password=db_pass,host=db_host,port=port)
cur=conn.cursor()

cur.execute("select id ,guid,name  from atlas_cms_vod.content where type='SEASON' and content_status='Published' and id not in (select distinct parent_id from atlas_cms_vod.content where parent_id in (select id from atlas_cms_vod.content where type='SEASON' and content_status='Published' )and type='EPISODE' and content_status='Published'order by parent_id)")
frsh =cur.fetchall()
# df=pd.read_sql(sql,conn)
df1 = pd.DataFrame(frsh,columns=['                     id','                          guid','                                   name']) #Pandas ile sql sonucu daha anlaşılır okunabilir

df= tabulate(df1, showindex=False, headers=df1.columns) # gelen sonuçları hizalamak için kullanıldı.



#
# for i in frsh:
#     print(i[0],i[1])
#
#     yaz = 'Aşağıdaki Sezonlarda altında published episode yok \n\n'+'guid'+'         '+'Name\n'+str(i[0])+' '+str(i[1])
#
#
yaz = 'Aşağıdaki Sezonlarda altında published episode yok (id,name,guid) \n\n'+str(df) +'\n\n' + 'Test İçin Atılmıştır '
msg = EmailMessage()
msg['Subject'] = 'Altı Boş Sezonlar'
msg['From'] = Email_user
msg['to'] = 'Oguzhan@saatteknoloji.com'
msg.set_content(str(yaz))

with smtplib.SMTP('smtp.office365.com',587) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(Email_user,password)


    smtp.send_message(msg)


conn.close()
