##PyDskChk

![PyDskChk Command Line](http://i.imgur.com/VNIUF.jpg)

PyDskChk or Python Disk Checker is a simple Python only system for monitoring disks or folders. It has both local functionality (just alerting a terminal (and soon a file)) and email functionality. It simply takes a path and monitors it, when the path becomes unavalible it will print to the window and email you (through SMTP) with an alert.  
PyDskChk was developed for UZ's large a** RAID system (Over 300 disks to monitor) and is not _currently_ in use, although use is planned in the future. It was written and developed by [Andrei Zbikowski](http://az.wbbmx.org/) and was written to help manage large raid disk drives. It's free and open source, and probably 10x worse then any other disk checking system.   
  
Thanks To
==========
PyDskChk deserves credit to a few people...  
Bob2 on Freenode's Python for recommending while True:  
  
PyDskChk uses a few systems...  
[ConfigObj](http://bit.ly/eauaQx) was written by Michael Foord and Nicola Larosa. It's currently used for parsing settings.cfg into our diskchecker.py  
[SMTPLib](http://effbot.org/librarybook/smtplib.htm) a included module in Python 2.5 and later, it's the core to the email system.  
