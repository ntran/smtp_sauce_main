'''
Send emails 
'''
# Python libraries
import smtplib
import time

# Modules
import create_mail
from options import display_options
from options import recipient_count
from options import delay
from options import log

## Send email in series
## Params:	DEFAULT - DEFAULT values of the call
##		host - host name
##		port - port number
## Return: print counter and elapsed-time
def _series(DEFAULT, host, port):
	COUNT = 0
	time_xtra = 0
	
	wait = delay.delay(DEFAULT)
	to_list = recipient_count.create_recipient(DEFAULT['-t'], DEFAULT['-r'])
	
##    All the parameters that contains 'time' is to calculate the total time taken to Connect to server, Send mails, and Disconnect.
	
	time_st = time.time()
	# Connect to host	
	server = connect(DEFAULT, host, port)

	# If no message's body specified, send the email with default-message-body
	for j in range(0, DEFAULT['-m']):

		# Create email and display counter
		_time_xtra = time.time()
		message = create_mail.create_mail(DEFAULT)

		COUNT += 1
		display_options.display_counter(DEFAULT['-c'], COUNT)

		if (DEFAULT['-N']):
			to_list = recipient_count.change_recipient(DEFAULT['-t'], j)

		time_xtra += time.time() - _time_xtra

		# Send email
		send(DEFAULT, server, to_list, message, COUNT, host, port)
		# Delay
		time.sleep(wait)

		# If want to disconnect, quit server and reconnect for next message
		if (not DEFAULT['-d']) and (j < DEFAULT['-m']-1):
			disconnect(DEFAULT, server, host, port)
			server = connect(DEFAULT, host, port)

	disconnect(DEFAULT, server, host, port)

	time_elapse = time.time() - time_st - time_xtra
	return COUNT, time_elapse

## Send emails in parallel
## Params:	DEFAULT - DEFAULT values of the call
##		host - host name
##		port - port number
## Return: print counter, elapsed-time
def _parallel(DEFAULT, host, port):
	
	sessions = DEFAULT['-s']
	messages = DEFAULT['-m']
	# Get the delay
	wait = delay.delay(DEFAULT)
	to_list = recipient_count.create_recipient(DEFAULT['-t'], DEFAULT['-r'])
	
	COUNT = 0
	servers = []
	time_elapse = 0

	# Connect to servers
	for j in range(0, sessions):
		server = connect(DEFAULT, host, port)
		servers.append(server)

	# Send a <sessions> amount of messages parallel 
	times = int(round(messages/sessions, 0))
	for i in range(0, times):
		COUNT, _time = send_parallel(DEFAULT, sessions, COUNT, wait, to_list, servers, host, port)
		time_elapse += _time
		
	# Send the <rest> amount of the messages parallel
	rest = messages - times*sessions
	if rest > 0:
		COUNT, _time = send_parallel(DEFAULT, rest, COUNT, wait, to_list, servers, host, port)
		time_elapse += _time

	# If didn't close all the servers, close them now.
	if (DEFAULT['-d']):
		for i in range(0, sessions):
			disconnect(DEFAULT, servers[i], host, port)
						
	return COUNT, time_elapse

## Send a certain amount of emails in parallel 1 time
## Params:	DEFAULT - DEFAULT dictionary
##		amount - number of parallel sessions
##		servers - list of parallel sessions
##		host - host name
##		port - port number
## Return: Increase the counter and calculate elapsed-time
def send_parallel(DEFAULT, amount, count, wait, to_list, servers, host, port):
	xtra = 0

	_time = time.time()
	# Send emails
	for j in range(0, amount):	
		_xtra_time = time.time()
		# Create mail
		message = create_mail.create_mail(DEFAULT)
		# Display counter
		count += 1
		display_options.display_counter(DEFAULT['-c'], count)
		
		xtra_time = time.time() - _xtra_time
		xtra += xtra_time

		# Send emails
		send(DEFAULT, servers[j], to_list, message, count, host, port)
		# Delay	
		time.sleep(wait)
		
	# If want to disconnect, close the servers and reconnect
	if not (DEFAULT['-d']):
		for j in range(0, amount):
			disconnect(DEFAULT, servers[j], host, port)
			servers[j] = connect(DEFAULT, host, port)

	_time = time.time() - _time - xtra
	return count, _time

## Connect to server
## Params:	DEFAULT - Default dictionary
##			host - server's IP
##			port - connection port
## Return: Connected server
def connect(DEFAULT, host, port):
	try:
		log.connects(DEFAULT, host, port)
		if (DEFAULT['-L']):
			server = smtplib.LMTP(host, port)
		else:
			server = smtplib.SMTP(host, port)
	except Exception as exc:
		log.connects(DEFAULT, host, port)
		log.errors(DEFAULT, exc)
		raise Exception(exc)

	server.set_debuglevel(DEFAULT['-v'])
	# If not old mode, send HELO
	if not DEFAULT['-o']:
		server.helo(DEFAULT['-M'])
	return server

## Disconnect from server
## Params:	DEFAULT - DEFAULT dictionary
##			server - current connected server
##			host - server's IP
##			port - connecting port
## Return: disconnected server
def disconnect(DEFAULT, server, host, port):
	server.quit()
	log.disconnects(DEFAULT, host, port)
	return server


## Send email according to given host, port, server, and message
## Params:	DEFAULT - Default dictionary
##			server - server used to send mail
##			to_list - list of recepient
##			message - containing message
##			count - counter
def send(DEFAULT, server, to_list, message, count, host, port):
	try:
		server.sendmail(DEFAULT['-f'], to_list, message)
	except Exception as exc1:
		# If do not Abort whenever the server sends a negtive code
		if (DEFAULT['-A']):
			try:
				# If no retries after host send RST, print warning
				if DEFAULT['-C'] <= 0:
					error = 'WARNING: %s - Message #%s' % (exc1, count)
					log.errors(DEFAULT, error)
					print Exception(error)

				else:
					# Retry to send mail
					for i in range(0, DEFAULT['-C']):
						server.set_debuglevel(0)
						try:
							log.retries(DEFAULT, i+1, DEFAULT['-C'])
							server.sendmail(DEFAULT['-f'], to_list, message)
							break
						except Exception as exc3:
							error = 'WARNING: %s - Message #%s' % (exc3, count)
							log.errors(DEFAULT, error)
							print Exception(error)
							continue

			except Exception as exc2:
				# Still fail, print Warning but do not abort
				error = 'WARNING: %s - Message #%s' % (exc2, count)
				log.errors(DEFAULT, error)
				print Exception(error)
		else:
			# Raise error
			error = 'FATAL: %s' % exc1
			log.errors(DEFAULT, error)
			disconnect(DEFAULT, server, host, port)
			raise Exception(error)
			
			
	
