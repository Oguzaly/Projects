import psycopg2
import smtplib
from email.message import EmailMessage


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

cur.execute("select id,name,guid from atlas_cms_vod.content where content_status in ('ReadyForIngest','OngoingIngest')")
frsh =cur.fetchall()

# for i in frsh:
#     print(i[0],i[1])

    # yaz = 'Aşağıdaki Sezonlarda altında published episode yok \n\n'+'guid'+'         '+'Name\n'+str(i[0])+' '+str(i[1])
yaz = 'Aşağıdaki içerikler ReadyForIngest de ve OngoingIngest da takılmış içerikleri gözlemlemekteyiz. (id,name,guid) \n\n'+str(frsh)
msg = EmailMessage()
msg['Subject'] = 'ReadyForIngest ve OngoingIngest de takılan içerikler'
msg['From'] = Email_user
msg['to'] = 'cansu.cetinkaya@turktelekom.com.tr','Oguzhan@saatteknoloji.com','mustafakemal@saatteknoloji.com','berkan@saatteknoloji.com','berivan@saatteknoloji.com','esat@saatteknoloji.com','hakan@saatteknoloji.com'
msg.set_content(str(yaz))

with smtplib.SMTP('smtp.office365.com',587) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(Email_user,password)


    smtp.send_message(msg)
