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
cur1=conn.cursor()
cur2=conn.cursor()
cur3=conn.cursor()
cur.execute("select count(*),type,operation, status from atlas_mw_connector.ingest_job where to_timestamp(creation_date/1000)::timestamp>current_date::timestamp group by type,operation,status")
frsh =cur.fetchall()
cur1.execute("select count(*),content_status from atlas_cms_vod.content group by content_status")
frsh1=cur1.fetchall()
cur2.execute("select count(*),status from atlas_cms_vod.catchup group by status")
frsh2=cur2.fetchall()
cur3.execute("select count(*),release_date,ingested from atlas_cms_btv.program where  release_date>current_date::date-6 group by ingested,release_date")
frsh3=cur3.fetchall()
# df=pd.read_sql(sql,conn)
df1 = pd.DataFrame(frsh,columns=['count','type','operation','status']) #Pandas ile sql sonucu daha anlaşılır okunabilir
dfa= tabulate(df1,showindex=False, headers=df1.columns,tablefmt="pretty",colalign=("left","left","left","left")) # gelen sonuçları hizalamak için kullanıldı
df2=pd.DataFrame(frsh1,columns=['Count','content_status'])
dfb=tabulate(df2,showindex=False, headers=df2.columns,tablefmt="pretty",colalign=("left","left"))
df3=pd.DataFrame(frsh2,columns=['Count','status'])
dfc=tabulate(df3,showindex=False, headers=df3.columns,tablefmt="pretty",colalign=("left","left"))
df4=pd.DataFrame(frsh3,columns=['Count','release_date','ingest durumu'])
dfd=tabulate(df4,showindex=False, headers=df4.columns,tablefmt="pretty",colalign=("left","left","left"))
# numalign="right",stralign="left"
#
# for i in frsh:
#     print(i[0],i[1])
#
#     yaz = 'Aşağıdaki Sezonlarda altında published episode yok \n\n'+'guid'+'         '+'Name\n'+str(i[0])+' '+str(i[1])

yaz = 'Günlük Gönderilen Xmllerin Durumu \n\n'+str(dfa) +'\n\n' +'Vod Ingestleri'+'\n\n'+str(dfb)+'\n\n'+ 'Cutv Ingestleri' +'\n\n'+ str(dfc) +'\n\n'+'14 günlük Epg Ingest durumları' +'\n\n'+ str(dfd)
msg = EmailMessage()
msg['Subject'] = 'Altı Boş Sezonlar'
msg['From'] = Email_user
msg['to'] = 'Oguzhan@saatteknoloji.com','mustafakemal@saatteknoloji.com','berivan@saatteknoloji.com','hakan@saatteknoloji.com','esat@saatteknoloji.com'
msg.set_content(str(yaz))
with smtplib.SMTP('smtp.office365.com',587) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(Email_user,password)
    smtp.send_message(msg)
conn.close()
