import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

COMMASPACE = ', '
gmail_user = "email_id"
gmail_pwd = "password"

def send_notification(emaillist, status, term, course_name, course_id):
    print "Sending notification!!"
    msg = MIMEMultipart()
    Subject = 'Seat Available for %s by Prof. %s' % (status[1], status[0])

    Text = "Hi, \n"
    Text += "\nProf. %s has %s seats available in his %s class!! \n" % (status[0], status[2], course_name)
    Text += "Use to following url to register for the class:\n"
    Text += "https://webapp4.asu.edu/catalog/classlist?k=%s&t=%s&e=open&hon=F\n"% (course_id, term)
    Text += '\nBest, \nASU Class Notifier'
    me = "ASU Class Notifier"
    msg['From'] = me
    msg['To'] = COMMASPACE.join(emaillist)
    msg = 'Subject: {}\n\n{}'.format(Subject, Text)

    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmail_user, gmail_pwd)
    mailServer.sendmail(gmail_user, emaillist, msg)
    # Should be mailServer.quit(), but that crashes...
    mailServer.close()

    #print emaillist
    pass