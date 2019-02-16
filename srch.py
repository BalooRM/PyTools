# read search terms as command line arguments and compare to STDIN
import sys
import re

usage = ("Usage: \n"
         " > python srch.py first second < file.txt\n" 
         " > python srch.py first second third < file.txt\n" 
         " > python srch.py \"first term\" second < file.txt")

myargs = sys.argv     # read command line args
#print (myargs)
if len(myargs) == 1:  # if there are no args, print usage and exit
    sys.exit (usage)

#for i in range(1, len(myargs)):    # loop from 1 to n, ignore 0th argv
#    print (myargs[i])

for line in sys.stdin:
    ls = line.split('\n')                 # split STDIN on newline
    for i in range(0, len(ls)):           # loop from 0 for all lines
        myflag = 1                        # set flag = 1, assume all match
        for j in range (1, len(myargs)):  # loop from 1, ignore argv[0]
            m = re.search(myargs[j], ls[i], re.IGNORECASE)
            if m == None:    # if search fails, returning Nonetype result
                myflag = 0   # set flag to 0
        if myflag == 1:
            print (ls[i].strip())
