'''
Add message body to email
'''
# Python libraries
from email.mime.text import MIMEText

# Modules
import rlength
import msg_headers

## Create a message body
def prepare_body(msg, body):
	body = MIMEText(body, 'plain')
	return msg.attach(body)


## Create the email needed to be sent
## Params
def create_body(DEFAULT, msg):

	## Check conflicts
	llength = DEFAULT['-l'] * (DEFAULT['-rl'][0] + DEFAULT['-rl'][1])
	if llength > 0:
		raise Exception("Conflict-Options: Cannot use '-l' with '-rl'") 
	elif (DEFAULT['-F'] != '') and ((DEFAULT['-rl'][1] > 0) or (DEFAULT['-l'] > 0)):
		raise Exception("Conflict-Options: Cannot use '-F' with '-l' or '-rl'")

	elif DEFAULT['-rl'][1] > 0:			
		body = rlength._rl(DEFAULT['-rl'][0], DEFAULT['-rl'][1])
		message = prepare_body(msg, body)
		return message, len(body)

	elif DEFAULT['-l'] > 0:
		body = rlength._l(DEFAULT['-l'])
		message = prepare_body(msg, body)
		return message, DEFAULT['-l']
	
	elif DEFAULT['-F'] != '':
		_message, body = msg_headers.create_headers(DEFAULT['-F'], msg)
		message = prepare_body(_message, body)
		return message, 0
	
	else:
		return DEFAULT['default_body'], 0
