##PyDskChk

![PyDskChk Command Line](http://i.imgur.com/HTbqc.jpg)

Python Disk Checker, or PyDskChk for short, is a simple, minimalistic, low resources monitoring system for disks and folders. It has both local functionality for reporting too a terminal window and email functionality for alerting you over the internet.  
  
PyDskChk simply takes a path to a disk, folder, or file and monitors it. When the path becomes unavailable it both prints out the status to the terminal window, and sends you an email (through SMTP) to alert you of the change.  
  
PyDskChk was created and developed for a large scale RAID system powering Urban Zone, and was completely written and developed by [Andrei Zbikowski](http://az.wbbmx.org/), a freelance teen programmer.  
  
PyDskChk is 100% free and opensource, and probably not as good as other disk checking/monitoring systems. 

###Using it
####Configuration
PyDskChk has a settings file for easy customizing and deploying. Simply open up /reqs/example_settings.cfg and edit the settings (described below). Then save the file, and rename it settings.cfg. Run start.py in the home directory and you're all set.
  
versionhash : You should generally leave this alone. It's there for some basic tracking and is a placeholder for future versions.  
path : The path or file you want to monitor  
email : The email to send alerts too  
sentfrom : The email alerts are being sent from (NOT TO!)  
username : Your SMTP username  
password : Your SMTP password  
server : The smtp server  
os : Should be "mac" or "lin". Windows is buggy, if you really want to use it see the hacks section below.  
delay : The delay between checks. The higher it is the less resources the script requires.  
  
####Module useage
PyDskChk has very VERY basic module support. It was put in place as a holder for future versions. To use it, simply import the diskchecker.py file from /reqs/ and call diskchecker.checker(PATH). Below is a basic example of how to do this...
   
    import reqs.diskchecker
    finder = diskchecker.checker(PATH)
    def simplefunction():
    	if finder = True:
    		MyPathWasFound()
    	elif finder == False:
    		MyPathWasNotFound()
    	else:
    		SomeoneBrokeIt()
####Hacking
PyDskChk is open source, so I really encourage people to hack it. One way you can work with it, is by testing out the Windows and Linux functionality for me (And reporting [issues](https://github.com/b1naryth1ef/pydskchk/issues) if you find them). To run the script on windows, you'll have to change a few lines. Open up /reqs/diskchecker.py in your faviourte text editor, and change out this:
    
        elif osdis == "win":
        print "Sorry we don't currently support Windows! Windows support is coming in V0.4!"
        import sys
        sys.exit()
to this:
	
	elif osdis == "win":
    print "I IZ A HACKER!"
####Side notes
PyDskChk doesnt have a large footprint on your computer/servers resources. This is a screen grab of the basic Disk Checker running on Python 2.6 on Mac 10.6.6. 
![%0 CPU, 1 Thread, 4.7MB RAM, 20.4MB VRAM](http://i.imgur.com/jYDpW.jpg)
  
###Roadmap
PyDskChk is planned to be more then just a small tool. Later on this year a project will spawn using PyDskChk and other tools to provide an all-around system monitor / notifier for python.   
V0.3 : Full email support, more settings and tweaking abilities.   
v0.4 : Better module support.   
v0.5 : Folder/File changes tracking  
V0.6 : Suport for more interfaces.  

###Thanks To  
####PyDskChk deserves credit to a few people...  
Bob2 on Freenode's Python for recommending while True:  
[Patrick](http://talk.jeelabs.net/topic/704) from the JeeLabs talk forums for getting me intrested in making the disk checker email people...
  
####PyDskChk uses a few systems...  
[ConfigObj](http://bit.ly/eauaQx) was written by Michael Foord and Nicola Larosa. It's currently used for parsing settings.cfg into our diskchecker.py  
[SMTPLib](http://effbot.org/librarybook/smtplib.htm) a included module in Python 2.5 and later, it's the core to the email system.  
