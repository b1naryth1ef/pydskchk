import smtplib
import string
import os
import mailer
import email.Utils
from email.mime.text import MIMEText

#---------------EDIT BELOW------------------#
SENDMAIL = "/usr/sbin/sendmail" # sendmail location
path = "./test" #Path of disk to monitor
email = "ateamrocks@gmail.com" #Your email
sentfrom = "azcomp@passthrough.com"
#fp = open("emailfile", 'wb+rb')

#--------DO NOT EDIT BELOW THIS LINE--------#


x = "0"
def printer(prints):
	if x == "0":
		print prints
	else:
		None
	
def doemail(location,reason):
	p = os.popen("%s -t" % SENDMAIL, "w")
	p.write("To:"+email+"\\n")
	p.write("Subject: DISK ERROR ON DISK "+path+"\\n")
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
		doemail(path,reason)
		break
	else:
		doemail(path,reason)
		print "ERRORZ"
		reason = "Random error!"
		
