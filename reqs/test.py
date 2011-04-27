import os
import time
import sys
import etc
import diskchecker




filepath = sys.argv[1]
delay = sys.argv[2]
def filechanges():
    print "File Changes is running!"
    x = os.stat(filepath)
    delayx = float(delay)
    while True:
        time.sleep(delayx)
        x2 = os.stat(filepath)
        if x[8] < x2[8]:
            print "Changed"
            reason = "File changed!"
            diskchecker.pusher(filepath,reason)
            sys.exit()
        elif x[9] < x2[9]:
            print "changed"
            reason = "File changed!"
            diskchecker.pusher(filepath,reason)
            sys.exit()
        else:
           None
filechanges()
