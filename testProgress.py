'''
Created on Jan 5, 2012

@author: wwward
'''

import simpleProgress
import sys, time

if __name__ == '__main__':
    s = simpleProgress.display(sys.argv[1], sys.argv[2])
    s.clear()
    for i in range(0,32):
        s.write('.')
        time.sleep(.5)
    time.sleep(2)
    s.write('0')
    s.close()
    sys.exit(0)