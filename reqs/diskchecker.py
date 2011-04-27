import string
import os
import time
import sys
from configobj import ConfigObj
import downloader
from etc import MemoryMonitor
import subprocess
import signal
import etc
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
fchanges = config['filechanges']
filepath = config['file']


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

def memusage(): #not in use currently
    memory_mon = MemoryMonitor('username')
    used_memory = memory_mon.usage()
    return used_memory

def pusher(path,reason):
    etc.doemail(path,reason)
    	
def main():
    if fchanges == "1":
        xf32 = "/Users/Andrei/Code/pydskchk/reqs/test.py"
        proc = subprocess.Popen(["python", xf32, filepath, delay])
    else:
        None    
    checkos()
    #updatecheck()
    delayx = float(delay)
    def tester():
        x = checker(path)
        if x == False:
            print "Disk/Folder Not Found!"
            reason = "Not Found!"
            etc.doemail(path,reason)
            os.kill(proc.pid, signal.SIGUSR1)
            import sys
            sys.exit()
        else:
            time.sleep(delayx)

    print "Disk checker is running!"
    while True:
        tester() 