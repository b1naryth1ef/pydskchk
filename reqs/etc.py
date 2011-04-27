import subprocess
from email.mime.text import MIMEText
import smtplib
from configobj import ConfigObj
import urllib2
import socket
import sys

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
fchanges = config['filechanges']
filepath = config['file']

def external():
    ip = urllib2.urlopen("http://www.whatismyip.com/automation/n09230945.asp").read()
    return ip
     
def internal():
    internal = socket.gethostbyname(socket.gethostname())
    return internal

class MemoryMonitor(object):

    def __init__(self, username):
        """Create new MemoryMonitor instance."""
        self.username = username

    def usage(self):
        """Return int containing memory used by user's processes."""
        self.process = subprocess.Popen("ps -u %s -o rss | awk '{sum+=$1} END {print sum}'" % self.username,
                                        shell=True,
                                        stdout=subprocess.PIPE,
                                        )
        self.stdout_list = self.process.communicate()[0].split('\n')
        return int(self.stdout_list[0])


memory_mon = MemoryMonitor('root')
used_memory = memory_mon.usage()


def doemail(path,reason):
    exip = external()
    inip = internal()
    print "Sending email..."
    subject = "Disk/Folder:"+path+" is missing!"
    func = "There is a disk or folder error (001) on disk/folder: "+path+" . \nExternal IP of: "+exip+"\nInternal IP of: "+inip+" .\n"
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
    fr2 = "python"
    proc2 = subprocess.Popen(["killall",fr2])