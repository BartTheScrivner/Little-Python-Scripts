import PyPDF2, os, sys
from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger

pdf_in = open('//Users/Olympus/Desktop/TEPDF.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(pdf_in)
pdf_writer = PyPDF2.PdfFileWriter()
 
for pagenum in range(pdf_reader.numPages):
    page = pdf_reader.getPage(pagenum)
    if pagenum % 2:
        page.rotateClockwise(180)
    pdf_writer.addPage(page)
 
pdf_out = open('rotated.pdf', 'wb')
pdf_writer.write(pdf_out)
pdf_out.close()
pdf_in.close()

