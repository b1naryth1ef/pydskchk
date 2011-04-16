import smtplib
import string
import os
import email.Utils
from email.mime.text import MIMEText
#from configobj import ConfigObj
from reqs.configobj import ConfigObj
__Version__ = "0.2.2"
                                                                          #If you got here, please go and edit settings.py !!!!
config = ConfigObj("./reqs/settings.cfg")   
versioner = config['version']                              #Although this isnt technically a .py file, it's just easy for packaging.
sendmail = config['sendmail']
path = config['path']
email = config['email']
sentfrom = config['sentfrom']
smtp = config['smtp']
username = config['username']
password = config['password']
smtpserver = config['server']
x = "0"

def versioncheck():
    if versioner == "DEV":
        print "Running in developer Mode!"
        devmode = "1"
    elif versioner != __Version__:
        print "ERROR: Please update your config to the current running version: "+__Version__+""
        import sys
        sys.exit()
    else:
        pass
def checker(chkpath):
     while True:
        if os.path.exists(chkpath) == True:
    		return 1
    	elif os.path.exists(chkpath) == False:
         return 0
         break
    	else:
            return 2

def printer(prints):
	if x == "0":
		print prints
	else:
		None
def doemail(location,reason):
	subject = "Disk/Folder:"+path+" is missing!"
	func = "There is a disk or folder error (001) on disk/folder: "+path+" ."
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
		
def main():
    while True:
    	if os.path.exists(path) == True:
    		printer("Disk/Folder Found")
    		x = "1"
    	elif os.path.exists(path) == False:
    		printer("Disk/Folder Not Found!")
    		x = "1"
    		reason = "Not Found!"
    		doemail(path,reason)
    		break
    	else:
    		doemail(path,reason)
    		print "ERRORZ"
    		reason = "Random error!"
