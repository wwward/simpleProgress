'''
Created on Jan 5, 2012

@author: wwward
'''

import simpleProgress
import sys

if __name__ == '__main__':
    s = simpleProgress.display(sys.argv[1], sys.argv[2])
    s.clear()
    s.write('foobar_test')