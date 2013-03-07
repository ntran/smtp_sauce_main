'''
Create random file/message with a random size
'''

import os
import random

## KB, MB, GB sizes 
SIZE = {'K': 1, 'M': 1024, 'G': 1048576}

## Temporary file will be created with a given size
tempfile = 'temp.txt'


## Create a random file with a size in range
## Params:	times - repetitive times
##		range_min - Minimum file size
##		range_max - Maximum file size 
def randomize(range_min, range_max):
	size = random.randint(range_min, range_max)
	return size

## Create a random message payload with a given range
## Params:	range_min - minimum size
##		range_max - maximum size
## Return: Generate a random message payload
def _rF(range_min, range_max):	
	size = randomize(range_min, range_max)
	return size


## Create a fix sized message
## Params:	size - messange's size
## Return:	a fixed size message
def _l(size):
	times = int(round(size/1024, 0))
	rest = size - times*1024

	# msg string below is 1024 characters = 1KB
	kb = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\nxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n'

	msg = ''.join([kb for i in xrange(0, times)])
	_msg = ''.join(['x' for i in xrange(0, rest)])
	msg += _msg	
	return msg


## Create a file with a given range size
## Params:	range_min - minimum size
##		range_max - maximum size
## Return: Generate a random file
def _rl(range_min, range_max):
	size = randomize(range_min, range_max)
	return _l(size)


## Split string to a number and a letter
## Params:	string - a string
## Return: A number and a letter
def split_string(string):
	l = len(string) - 1

	num = string[:l]
	type = string[l]

	return int(num), type	
