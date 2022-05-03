from smtplib import SMTP
try:
    # Mail mesaj bilgileri
    subcject = "TEST OLARAK GÖNDERİLEN MAİL"
    message  = "Bu bir test mesajıdır dikkate almayın"
    content  = "Subject: {0}\n\n{1}".format(subcject,message)

    # hesap bilgileri
    mymailAdress= "saatbildirim@gmail.com"
    password= "cmssaat2020"
    To=['oguzhan@saatteknoloji.com'] # burda ikisinin arasına koyman gerekiyor.
    # kime gönderilecek bilgisi
    sendTo = ['esatvural06@gmail.com','esatvural1997@gmail.com']
    mail = SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login(mymailAdress,password)
    mail.sendmail(mymailAdress,sendTo,content.encode("utf-8"))## (utf-8 kodu dopru çalışması için) 
    print("mail gönderildi")
except Exception as e:
    print("Hata oluştu!\n{0}".format(e))
