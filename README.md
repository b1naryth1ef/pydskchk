##PyDskChk

![PyDskChk Command Line](http://i.imgur.com/VNIUF.jpg)

PyDskChk or Python Disk Checker is a simple Python only system for monitoring disks or folders. It has both local functionality (just alerting a terminal (and soon a file)) and email functionality. It simply takes a path and monitors it, when the path becomes unavalible it will print to the window and email you (through SMTP) with an alert.  
PyDskChk was developed for UZ's large a** RAID system (Over 300 disks to monitor) and is not _currently_ in use, although use is planned in the future. It was written and developed by [Andrei Zbikowski](http://az.wbbmx.org/) a freelance teen programmer. It's free and open source, and probably 10x worse then any other disk checking system.   

###Using it
PyDskChk both has module and normal support. To run it just as a normal application, edit the /reqs/example_settings.cfg and rename it settings.cfg . Then run start.py and enjoy ;) To import this in a script, type the following:
  
    import diskchecker.py
    finder = diskchecker.checker(PATH)
    while true:
        if finder == "1":
            pass
        elif finder == "0":
            print "Error"
        elif finder == "3":
            print "Error loading module"

    
###Thanks To  
####PyDskChk deserves credit to a few people...  
Bob2 on Freenode's Python for recommending while True:  
[Patrick](http://talk.jeelabs.net/topic/704) from the JeeLabs talk forums for getting me intrested in making the disk checker email people...
    
####PyDskChk uses a few systems...  
[ConfigObj](http://bit.ly/eauaQx) was written by Michael Foord and Nicola Larosa. It's currently used for parsing settings.cfg into our diskchecker.py  
[SMTPLib](http://effbot.org/librarybook/smtplib.htm) a included module in Python 2.5 and later, it's the core to the email system.  
