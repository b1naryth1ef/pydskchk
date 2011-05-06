##PyDskChk

![PyDskChk Command Line](http://i.imgur.com/s9RYF.jpg)

PyDskChk, or Python Disk Checker, is a simple, minimalistic, low resources monitoring system for disks, files and folders. It not only can simply print to the console, but also alert you by email (through SMTP). PyDskChk is basically a compilation of a bunch of other tools out there, but it has a unique handling of File Changes and reporting. It's in constant development making it more likely it will work on your system! PyDskChk was developed for a large server system partly maintained by its developer, [Andrei Zbikowski](http://az.wbbmx.org/) a teen developer.
  
PyDskChk is 100% free and opensource, and probably not as good as other disk checking/monitoring systems. 

###Using it
####Configuration
PyDskChk has a settings file for easy customizing and deploying. Simply open up /reqs/example_settings.cfg and edit the settings (described below). Then save the file, and rename it settings.cfg. Run start.py in the home directory and you're all set. 
  
checkdisk : Either "1" or "0". This sets whether to check a disk/folder  
checkfile : Either "1" or "0". This sets whether to check a file for changes.  
sound : Either "1" or "0". This sets whether to play a sound on disk/folder/file error
diskpath : Path to the disk or folder to check  
filepath : Path to the file to monitor  
fromemail : The email (and smtp login) to send from.  
toemail : The email to send alerts too.  
password : SMTP Password  
server : SMTP Server  
dev : Should be 'True', 'False', or 'Full' Further explanation in "Debugging" below.

####Hacking
PyDskChk is open source, so I really encourage people to hack it. One way you can work with it, is by testing out the Windows and Linux functionality for me (And reporting [issues](https://github.com/b1naryth1ef/pydskchk/issues) if you find them).
  
PyDskChk has a very cool way to monitor files for changes. If your interested in using this as a module, you'll need to look through the source yourself. Basically we take a snapshot of the files info using os.stat(PATH). We then take the list and split out st\_atime and st_mtime. Which are time of most recent access and time of most recent content modification respectively. We then wait for a interval defined by us, or the user (3-6 seconds is good) and take another snap shot. We can simply then do some basic logic. All together it looks a little like this:
    
    import os
    import time
    stat1 = os.stat(FILE/FOLDER)
    time.sleep(5)
    stat2 = os.stat(FILE/FOLDER)
    if stat1 < stat2:
    	print "File Changed!"
    else:
    	pass
This could also be achieved by if stat1 != stat2, but I feel more comfortable with it this way...

####Debugging
PyDskChk has a nice debugging system built into it. Whenever the dev flag is on (in settings), you'll get some basic information about what its doing, as well as feedback when you reach errors. If you still have trouble narrowing down where your problem is, try setting the dev flag to "full". This prints out all the traces and info about whats going on. You can always open up an [issue](https://github.com/b1naryth1ef/pydskchk/issues) if need be.

  
####Side notes
PyDskChk doesnt have a large footprint on your computer/servers resources. This is a screen grab of the basic Disk Checker running on Python 2.6 on Mac 10.6.6. 
![%0 CPU, 1 Thread, 4.7MB RAM, 20.4MB VRAM](http://i.imgur.com/jYDpW.jpg) 

###Thanks To  
####PyDskChk deserves credit to a few people...  
Bob2 on Freenode's Python for recommending while True:  
[Patrick](http://talk.jeelabs.net/topic/704) from the JeeLabs talk forums for getting me interested in making the disk checker email people...  
[Strike](http://forums.devshed.com/member.php?u=13758) from the devshed forums for shedding light on my File Changes problem.
  
####PyDskChk uses a few systems...  
[ConfigObj](http://bit.ly/eauaQx) was written by Michael Foord and Nicola Larosa. It's currently used for parsing settings.cfg into our diskchecker.py  
[SMTPLib](http://effbot.org/librarybook/smtplib.htm) a included module in Python 2.5 and later, it's the core to the email system.  
