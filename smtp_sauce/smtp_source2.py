'''
Execute smtp-source in terminal
'''
# Python libraries
import os
from time import time

# Modules
from options import rlength
from options import display_options


## Execute the command
## Params:	params - (array) a list of command's options
def smtp_source2(params):

	# Analyze the command
	params, _time = read_command(params)
	command = ' '.join(params)
	if (_time):
		start_t = time()
		os.system(command)
		elapse = time() - start_t
		display_options.display_time(_time, elapse)
	else:
		os.system(command)


## Read all the options and return it to smtp-sauce (not be sent yet)
## Params:	params - (array) a list of options
##		DEFAULT - (dictionary) a dictionary of input options
## Return:	a full email message 
def read_command(params):
	_time = False	#time indicator
	insertlist = []
	params[0] = 'smtp-source' #Replace clone smtp-source2 with the actual smtp-source

	for i in range(1, len(params)):
		if params[i] == '-rl':
			min_range = int(params[i+1])
			max_range = int(params[i+2]) 
			# Remove these unreal options from command
			params[i], params[i+1], params[i+2] = '', '', ''
			# Create a random length, call '-l' 
			random_length = rlength.randomize(min_range, max_range)		
			insertlist.append((1, '-l'))
			insertlist.append((2, str(random_length)))

		elif params[i] == '-tm':
			_time = True
			params[i] = ''

	for i in params:
		if i == '':
			params.remove(i)

	for (position, call) in insertlist:
		params.insert(position, call)

	return params, _time
	