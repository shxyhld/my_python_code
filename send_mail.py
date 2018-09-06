#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os
import datetime

def send_file(receiver, subject, content, filename=''):
	sender = '123456789@sina.com'
	password = 'abcdefg'
	title = sender

	smtpserver = 'smtp.sina.com'
	smtp = smtplib.SMTP_SSL(smtpserver,'465')
	smtp.login(sender,password)

	msg = MIMEMultipart()
	msg['From'] = Header(title)
	msg['To'] = Header(receiver, 'utf-8')
	msg['Subject'] = Header(subject, 'utf-8')
	msg.attach(MIMEText(content, 'plain', 'utf-8'))
	
	if filename:
		att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
		att1["Content-Type"] = 'application/octet-stream'
		filename = os.path.basename(filename)
		att1["Content-Disposition"] = 'attachment; filename=%s' % filename
		msg.attach(att1)
	try:
		smtp.sendmail(sender, receiver, msg.as_string())
		print 'success'
	except smtplib.SMTPException as e:
		print ('fail',e)
	smtp.quit()
	
if __name__ == '__main__':
	send_file('123456789@sina.com', 'auto_mail3_subject','auto_mail3_content', 'test.txt')