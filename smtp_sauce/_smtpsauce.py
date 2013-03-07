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
def read_command(params):
        #params = command.split()
        if params != []:
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

        os.system("find . -name '*.pyc' -delete")


## Get the command from terminal
## Return: the command or 'exit' the program
def _smtpsauce():
	command = ['smtp-sauce']
	for i in range(1, len(sys.argv)):
		command.append(sys.argv[i])
	read_command(command)

_smtpsauce()
