import zipfile, sys

if len(sys.argv) < 3:
	print "Usage: %s /path_to_dictionary /path_to_zip_file" %(str(sys.argv[0]))
	print "Example: %s ./dict.txt ./hello.zip " %(str(sys.argv[0]))
	print "Dictionary should only contain one password per line"
	sys.exit(1)
	
dic = sys.argv[1]; zFile = sys.argv[2]

def extractFile(z, password):
    try:
        z.extractall(pwd=password)
        return password
    except:
        return

def main():
    z = zipfile.ZipFile(zFile)
    passFile = open(dic)
    for line in passFile.readlines():
        password = line.strip('\n')
        guess = extractFile(z, password)
        if guess:
            print '[+] Password = ' + password + '\n'
            exit(0)

    print 'Warning: Password not found!'

main()
