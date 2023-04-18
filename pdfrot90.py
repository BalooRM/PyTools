#!/usr/bin/python
import sys
import re
import PyPDF2
#from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

appname = sys.argv[0]
usage = """  This script rotates one or more PDF files and saves as new file(s)

Usage: 
 > python """ + appname + """ FILE1.PDF FILE2.PDF

Output: FILE1_rot90.pdf FILE2_rot90.pdf etc.
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

for pdf in pdfs:
    reader = PyPDF2.PdfFileReader(pdf)
    writer = PyPDF2.PdfFileWriter()
    outfile = pdf[:-4] + "_rot90.pdf"
    for i in range(reader.numPages):
        page = reader.getPage(i)
        page.compressContentStreams()
        writer.addPage(page.rotateClockwise(90))
    print(outfile)
    with open(outfile, 'wb') as f:
        writer.write(f)
