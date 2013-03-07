'''
Add subject to message
'''

def create_subject(subject, msg):
	msg['Subject'] = subject
	return msg

def create_headers(filename, msg):

	HEADERS = ["Apparently-To", "Bcc", "Cc", "Content-Description", "Content-Disposition", "Content-ID", "Content-Length", "Content-Transfer-Encoding", "Content-Type", "Delivered-To", "Disposition-Notification-To",     "Date", "Errors-To", "From", "Mail-Followup-To", "Message-Id", "MIME-Version", "Received", "Reply-To", "Resent-Bcc", "Resent-Cc", "Resent-Date",     "Resent-From", "Resent-Message-Id", "Resent-Reply-To", "Resent-Sender", "Resent-To", "Return-Path", "Return-Receipt-To", "Sender", "Subject", "To"]


	body = ''
	f = open(filename, 'r')
	for line in f:
		_line = line.split()
		#print _line
		if _line == []:
			continue
		else:
			found = False
			for i in HEADERS:
				if _line[0].replace(':', '') == i :
					msg['%s' % i] = ' '.join(_line[1:])
					found = True
					break
			if not found:
				body += ' '.join(_line) + '\n'

	return msg, body

