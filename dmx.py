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
    for ii in range(0,52,4):         
        mydmx.setChannel(1, chan[ii]) # set DMX channel 1 to full
        mydmx.setChannel(2, chan[ii+1]) # set DMX channel 2 to 128
        mydmx.setChannel(3, chan[ii+2]) # set DMX channel 3 to 0
        mydmx.setChannel(4, chan[ii+3])
        mydmx.render()
    time.sleep(8)
