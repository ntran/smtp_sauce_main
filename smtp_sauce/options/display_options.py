'''
Display counter and elapse-time
'''
import os

## Display counter
## Params:	_c - Indicate if the user type '-c'
##		count - The current count 
def display_counter(_c, count):
	if (_c) :
		os.system("printf " + str(count) + "\r")
	return 0


## Display time
## Params:	_tm - Indicate if the user type '-tm'
##		elapse - elapsed time
def display_time(_tm, elapse):
	if (_tm) :
		elapse = round(elapse, 2)
		sec = elapse % 60
		_min = (elapse - sec)/60
		min = _min % 60
		hour = (_min - min)/60
		os.system("echo [Elapsed-time]  %d:%02d:%.2f" % (hour, min, sec))
	return 0
