#!/usr/bin/python
import sys
import re
import PyPDF2
#from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

appname = 'pdfmrg.py'
usage = """  This script merges multiple PDF files into a single file

Usage: 
 > python """ + appname + """ FILE1.PDF FILE2.PDF FILE3.PDF

Output: merged.pdf
"""
#input("Press Enter to continue...")

myargs = sys.argv    # read command line args
if len(myargs) < 2:  # if there are not enough args, print usage and exit
    print("ERROR: not enough parameters.\n")
    print(usage)
    #input("Press Enter to continue...")
    sys.exit()

pdfs = []
for infile in myargs[1:]:
    print(infile)
    if not re.search("\.PDF$", infile, re.IGNORECASE):
        print("ERROR: Input", infile, "is not a PDF file.\n")
        #input("Press Enter to continue...")
        sys.exit(usage)
    pdfs.append(infile)

#sys.exit('Goodbye')

print(pdfs)
input("Press Enter to continue...")

#sys.exit('Goodbye')

merger = PyPDF2.PdfMerger()
writer = PyPDF2.PdfWriter()

for pdf in pdfs:
    reader = PyPDF2.PdfReader(pdf)
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        page.compress_content_streams()
        writer.add_page(page)
    merger.append(pdf)

merger.write('Scan2merge.pdf')
with open('Scan2PageWrite.pdf', 'wb') as f:
    writer.write(f)
