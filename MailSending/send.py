import psycopg2
import smtplib
from email.message import EmailMessage
from pandas import DataFrame
import pandas as pd
from tabulate import tabulate

Email_user='Mail'
password='Şifre'

#Staging
# #
# db_host = '10.98.228.149'
# db_name = 'atlas_db'
# db_user = 'saatcms'
# db_pass = 'cms123'
# port = '5000'

conn=psycopg2.connect(dbname=db_name,user=db_user,password=db_pass,host=db_host,port=port)
cur=conn.cursor()

cur.execute("select type,operation, status,count(*) from atlas_mw_connector.ingest_job where to_timestamp(creation_date/1000)::timestamp>current_date::timestamp group by type,operation,status")
frsh =cur.fetchall()
# df=pd.read_sql(sql,conn)
df1 = pd.DataFrame(frsh,columns=['type','operation','status','count']) #Pandas ile sql sonucu daha anlaşılır okunabilir

df= tabulate(df1, showindex=False, headers=df1.columns,tablefmt="rst") # gelen sonuçları hizalamak için kullanıldı.


# numalign="right",stralign="left"
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
