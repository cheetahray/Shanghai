import pysimpledmx
import time
mydmx = pysimpledmx.DMXConnection("/dev/ttyUSB0")
'''
chan = [ 0, 0, 0, 0,
         0, 0, 0, 1,
         0, 0, 1, 0,
         0, 0, 1, 1,
         0, 1, 0, 0,
         0, 1, 0, 1,
         0, 1, 1, 0,
         0, 1, 1, 1,
         1, 0, 0, 0,
         1, 0, 0, 1,
         1, 0, 1, 0,
         1, 0, 1, 1,
         1, 1, 0, 0,
         1, 1, 0, 1,
         1, 1, 1, 0,
         1, 1, 1, 1 ]
'''
chan = [ 
         0, 0, 0, 1,
         0, 0, 1, 0,
         0, 1, 0, 0,
         1, 0, 0, 0
       ]
jj = 0
while True:
    for ii in range(0,16,4):         
        mydmx.setChannel(1, chan[ii]) # set DMX channel 1 to full
        print chan[ii]
        mydmx.setChannel(2, chan[ii+1]) # set DMX channel 2 to 128
        print chan[ii+1]
        mydmx.setChannel(3, chan[ii+2]) # set DMX channel 3 to 0
        print chan[ii+2]
        mydmx.setChannel(4, chan[ii+3])    
        print chan[ii+3]
        mydmx.render()
        time.sleep(5)
