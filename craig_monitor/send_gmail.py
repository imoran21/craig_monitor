import smtplib
import email

from email.mime.text import MIMEText
from settings import update_path
from password_settings import email_password, fromaddr, toaddr
import json
import datetime


def create_body(update_path):
    with open(update_path) as update_file:
        update_data = json.load(update_file)
    msg = ""
    for i,m in enumerate(update_data): 
        for k,v in m.items():
            link = k 
            values = (v)
        msg += '\n\n------------------------------------------\n'
        msg += 'NEW POST # {} {} \n'.format(i+1,k)
        msg += '\t TITLE: {} \n'.format(values['title'].encode('utf-8'))
        msg += '\t LOCATION: {} \n'.format(values['location'].encode('utf-8'))

        msg += '\t Housing: {} \n'.format(values['housing'].encode('utf-8'))
        msg += '\n\n------------------------------------------\n' 
        msg += '\t Post Body : \n\t\t {} \n'.format(values['body'].encode('utf-8'))
    return str(msg), len(update_data)

def send_gmail(body_text, fromaddr, toaddr,email_password,item_count):
    smtp_host = 'smtp.gmail.com'
    smtp_port = 587
    
    server = smtplib.SMTP()
    server.connect(smtp_host,smtp_port)
    server.ehlo()
    server.starttls()
    server.login(fromaddr,email_password)

    sub = '{} New Craigslist Posts found! [Automated Tracking]  {}'.format(item_count+1, str(datetime.datetime.now()))

    msg = email.MIMEMultipart.MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = email.Utils.COMMASPACE.join([toaddr])
    msg['Subject'] = sub  
    msg.attach(MIMEText(body_text))
    msg.attach(MIMEText('\nsent via python', 'plain'))
    server.sendmail(fromaddr,toaddr,msg.as_string())

def main_email():
    body_text,item_count  = create_body(update_path)
    if body_text:
         print 'email created' 
         send_gmail(body_text, fromaddr, toaddr, email_password, item_count)
         print 'email sent!'
    else:
        print 'no email sent as there are no new posts'

