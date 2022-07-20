#!/usr/bin/python
import PyPDF2
from PIL import Image
import os
import sys

pdf = 'tmp.pdf'
writer = PyPDF2.PdfFileWriter()

files = os.listdir(".")
flst = [fn for fn in files if '.png' in fn]
for fn in flst:
    print(fn)
    im = Image.open(fn)
    im.save(pdf, 'PDF', resolution=100.0)
    reader = PyPDF2.PdfFileReader('tmp.pdf')
    for i in range(reader.numPages):
        page = reader.getPage(i)
        page.compressContentStreams()
        writer.addPage(page)

with open('merged.pdf', 'wb') as f:
    writer.write(f)
