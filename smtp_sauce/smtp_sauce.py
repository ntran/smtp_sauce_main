## Author: Nguyen Tran
## Python version: 2.7

'''
Execute smtp-sauce commands just like smtp-source, but with more options
'''

# Python libraries
import os
import sys
import smtplib
from socket import *

# Modules
from options import display_options
from options import ipv_
from options import windowsize
import send_mail

USAGE = 'Usage: smtp-sauce -4 -6 -a file -A -c -C count -d -f from -F headerfile -l length -log -L -m msgcount -M myhostname -N -o -r recipientcount -R mintime maxtime -ra folder -rl minlength maxlength -s sessioncount -S subject -t to -tm -T windowsize -v -w interval host[:port]'

## Execute the command
## Params:	params - (array) a list of command's options
def smtp_sauce(params):
	
	# Options dictionary
	INITIAL = {'default_body': 'Text goes here.',
			'logfile': '',
			'-4' : False, 
			'-6' : False, 
			'-a' : '',
			'-A' : False,
			'-c' : False,
			'-C' : 0,
			'-d' : False, 
			'-f' : 'foo', 
			'-F' : '',
			'-l' : 0,
			'-log': False,
			'-L' : False,
			'-o' : False,
			'-ra': '', 
			'-rl': [0, 0], 
			'-R' : [0, 0],
			'-m' : 1, 
			'-M' : '', 
			'-N' : False,
			'-r' : 1, 
			'-s' : 1, 
			'-S' : '', 
			'-t' : ['foo'],
			'-T' : 0,
			'-tm': False,
			'-v' : 0,
			'-w' : 0}

	DEFAULT = INITIAL	#Initialize default values
	COUNT = 0
	LOGFILE = "smtp.log"

	# Create 'from' address from the host
	hostname = gethostname()
	DEFAULT['-f'] = '%s@%s' % (DEFAULT['-f'], hostname)
	DEFAULT['-t'][0] = '%s@%s' % (DEFAULT['-t'][0], hostname)

	host, port = read_command(params, DEFAULT)
	old_val, syschange = windowsize.change_default(DEFAULT['-T'])	# Change TCP windowsize
	if DEFAULT['-log']:
		logpath = os.path.join(os.getcwd(), LOGFILE)
		DEFAULT['logfile'] = open(logpath, 'w')
	# Create and send mails
	if DEFAULT['-s'] > 1:
		COUNT, time_elapse = send_mail._parallel(DEFAULT, host, port)
	else:
		COUNT, time_elapse = send_mail._series(DEFAULT, host, port)

	
	windowsize.restore_default(DEFAULT['-T'], old_val, syschange)	# Restore TCP windowsize

	# Print counter and timer
	if (DEFAULT['-c']):
		os.system('echo %s' % COUNT)
	display_options.display_time(DEFAULT['-tm'], time_elapse)
	if DEFAULT['-log']:
		DEFAULT['logfile'].close()
	return 0


## Analyze the command, assign the values to DEFAULT after reading it
## Params:	params - (array) a list of options
##			DEFAULT - (dictionary) a dictionary of input options
## Return:	a full email message 
def read_command(params, DEFAULT): 
	if len(params) == 1:
		raise Exception('ERROR: %s' % USAGE )
		
	try:
		for i in range(1, len(params)):	
			if params[i] == '-4':
				DEFAULT['-4'] = True
	
			elif params[i] == '-6':
				DEFAULT['-6'] = True
	
			elif params[i] == '-a':
				DEFAULT['-a'] = params[i+1]
				
			elif params[i] == '-A':
				DEFAULT['-A'] = True
	
			elif params[i] == '-c':
				DEFAULT['-c'] = True
				
			elif params[i] == '-C':
				DEFAULT['-C'] = int(params[i+1])
	
			elif params[i] == '-d':
				DEFAULT['-d'] = True
	
			elif params[i] == '-f':
				DEFAULT['-f'] = params[i+1]
	
			elif params[i] == '-F':
				DEFAULT['-F'] = params[i+1]
	
			elif params[i] == '-l':
				DEFAULT['-l'] = int(params[i+1])
				
			elif params[i] == '-log':
				DEFAULT['-log'] = True
				
			elif params[i] == '-L':
				DEFAULT['-L'] = True
			
			elif params[i] == '-m':
				DEFAULT['-m'] = int(params[i+1])
	
			elif params[i] == '-M':
				DEFAULT['-M'] = params[i+1]
			
			elif params[i] == '-N':
				DEFAULT['-N'] = True
	
			elif params[i] == '-o':
				DEFAULT['-o'] = True
	
			elif params[i] == '-r':
				DEFAULT['-r'] = int(params[i+1])
					
			elif params[i] == '-ra':
				DEFAULT['-ra'] = params[i+1]	
	
			elif params[i] == '-rl':
				DEFAULT['-rl'][0] = int(params[i+1])
				DEFAULT['-rl'][1] = int(params[i+2])
	
			elif params[i] == '-R':
				DEFAULT['-R'][0] = int(params[i+1])
				DEFAULT['-R'][1] = int(params[i+2])
	
			elif params[i] == '-s':
				DEFAULT['-s'] = int(params[i+1])
	
			elif params[i] == '-S':
				DEFAULT['-S'] = params[i+1]			
	
			elif params[i] == '-t':
				DEFAULT['-t'] = [params[i+1]]
				
			elif params[i] == '-T':
				DEFAULT['-T'] = params[i+1]
			
			elif params[i] == '-tm':
				DEFAULT['-tm'] = True
	
			elif params[i] == '-v':
				DEFAULT['-v'] = 1
		
			elif params[i] == '-w':
				DEFAULT['-w'] = int(params[i+1])
				
		# Check for valid host
		try:
			host, port = params[len(params) - 1].strip().split(':')
		except:
			host = params[len(params) -1]
			port = ''
		
		try:
			host, port = ipv_.connect_ip(DEFAULT['-4'], DEFAULT['-6'], host, port)
		except Exception as exc:
			raise ('FATAL: %s' % exc)

	except:
		raise Exception('ERROR: %s' % USAGE )
		
	return host, port
