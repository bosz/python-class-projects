import os
import time 
from stat import *


try: 
	st = os.stat('Akpos.mp4')
except IOError:
	print "Couldn't get information about video"
	
else:
	print "for video"
	print "file size: ", st[ST_SIZE]
	print "file modified: ", time.asctime(time.localtime(st[ST_MTIME]))
	print "Access Rights: ", st[ST_MODE]
	
try: 
	st = os.stat('new.pdf')
except IOError:
	print "Couldn't get information about PDF"
	
else:
	print "for PDF"
	print "file size: ", st[ST_SIZE]
	print "file modified: ", time.asctime(time.localtime(st[ST_MTIME]))
	
try: 
	st = os.stat('pic.jpg')
except IOError:
	print "Couldn't get information about Image"
	
else:
	print "for Image"
	print "file size: ", st[ST_SIZE]
	print "file modified: ", time.asctime(time.localtime(st[ST_MTIME]))