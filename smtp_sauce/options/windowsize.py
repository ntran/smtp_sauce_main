'''
Change the default TCP windows size
'''
import os

# #Change default windowsize
def change_default(new_val):
    syschange = False
    f = open('/proc/sys/net/core/wmem_default', 'r')
    val = f.readline()
    if (new_val > 0) and (val > 0):
        # Open and read origninal wmem value      
        # Assign new value
        print 'Changing TCP Default Windowsize... (password may be required)'
        os.system('sudo sysctl -w net.core.wmem_default=%s' % new_val)
        syschange = True
    return val, syschange

## Restore the original windowsize
def restore_default(new_val, old_val, syschange):
    if (new_val > 0) and (old_val > 0) and (syschange):
        print 'Restore system defaults...'
        os.system('sudo sysctl -w net.core.wmem_default=%s' % old_val)
    return 0
       
        