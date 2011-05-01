#!/usr/bin/env python
# encoding: utf-8
import sys
import os
import smtplib
from email.MIMEText import MIMEText
import time
from email.mime.text import MIMEText
from configobj import ConfigObj
import socket
import urllib2
import platform
__Version__ = "0.4.1"
config = ConfigObj("./reqs/settings.cfg")
checkdisk = config['checkdisk']
checkfile = config['checkfile']
path2 = config['diskpath']
path = config['filepath']
email = config['fromemail']
toemail = config['toemail']
password = config['password']
surv = config['server']
dev = config['dev']
def oscheckr():
    osname = platform.system()
    osver = platform.release()
    if osname == "Darwin":
        if osver > 10.4:
            print "PyDskChk Version:",__Version__,"loaded on Mac",osver
        elif osver < 10.4:
            if dev = True:
                print "PyDskChk Version:",__Version__,"loaded on Mac",osver,"[DEV MODE]"
            else:
                print "Mac support is buggy on systems older then Mac 10.4. Set the 'dev = True' flag in the settings file to use this on",osver
                sys.exit()
    if osname == "Windows":
        if dev = True:
            print "PyDskChk Version:",__Version__,"loaded on",osname,osver,"[DEV MODE]"
        else:
            print "Windows support is buggy. Set the 'dev = True' in the settings file to use this on Windows"
            sys.exit()

oscheckr()
    
def external():
    ip = urllib2.urlopen("http://www.whatismyip.com/automation/n09230945.asp").read()
    return ip
     
def internal():
    internal = socket.gethostbyname(socket.gethostname())
    return internal

def filechecker(path,interval):
    x = os.stat(path)
    time.sleep(5)
    x2 = os.stat(path)
    if x[8] < x2[8]:
        print "Changed! [1]"
        eip = external()
        iip = internal()
        message = "The file or folder: "+path+" has been changed, modified or deleted.\n External IP: "+eip+" \nInternal IP: "+iip
        mailer(message) 
        sys.exit()
    elif x[9] < x2[9]:
        print "Changed! [2]"
        eip = external()
        iip = internal()
        message = "The file or folder: "+path+" has been changed, modified or deleted.\nExternal IP: "+eip+" \nInternal IP: "+iip 
        mailer(message) 
        sys.exit()
    else:
        None

def diskchecker(path,interval):  
    delayx = float(interval)
    x = os.path.exists(path)
    if x == False:
        print "Disk/Folder at "+path+" Not Found!"
        message = "A Disk or Folder located at "+path+" become locked, unavalible or was deleted!"
        mailer(message)
        import sys
        sys.exit()
    else:
        time.sleep(delayx)

def mailer(msgx):
    msg = MIMEText(msgx)
    msg['Subject'] = 'Disk or file error!'
    msg['From'] = email
    msg['To'] = toemail 
    server = smtplib.SMTP(surv,587) #port 465 or 587
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email,password)
    server.sendmail(email,toemail,msg.as_string())
    server.close()

def main():
    if checkdisk == "1":
        print "Disk Checker initated on "+path2
        while True:
            diskchecker(path2,5)
    else:
        pass
    if checkfile == "1":
        print "File Checker initated on "+path
        while True:
            filechecker(path,5)
    else: 
        pass
        
#Final stuff... Keep at the end
if __name__ == '__main__':
	main()