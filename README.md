##PyDskChk

![PyDskChk Command Line](http://i.imgur.com/HTbqc.jpg)

PyDskChk, or Python Disk Checker, is a simple, minimalistic, low resources monitoring system for disks, files and folders. It has both local console functionality, and remote SMTP functionality for email alerts. PyDskChk for disks and folders, uses Pythons built it os.path.exists() function to check when a path or disk becomes unavalible. It then reports that to the console, and can email you. PyDskChk was developed for a large server system partly maintaned by its devloper, [Andrei Zbikowski](http://az.wbbmx.org/) a teen developer.
  
PyDskChk is 100% free and opensource, and probably not as good as other disk checking/monitoring systems. 

###Using it
####Configuration
PyDskChk has a settings file for easy customizing and deploying. Simply open up /reqs/example_settings.cfg and edit the settings (described below). Then save the file, and rename it settings.cfg. Run start.py in the home directory and you're all set. Note for each run you can only choose either checkdisk or checkfile. If both are set to one, checkdisk is used.
  
checkdisk : Either "1" or "0". This sets whether to check a disk/folder  
checkfile : Either "1" or "0". This sets whetehr to check a file for changes.  
diskpath : Path to the disk or folder to check  
filepath : Path to the file to monitor  
fromemail : The email (and smtp login) to send from.  
toemail : The email to send alerts too.  
password : SMTP Password  
server : SMTP Server  
dev : Should be False unless your running this on Mac >10.4 or Windows. True will enable developer features.

####Hacking
PyDskChk is open source, so I really encourage people to hack it. One way you can work with it, is by testing out the Windows and Linux functionality for me (And reporting [issues](https://github.com/b1naryth1ef/pydskchk/issues) if you find them).
  
PyDskChk has a very cool way to monitor files for changes. If your intrested in using this as a module, either break out the code yourself (in the filemonitormod() function), or use PyDskChk as a module. Simply import Main and then run Main.filemonitormod(PATH,INTERVAL) interval is recommended to be higher then 5.
  
####Side notes
PyDskChk doesnt have a large footprint on your computer/servers resources. This is a screen grab of the basic Disk Checker running on Python 2.6 on Mac 10.6.6. 
![%0 CPU, 1 Thread, 4.7MB RAM, 20.4MB VRAM](http://i.imgur.com/jYDpW.jpg) 

###Thanks To  
####PyDskChk deserves credit to a few people...  
Bob2 on Freenode's Python for recommending while True:  
[Patrick](http://talk.jeelabs.net/topic/704) from the JeeLabs talk forums for getting me intrested in making the disk checker email people...  
[Strike](http://forums.devshed.com/member.php?u=13758) from the devshed forums for shedding light on my File Changes problem.
  
####PyDskChk uses a few systems...  
[ConfigObj](http://bit.ly/eauaQx) was written by Michael Foord and Nicola Larosa. It's currently used for parsing settings.cfg into our diskchecker.py  
[SMTPLib](http://effbot.org/librarybook/smtplib.htm) a included module in Python 2.5 and later, it's the core to the email system.  
