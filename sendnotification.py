import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

COMMASPACE = ', '
gmail_user = "email"
gmail_pwd = "password"

def send_notification(emaillist, status):
    print "Sending notification!!"
    msg = MIMEMultipart()
    Subject = 'Seat Available for %s by Prof. %s' % (status[1], status[0])
    Text = 'Seat Available for %s by Prof. %s' % (status[1], status[0])
    me = "ASU Class Notifier"
    msg['From'] = me
    msg['To'] = COMMASPACE.join(emaillist)
    msg.preamble = 'Seat Available for %s by Prof. %s' % (status[1], status[0])
    msg = 'Subject: {}\n\n{}'.format(Subject, Text)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, emaillist, msg)
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()

    print emaillist
    pass