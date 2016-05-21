import pysimpledmx
import time
mydmx = serial.Serial("/dev/ttyAMA0", baudrate=115200) #mydmx = pysimpledmx.DMXConnection("/dev/ttyUSB0")

chan = [ 1,1,0,0,
         0,1,1,0,
         1,0,1,0,
         1,0,0,1,
         1,1,1,0,
         1,0,1,1,
         1,0,0,0,
         0,1,0,0,
         0,0,1,0,
         0,0,0,1
       ]
         
while True:
    for ii in range(24,40,4):         
        #mydmx.setChannel(2, chan[ii]) # set DMX channel 1 to full
        print chan[ii]
        #mydmx.setChannel(3, chan[ii+1]) # set DMX channel 2 to 128
        print chan[ii+1]
        #mydmx.setChannel(4, chan[ii+2]) # set DMX channel 3 to 0
        print chan[ii+2]
        #mydmx.setChannel(5, chan[ii+3])    
        print chan[ii+3]
        #mydmx.render()
        mydmx.write(str(chan[ii])+str(chan[ii+1])+str(chan[ii+2])+str(chan[ii+3]))
        time.sleep(1)
        print "Fa"
