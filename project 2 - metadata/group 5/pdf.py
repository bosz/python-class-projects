import optparse
from pyPdf import PdfFileReader

def get_metadata(pdf):
	ret={}
	pdf_toread = PdfFileReader(open(pdf, "rb"))
	pdf_info = pdf_toread.getDocumentInfo()

	
	print str(pdf_info)



parser = optparse.OptionParser()

parser.add_option('-f', dest='filePath', type='string',help='Please Specify the pdf fileName')

option = parser.parse_args()[0]

print option
file_metadata = get_metadata(option.filePath)


#for key, value in file_metadata.items():
#    print str(key) + ' : ' + str(value)
