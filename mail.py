#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import qqlist
from email.mime.text import MIMEText
from email.header import Header


def send_mail(content,subject='Feedback'):
    mail_host=qqlist.mail_host  #设置服务器
    mail_user=qqlist.mail_user    #用户名
    mail_pass=qqlist.mail_pass   #口令


    sender = qqlist.mail_user
    receivers = [qqlist.mail_user ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header('mail_user', 'utf-8')
    message['To'] = Header('mail_user', 'utf-8')
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
    except Exception as e:
        pass

if __name__ == '__main__':
    send_mail('test')
