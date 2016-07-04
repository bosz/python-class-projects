# the following program probes a provided host for open ports
#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime
#some functions
def scanHost(portList, remoteServerIPaddress):
	""" scan ports in a list using a tuple (remoteServerIPaddress, port) where port is any port in the portList ouputs open ports"""
	try:
	    for port in portList:  
	        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	        result = sock.connect_ex((remoteServerIPaddress, port))
	        if result == 0:
	            print "Port {}: 	 Open".format(port)
	        sock.close()
	except KeyboardInterrupt:
		print "You pressed Ctrl + C"
		sys.exit()
	except socket.gaierror:
		print "Hostname could not be resolved. Exiting ..."
	except socket.error:
		print "Could not connect to server"
		sys.exit()

def messageToUser(remoteServer):
	""" This method writes a friendly message to the screen for the user"""
	print "*"*50
	print "Hold on while I scan the remote host", remoteServer
	print "*"*50

def tellScanDuration(startTime, endTime):
	""" This takes the startTime and endTime computes the duration of the port scan and prints it out"""
	totalTime = endTime - startTime
	print "Scanning completed in: ",totalTime

def remoteServerConfigurations():
	"""This function requests user input and returns remoteServerIp"""
	remoteServer = raw_input("Enter a remote host for scanning: ")
	remoteServerIP = socket.gethostbyname(remoteServer)
	return remoteServer, remoteServerIP
# clear the screen
subprocess.call('clear', shell=True)

server, ip = remoteServerConfigurations()

messageToUser(server)

#note the time the scan started
tStart = datetime.now()

#list of ports to scan
# portList = [21,22,35,43,80,443,558,631,795,3306,4848]
portList = range(1, 9000)

scanHost(portList, ip)

#note the time the scan has ended
tStop = datetime.now()

tellScanDuration(tStart, tStop)
