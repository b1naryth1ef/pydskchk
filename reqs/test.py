import os
import time
import sys

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
            x = os.stat(filepath)
        elif x[9] < x2[9]:
            print "changed"
            x = os.stat(filepath)
        else:
           None
filechanges()