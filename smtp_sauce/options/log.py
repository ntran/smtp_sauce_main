'''
Create a logfile of all the attachments sent through the server
'''
import os
import time
import socket

## Email
def messages(DEFAULT, logbody, att):
	if DEFAULT['-log']:
		current = time.strftime("%x %X")
		tos = ';'.join(DEFAULT['-t'])
		DEFAULT['logfile'].write("%s |  Email-- From: <%s>. To: <%s>. Body-length: %s. Attachment: %s. \n" % (current, DEFAULT['-f'], tos, logbody, att))
	return 0		 

## Retry email
def retries(DEFAULT, times, total):
	if DEFAULT['-log']:
		current = time.strftime("%x %X")
		DEFAULT['logfile'].write("%s |  Retry Email-- Attempt ..%s/%s\n" % (current, times, total))
	return 0

## Connections established
def connects(DEFAULT, host, port):
	if DEFAULT['-log']:
		try:
			ipinfo = socket.gethostbyaddr(host)
			ips = ','.join(ipinfo[2])
		except:
			ips = host
		current = time.strftime("%x %X")
		DEFAULT['logfile'].write("%s |  Connect to <%s> %s:%s \n" % (current, host, ips, port))
	return 0

## Disconnect to servers
def disconnects(DEFAULT, host, port):
	if DEFAULT['-log']:
		ipinfo = socket.gethostbyaddr(host)
		ips = ','.join(ipinfo[2])
		current = time.strftime("%x %X")
		DEFAULT['logfile'].write("%s |  Disconnect from <%s> %s:%s \n" % (current, host, ips, port))
	return 0

## Errors
def errors(DEFAULT, error):
	if DEFAULT['-log']:
		current = time.strftime("%x %X")
		DEFAULT['logfile'].write("%s |  %s \n" % (current, error))
	return 0


