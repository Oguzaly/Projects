import os
import smtplib
from email.message import EmailMessage
Email_user=os.environ.get('SaatBildirim@gmail.com')

password=os.environ.get('cmssaat2020')

msg = EmailMessage()
msg['Subject'] = 'Test Subject'
msg['From'] = Email_user
msg['to'] = 'Oguzhan@saatteknoloji.com'
msg.set_content('centent test')

with smtplib.SMTP('smtp.gmail.com',465) as smtp :

    smtp.login(Email_user,password)


    smtp.send_message(msg)
