from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

try:
    fp = open('diveintopython.pdf', 'rb')
    parser = PDFParser(fp)
    doc = PDFDocument(parser)

    print doc.info[0]
except:
    print 'Sorry the File Could Not Be Opened'