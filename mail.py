#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
import poplib
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


def receive_mail():
    email = settings.mail_user
    password =settings.mail_user
    pop3_server = "pop.qq.com"

    server = poplib.POP3(pop3_server,995)
    print(server.getwelcome())
    server.user(email)
    server.pass_(password)
# list()返回所有邮件的编号:
    resp, mails, octets = server.list()
    print(mails)
# 获取最新一封邮件, 注意索引号从1开始:
    index = len(mails)
    resp, lines, octets = server.retr(index)
# lines存储了邮件的原始文本的每一行,
# 可以获得整个邮件的原始文本:
    msg_content = '\r\n'.join(lines)
# 稍后解析出邮件:
    print(msg_content)

    server.quit()

if __name__ == '__main__':
    receive_mail()
