import pysimpledmx
import time
mydmx = pysimpledmx.DMXConnection("/dev/ttyUSB0")
chan = [ 0  , 0  , 0  , 0  ,
         0  , 0  , 0  , 255,
         0  , 0  , 255, 0  ,
         0  , 0  , 255, 255,
         0  , 255, 0  , 0  ,
         0  , 255, 0  , 255,
         0  , 255, 255, 0  ,
         0  , 255, 255, 255,
         255, 0  , 0  , 0  ,
         255, 0  , 0  , 255,
         255, 0  , 255, 0  ,
         255, 0  , 255, 255,
         255, 255, 0  , 0  ,
         255, 255, 0  , 255,
         255, 255, 255, 0  ,
         255, 255, 255, 255 ]
while True:
    jj = 1
    for ii in range(0,64,4):         
        mydmx.setChannel(jj, chan[ii]) # set DMX channel 1 to full
        mydmx.setChannel(jj+1, chan[ii+1]) # set DMX channel 2 to 128
        mydmx.setChannel(jj+2, chan[ii+2]) # set DMX channel 3 to 0
        mydmx.setChannel(jj+3, chan[ii+3])
        mydmx.render()
        time.sleep(5)
