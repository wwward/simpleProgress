'''
Created on Jan 5, 2012

@author: wwward
'''

import serial, sys

class display:
    def __init__(self, usb='/dev/ttyUSB0', baud=9600, debug=True):
        try:
            self.comm = serial.Serial(usb, baud)
            if debug: print "serial init" + usb + baud
        except serial.SerialException:
            sys.exit("error initializing port")
            
        self.comm.setRTS(0)
        
    def clear(self):
        self.comm.write(chr(0xFE)+chr(0x01))
        
    def write(self,string):
        self.comm.write(string)
    
    def __exit__(self):
        self.comm.close()
        
if __name__ == '__main__':
    d = display(sys.argv[1],sys.argv[2])
    d.clear()
    d.write('foo')
    sys.exit(0)
    