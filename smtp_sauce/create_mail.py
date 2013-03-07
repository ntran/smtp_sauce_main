'''
Create email base on given information
'''
# Python libraries
from email.mime.multipart import MIMEMultipart

# Modules
from options import msg_att
from options import msg_body
from options import msg_headers
from options import log

## Create email
## Params:	headers - Message headers
##		body	- Message body
##		att	- Message attachments
## Return: an email message
def create_mail(DEFAULT):
	msg = MIMEMultipart()
	temp, logbody = msg_body.create_body(DEFAULT, msg) 		#Body
	temp, logatt = msg_att.create_att(DEFAULT, msg)		#Attachment
	# If not old mode, send headers
	if not DEFAULT['-o']:
		msg_headers.create_subject(DEFAULT['-S'], msg)	#Subject
	log.messages(DEFAULT, logbody, logatt)
	msg_final = msg.as_string()
	return msg_final
