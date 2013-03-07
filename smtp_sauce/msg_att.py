'''
Add attachments to message
'''

# Python libraries
import os
import sys 
import smtplib
import mimetypes
from random import choice
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email import encoders


## Attach a file to the email
## Params:	msg - the email
##		filename - the file
## Return: The email with attachments
def msg_att(message, filename):

	ctype, encoding = mimetypes.guess_type(filename)
	if ctype is None or encoding is not None:
		ctype = 'application/octet-stream'
	
	maintype, subtype = ctype.split('/', 1)
	if maintype == 'text':
		f = open(filename)
		msg = MIMEText(f.read())
		f.close()
	elif maintype == 'audio':
		f = open(filename, 'rb')
		msg = MIMEAudio(f.read(), _subtype = subtype)
		f.close()
	elif maintype == 'image':
		f = open(filename, 'rb')
		msg = MIMEImage(f.read(), _subtype = subtype)
		f.close()
	elif maintype == 'application':
		f = open(filename)
		msg = MIMEApplication(f.read(), _subtype = subtype)
		f.close()
	else:
		f = open(filename, 'rb')
		msg = MIMEBase(f.read(), _subtype = subtype)
		f.close()
		encoders.encode_base64(msg)

	return message.attach(msg)

## Attach a random file in folder 
## Params:	folder - folder's directory
## Return: a random file's directory
def random_att(folder):
	list_files = os.listdir(folder)
	filename = choice(list_files)
	filepath = os.path.join(folder, filename)
	return filepath


def create_att(DEFAULT, msg):
	if (DEFAULT['-a'] != '') and (DEFAULT['-ra'] != ''):
		raise Exception("Conflict-Options: Cannot create '-a' with '-ra'")

	elif DEFAULT['-a'] != '' :
		message = msg_att(msg, DEFAULT['-a'])
		return message

	elif DEFAULT['-ra'] != '':
		filename = random_att(DEFAULT['-ra'])
		message = msg_att(msg, filename)
		return message

	else:
		return msg
