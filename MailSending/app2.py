import psycopg2
import smtplib
from email.message import EmailMessage


Email_user='oguzhan@saatteknoloji.com'
password='Oo1+1993'



    # yaz = 'Aşağıdaki Sezonlarda altında published episode yok \n\n'+'guid'+'         '+'Name\n'+str(i[0])+' '+str(i[1])
yaz = 'Test İçin Atılmıştır '
msg = EmailMessage()
msg['Subject'] = 'Altı Boş Sezonlar'
msg['From'] = Email_user
msg['to'] = 'Oguzhan@saatteknoloji.com','mahmutttttttt.deneme@gmail.com'
msg.set_content(str(yaz))

csvfiles = ['C:/Users/HP/Desktop/playground/EpgConflict/Conflict.csv']

for file in csvfiles:

    with open(file, 'rb') as f:
        file_data = f.read()
        # file_type = imghdr.what(f.name)
        file_name = 'Conflict.csv'

    msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)


with smtplib.SMTP('smtp.office365.com',587) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(Email_user,password)


    smtp.send_message(msg)
