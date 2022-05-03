import os
import smtplib
from email.message import EmailMessage
Email_user='SaatBildirim@gmail.com'

password='cmssaat2020'

msg = EmailMessage()
msg['Subject'] = 'Test Subject'
msg['From'] = Email_user
msg['to'] = 'Oguzhan@saatteknoloji.com'
msg.set_content('centent test')

with smtplib.SMTP('smtp.gmail.com',587) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(Email_user,password)


    smtp.send_message(msg)
