import smtplib
import string
import os
import time
import email.Utils
from email.mime.text import MIMEText
from reqs.configobj import ConfigObj
import reqs.downloader
import socket
import urllib2
__Version__ = "0.2.4.1B"
versionhash = "001"
 
                                                       #If you got here, please go and edit settings.py !!!!
config = ConfigObj("./reqs/settings.cfg")                            #Although this isnt technically a .py file, it's just easy for packaging.
path = config['path']
email = config['email']
versionchk = config['versionhash']
sentfrom = config['sentfrom']
username = config['username']
password = config['password']
smtpserver = config['server']
osdis = config['os']
delay = config['delay']

def external():
    ip = urllib2.urlopen("http://www.whatismyip.com/automation/n09230945.asp").read()
    return ip
     
def internal():
    internal = socket.gethostbyname(socket.gethostname())
    return internal

def checkos():
    if osdis == "mac":
        pass
    elif osdis == "lin":
        print "Linux support is buggy at best. Report problems on the Github page please!"
    elif osdis == "win":
        print "Sorry we don't currently support Windows! Windows support is coming in V0.4!"
        import sys
        sys.exit()
             
def updatecheck():
	print "checking for update"
	import urllib
	urllib.urlretrieve ("http://wbbmx.org/code/pydskchk/versions.cfg", "versions.cfg")
	config2 = ConfigObj("./versions.cfg")
	latest = config2['latest']
	updurl = config2['url']
def updatecheck2():
    frx = versionhash.split("-")
    print frx[0]
    if frx[0] < versionchk:
        print "Updating..."
        reqs.downloader.dl(updurl) 
    else:
        print "No update..."
        pass
    
    
def checker(chkpath):
    return os.path.exists(chkpath)


def doemail(location,reason):
    exip = external()
    inip = internal()
    print "Sending email..."
    subject = "Disk/Folder:"+path+" is missing!"
    func = "There is a disk or folder error (001) on disk/folder: "+path+" . External IP of: "+exip+" and internal IP of: "+inip+" ."
    msg = MIMEText(func)
    msg['Subject'] = 'Disk error on ' + path
    msg['From'] = sentfrom
    msg['To'] = email     # functions to send an email
    server = smtplib.SMTP(smtpserver)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username,password)
    server.sendmail(sentfrom, email, msg.as_string())
    server.quit()
    print " SENT!"
		
def main():
    checkos()
    #updatecheck()
    delayx = float(delay)  
    def tester():
        x = checker(path)
        if x == False:
            print "Disk/Folder Not Found!"
            reason = "Not Found!"
            doemail(path,reason)
        else:
            time.sleep(delayx)
            tester()
    print "Disk checker is running!"
    tester()