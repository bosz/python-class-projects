from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(fname):
	"""Get embedded EXIF data from image file."""
	ret = {}
	try:
		# Open the file
		img = Image.open(fname)
		if hasattr( img, '_getexif' ):
			# extract the EXIF data
			exifinfo = img._getexif()
		if exifinfo != None:
			# Loop through the data extracted and decode
			for tag, value in exifinfo.iteritems():
				decoded = TAGS.get(tag, tag)
				ret[decoded] = value
	# Catch in case of I/O Error
	except IOError:
		print 'IOERROR ' + fname
	return ret

if __name__ == '__main__':
	fileName = 'food.jpg'
	exif = get_exif_data(fileName)
	print "\n\n"
	print exif
	print "\n\n"
