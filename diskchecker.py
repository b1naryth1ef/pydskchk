import smtplib
import string
import os
#import mailer
import email.Utils
from email.mime.text import MIMEText
from configobj import ConfigObj

                                                                   #If you got here, please go and edit settings.py !!!!
config = ConfigObj("settings.cfg")                                 #Although this isnt technically a .py file, it's just easy for packaging.
sendmail = config['sendmail']
path = config['path']
email = config['email']
sentfrom = config['sentfrom']
smtp = config['smtp']
username = config['username']
password = config['password']
smtpserver = config['server']
x = "0"



def printer(prints):
	if x == "0":
		print prints
	else:
		None
def doemail2(location,reason):
	func = "There is a disk or folder error (001) on disk/folder: "+path+" ."
	msg = MIMEText(func)
	msg['Subject'] = 'Temperature'
	msg['From'] = sentfrom
	msg['To'] = email     # functions to send an email
	server = smtplib.SMTP(smtpserver)
	server.ehlo()
	server.starttls()
	server.ehlo()
	server.login(username,password)
	server.sendmail(sentfrom, email, msg.as_string())
	server.quit()
		
def doemail(location,reason):
	p = os.popen("%s -t" % sendmail, "w")
	p.write("To:%s\\n" % email)  
	p.write("Subject: DISK ERROR ON DISK %s\\n" % path)
	p.write("\\n") # blank line separating headers from body
	p.write("PATH: "+path+"\\n")
	p.write("REASON: "+reason+" \\n")
	sts = p.close()
	if sts != 0:
		print "Sendmail exit status", sts

while True:
	if os.path.exists(path) == True:
		printer("Disk/Folder Found")
		x = "1"
	elif os.path.exists(path) == False:
		printer("Disk/Folder Not Found!")
		x = "1"
		reason = "Not Found!"
		doemail2(path,reason)
		break
	else:
		doemail2(path,reason)
		print "ERRORZ"
		reason = "Random error!"
		
