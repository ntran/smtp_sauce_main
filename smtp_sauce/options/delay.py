'''
Wait for a random/fix time between messages
'''

import random


def delay(DEFAULT):
	o_delay = DEFAULT['-w'] * (DEFAULT['-R'][0] + DEFAULT['-R'][1])

	if o_delay > 0:
		raise Exception("Conflict-Options: Cannot use '-R' with '-w'") 
	
	elif DEFAULT['-R'][1] > 0:
		wait = random.randint(DEFAULT['-R'][0], DEFAULT['-R'][1])
		return wait

	elif DEFAULT['-w'] > 0:
		return DEFAULT['-w']

	else:
		return 0