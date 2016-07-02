from PIL import Image
from PIL.ExifTags import TAGS
import optparse 

def get_metadata(image):
    ret = {}
    i = Image.open(image)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


#parser = optparse.OptionParser("usage %prog "+ "-f <path to file>")

parser = optparse.OptionParser()

parser.add_option('-f', dest='filePath', type='string',help='Please Specify the image fileName')

option = parser.parse_args()[0]

print option

image_metadata = get_metadata(option.filePath)
for key, value in image_metadata.items():
    print str(key) + ' : ' + str(value)
    
