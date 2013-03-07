'''
Check FROM, TO email address
'''

def from_to(from, to, hostport):
	host, port = hostport.split(':')
	from += host
	to += port