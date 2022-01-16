"""
Created by cyborgoat at 2022/1/16
Email: cyborgoat@outlook.com

Description
-----------

"""
import json
import smtplib
from email.mime.text import MIMEText
from email.header import Header

with open("email-identities-nosync.json", 'r', encoding='utf-8') as jf:
    email_info = json.load(jf)
    email_addr = email_info.get('username', None)
    email_psswd = email_info.get('password', None)
    target_email = email_info.get('target_email', None)

message = MIMEText('Python Script Test', 'plain', 'utf-8')
message['From'] = Header(email_addr.split('@')[0], 'utf-8')  # 发送者
message['To'] = Header(target_email.split('@')[0], 'utf-8')  # 接收者

subject = 'Python SMTP Email Test'
message['Subject'] = Header(subject, 'utf-8')

connection = smtplib.SMTP("smtp.qq.com")
connection.starttls()
connection.login(user=email_addr, password=email_psswd)
connection.sendmail(from_addr=email_addr, to_addrs=target_email, msg=message.as_string())
connection.close()
