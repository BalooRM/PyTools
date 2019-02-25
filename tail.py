# read 0..1 command line args and print out last [number] lines from STDIN
import sys
#import re

usage = ("Usage: \n"
         " > python tail.py [number] < file.txt\n" 
         " Return last [number] lines or 10 by default, if unspecified\n") 

#print (usage)
myargs = sys.argv     # read command line args
mystart = 0
mynumlines = 10

if len(myargs) == 1:  # if there are no args, default to 10
    mynumlines = 10
elif myargs[1].isdigit():
    mynumlines = int(myargs[1])
else:
    sys.exit (usage)

lsout = []
for line in sys.stdin:
    ls = line.split('\n')                 # split STDIN on newline
    for i in range(0, len(ls)-1):
        lsout.append(ls[i].rstrip())

mystart = len(lsout) - mynumlines
if mystart < 0:
    mystart = 0
for i in range(mystart, len(lsout)):     # loop from start to end
    print (i, "\t", lsout[i])
