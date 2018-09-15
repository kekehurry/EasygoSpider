import imapclient
import settings
from email.parser import Parser
import os
import time

def control():
    server=imapclient.IMAPClient('imap.qq.com',ssl = True)
    server.login(settings.mail_user,settings.mail_pass)


    server.select_folder('INBOX',readonly = True)
    UIDS=server.search(['FROM %s'%settings.mail_user,'UNSEEN'])
    mail = server.fetch(UIDS,['BODY[]'])
    msg = Parser().parsestr(mail[UIDS[0]][b'BODY[]'].decode('utf-8'))
    subject = msg.get('Subject')
    print(subject)

    if subject=='Start':
        os.chdir("F:\\Desktop\\EasygoSpider-master\\EasygoSpider")
        os.system("taskkill /f /t /im powershell.exe")
        os.system("taskkill /f /t /im cmd.exe")
        os.system(".\\run.bat")
    if subject=='Stop':
        os.chdir("F:\\Desktop\\EasygoSpider-master\\EasygoSpider")
        os.system("taskkill /f /t /im powershell.exe")
        os.system("taskkill /f /t /im cmd.exe")

def update_github():
    os.chdir("F:\\Desktop\\EasygoSpider-master\\EasygoSpider")
    os.system("git add .")
    os.system("git commit -m \'refresh\'")
    os.system("git push")

if __name__ == '__main__':
    while True:
        control()
        time.sleep(60)
