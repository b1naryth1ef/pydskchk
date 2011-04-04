import os
SENDMAIL = "/usr/sbin/sendmail" # sendmail location

path = "./test" #Path of disk to monitor
email = "EMAIL@EMAIL.COM" #Your email

def doemail(location,reason):
	p = os.popen("%s -t" % SENDMAIL, "w")
	p.write("To:"+email+"\n")
	p.write("Subject: DISK ERROR ON DISK "+path+"\n")
	p.write("\n") # blank line separating headers from body
	p.write("PATH: "+path+"\n")
	p.write("REASON: "+reason+" \n")
	sts = p.close()
	if sts != 0:
		print "Sendmail exit status", sts


def main():
	if os.path.exists(path) == True:
		print "Found"
		import time
		time.sleep(10)
		main()
	elif os.path.exists(path) == False:
		print "Gone"
		reason = "Not Found!"
		doemail(path,reason)
	else:
		doemail(path,reason)
		print "ERRORZ"
		reason = "Random error!"	
main()
