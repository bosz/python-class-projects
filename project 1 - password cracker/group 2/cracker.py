import zipfile
import optparse
from threading import Thread
def crackZipfile(zFile,word):
   try:              
      zFile.extractall(pwd=word)
      print '[+] Found password: ' + word
      print '[+] File extracted'
      global found
      found=True
      t.exit()
   except:
      #print "Still searching password ......"
      pass
def main():
   found=False
   parser = optparse.OptionParser("usage%prog "+ "-f <zipfile> -d <dictionary>")
   parser.add_option('-f', dest='zname', type='string', help='specify zip file')
   parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
   (options,args) = parser.parse_args()
   if (options.zname == None) | (options.dname == None):
      print parser.usage
      exit(0)
   else:
      zname = options.zname
      dname = options.dname
   zFile = zipfile.ZipFile(zname)
   passFile = open(dname)
   for line in passFile.readlines():
      word = line.strip('\n')
      if found == True:
      	break
      t = Thread(target=crackZipfile, args=(zFile,word))
      t.start()
if __name__ == '__main__':
   main()