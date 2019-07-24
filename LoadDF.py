# Load Pandas dataframe from file
import pandas as pd
import numpy as np
from chardet import UniversalDetector
import sys
import re

usage = ("Usage: \n"
         " This script loads a data file as a Pandas DataFrame and summarizes contents.\n"
         " > python LoadDF.py filename.extension (.txt, .csv, .tsv, .xlsx)\n"
         )

myargs = sys.argv      # read command line args
if len(myargs) == 1:   # if there are no args, then exit
    sys.exit (usage)

myfile = myargs[1]
myflag = 0
df = pd.DataFrame()
detector = UniversalDetector()
f = open(myfile, "rb")
detector.feed(f.read())
detector.close()
f.close()
dctResult = detector.result
myencoding = dctResult['encoding']
print("File", myfile, "encoded as", myencoding)

if re.search(r'\.txt+$', myfile, re.IGNORECASE) != None:
    print ('TXT file')
    myflag += 1
    df = pd.read_csv(myfile, sep='\t', encoding=myencoding)
if re.search(r'\.tsv+$', myfile, re.IGNORECASE) != None:
    print ('TSV file')
    myflag += 1
    df = pd.read_csv(myfile, sep='\t', encoding=myencoding)
if re.search(r'\.csv+$', myfile, re.IGNORECASE) != None:
    print ('CSV file')
    myflag += 1
    df = pd.read_csv(myfile, sep=',', encoding=myencoding)
if re.search(r'\.xlsx+$', myfile, re.IGNORECASE) != None:
    print ('XLSX file')
    myflag += 1
    xlsx = pd.ExcelFile(myfile)
    df = pd.read_excel(xlsx, 'Sheet1') # assume Sheet1

if myflag == 0:
    sys.exit('Unrecognized file extension for file ' + myfile)
    
#df = pd.read_csv('Timesheet_20190101_20190510.tsv', sep ='\t')

print ('Data frame contains the following columns:')
print (df.columns)
print ('\nEach column\'s data contain the unique values as follows:')

for mycol in df.columns:
    print ('\nColumn:\t', mycol, '\t(', len(df[mycol].unique().tolist()), ' unique value(s))', sep='')
    print (df[mycol].unique())

