from PIL import Image
from PIL.ExifTags import TAGS

try:
    imageDetails = Image.open("IMG_20160516_065215.jpg")._getexif() # Getting the image meta data as a dictionary

    for (k,v) in imageDetails.iteritems():
        print '%s = %s' % (TAGS.get(k), v) #Printing the meta data
except:
    print 'Sorry the File Could Not Be Opened'