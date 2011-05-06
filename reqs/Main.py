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
import threading
from threading import Thread
__Version__ = "0.4.3"
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
def dp(message):
    if dev == 'True' or 'Full':
        print "\t[DEV] "+message
    else:
        pass
def er(message,details):
    if dev == 'True' or 'Full':
        print "\t[ERROR] "+message+" "+details
    elif dev == 'False':
        print "\t[ERROR] "+message
    else:
        pass 
def trace(message):
    if dev == 'Full':
        print "\t[TRACE] "+message
    else:
        pass  
def oscheckr():
    trace("@oscheckr Start")
    osname = platform.system()
    osver = platform.release()
    trace("@oscheckr_if")
    if osname == "Darwin":
        if osver > 10.4:
            print "PyDskChk Version:",__Version__,"loaded on Mac",osver
            dp("Loaded on Mac <10.4")
        elif osver < 10.4:
            if dev == 'True':
                dp("Loaded on Mac >10.4")
                print "PyDskChk Version:",__Version__,"loaded on Mac",osver,"[DEV MODE]"
            else:
                print "Mac support is buggy on systems older then Mac 10.4. Set the 'dev = 'True'' flag in the settings file to use this on",osver
                sys.exit()
    if osname == "Windows":
        if dev == 'True':
            print "PyDskChk Version:",__Version__,"loaded on",osname,osver,"[DEV MODE]"
        else:
            print "Windows support is buggy. Set the 'dev = 'True'' in the settings file to use this on Windows"
            trace("_SYSTEM EXIT_")
            sys.exit()

oscheckr()
    
def external():
    trace("@external")
    dp("Called external IP")
    ip = urllib2.urlopen("http://www.whatismyip.com/automation/n09230945.asp").read()
    return ip
     
def internal():
    trace("@internal")
    dp("Called internal IP")
    internal = socket.gethostbyname(socket.gethostname())
    return internal

def filechecker(path,interval):
    x = os.stat(path)
    time.sleep(5)
    x2 = os.stat(path)
    if x[8] < x2[8]:
        trace("@filechecker/fail/x[8]")
        print "Changed! [1]"
        eip = external()
        iip = internal()
        message = "The file or folder: "+path+" has been changed, modified or deleted.\n External IP: "+eip+" \nInternal IP: "+iip
        mailer(message) 
        sys.exit()
    elif x[9] < x2[9]:
        trace("@filechecker/fail/x[9]")
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
        trace("@diskchecker/fail/x")
        eip = external()
        iip = internal()
        print "Disk/Folder at "+path+" Not Found!"
        message = "A Disk or Folder located at "+path+" become locked, unavalible or was deleted!\nExternal IP: "+eip+"\nInternal IP: "+iip
        mailer(message)
        import sys
        sys.exit()
    else:
        time.sleep(delayx)

def mailer(msgx):
    trace("@mailer")
    print "Mailing error message..."
    dp("Called mailer")
    msg = MIMEText(msgx)
    msg['Subject'] = 'Disk or file error!'
    msg['From'] = email
    msg['To'] = toemail 
    server = smtplib.SMTP(surv,587) #port 465 or 587
    dp("Connected to server...")
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email,password)
    dp("Logged in")
    server.sendmail(email,toemail,msg.as_string())
    dp("Message sent")
    server.close()
    dp("Server connection severed")
    print "MESSAGE SENT!"
def initdisk(path,time):
    trace("@initdisk")
    dp("Loaded DiskChecker")
    while True:
        diskchecker(path,time)
def initfile(path,time):
    trace("@filechecker") 
    dp("Loaded FileChecker")  
    while True:
        filechecker(path,time)
def both(path1,time1,path2,time2):
    dp("Loaded File&Disk Checker")
    trace("@both")
    while True:
        filechecker(path2,time2)
        diskchecker(path1,time1)
def main():
    trace("@main")
    dp("Loaded main function")
    if checkdisk == "1" and checkfile=="0":
        dp("Diskchecker running, file checker off")
        print "Disk checker running! ["+path2+"]"
        Thread(target = initdisk, args =(path2,5) ).start()
    elif checkfile == "1" and checkdisk=="1":
        dp("Disk and File checker running")
        print "Disk checker running! ["+path2+"]"
        print "File checker running! ["+path+"]"
        Thread(target = both, args = (path2,5,path,5) ).start()
    elif checkfile == "1" and checkdisk=="0":
        dp("File checker running, disk checker  off")
        print "File checker running! ["+path+"]"
        Thread(target = initfile, args =(path,5)).start()
        
#Final stuff... Keep at the end
if __name__ == '__main__':
    trace("@__name__")
    main()