'''
In case the program quit unexpectedly, restore all changes have been made to system files
'''
import os

#### Restore TCP windowsize case
## Store original windowsize
def windowsize_store():
    wmem_default = '/proc/sys/net/core/wmem_default'
    f = open(wmem_default, 'r')
    val = f.readline()
    return val, wmem_default

## Restore original windowsize
def windowsize_restore(old_val):
    print 'The program has encountered errors. Reverting changes... (password may be required)'
    os.system('sudo sysctl -w net.core.wmem_default=%s' % old_val)
    return 0