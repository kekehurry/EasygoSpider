#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import settings
from email.mime.text import MIMEText
from email.header import Header


def send_mail(content):
    mail_host=settings.mail_host  #设置服务器
    mail_user=settings.mail_user    #用户名
    mail_pass=settings.mail_pass   #口令


    sender = settings.mail_user
    receivers = [settings.mail_user ]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("easygospider", 'utf-8')
    message['To'] =  Header(settings.mail_user, 'utf-8')

    subject = 'easygospider'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
    except Exception as e:
        pass
