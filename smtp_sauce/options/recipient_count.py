'''
Create a list of recipient base on the recipient_count
'''

## Create a list of recipients
## Params:	to_list - list of recipients(1 recipient at input)
##		_r	- number of recipients count
## Return: A list of _r recipients
def create_recipient(to_list, _r):
	addr = to_list[0]
	for i in range(1, _r):
		to_list.append(str(i) + addr)
	return to_list

def change_recipient(to_list, num):
	result = ['']*len(to_list)
	for i in range(0, len(to_list)):
		result[i] = "%s%s" % (num, to_list[i])
	return result
