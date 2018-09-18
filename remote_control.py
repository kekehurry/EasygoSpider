import imapclient
import mail
import qqlist
from email.parser import Parser
import os
import threading
import time

def readmail():
    server=imapclient.IMAPClient('imap.qq.com',ssl = True)
    server.login(qqlist.mail_user,qqlist.mail_pass)
    server.select_folder('INBOX',readonly = False)
    UIDS=server.search(['FROM %s'%qqlist.mail_user,'UNSEEN'])
    content = server.fetch(UIDS,['BODY[]'])
    try:
        msg = Parser().parsestr(content[UIDS[0]][b'BODY[]'].decode('utf-8'))
        subject = msg.get('Subject')
    except Exception as e:
        subject=""
    return subject

def control(subject):
    if subject=='Start':
        os.chdir("C:\\Users\\Kaius\\Desktop\\EasygoSpider")
        os.system("taskkill /f /t /im powershell.exe")
        os.system("taskkill /f /t /im cmd.exe")
        os.system(".\\run.bat")
    if subject=='Stop':
        os.chdir("C:\\Users\\Kaius\\Desktop\\EasygoSpider")
        os.system("taskkill /f /t /im powershell.exe")
        os.system("taskkill /f /t /im cmd.exe")
        mail.send_mail("%s Done!"%subject)

def update_github():
    os.chdir("C:\\Users\\Kaius\\Desktop\\EasygoSpider")
    os.system("git add .")
    os.system("git commit -m \'refresh\'")
    os.system("git push")

if __name__ == '__main__':
    while True:
        try:
            subject=readmail()
            if subject != "":
                print(subject)
                t=threading.Thread(target=control,args=(subject,),name='Control')
                t.start()
            else:
                print("waiting for instruction")
            time.sleep(60)
        except Exception as e:
            print(e)
            pass
 
