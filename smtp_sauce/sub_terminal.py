'''
Create a terminal through Python path, where commands are edited by Python programs.
'''
# Python libraries
import sys
import os

# Modules
import smtp_sauce
import smtp_source2
import restore

## Read the commands and pass it into a list of command's options
## Params:	command - terminal command
def read_command(command):
	params = command.split()
	if params != []:
		if params[0] == 'smtp-sauce' :
			try:
				origval, filename = restore.windowsize_store()
				# smtp-sauce
				smtp_sauce.smtp_sauce(params)
			except Exception as exc:
				print exc
				
				# Check and restore system changes
				checkval, filename = restore.windowsize_store()
				if checkval != origval:
					try:
						restore.windowsize_restore(origval)
						print 'System restored succesfully!'
					except Exception as _exc:
						print _exc
						print 'FATAL: Failed to restore system! Please open file %s and change its data to %s' % (filename, origval)
						sys.exit()
						
		elif params[0] == 'smtp-source2' :
			try:
				# smtp-source2
				smtp_source2.smtp_source2(params)
			except Exception as exc:
				print exc
		else:
			os.system(command)		#run a normal terminal command
	
	os.system("find . -name '*.pyc' -delete")


## Get the command from terminal
## Return: the command or 'exit' the program
def sub_terminal():
	print "The program will keep taking input until you type 'exit'\n"
	while 1 == 1:
		call = raw_input('>> ')
		if call == 'exit':
			sys.exit()
		else:
			read_command(call)

sub_terminal()
