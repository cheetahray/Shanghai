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
jj = 0
while True:
    for ii in range(1,65,4):         
        mydmx.setChannel(ii, chan[jj]) # set DMX channel 1 to full
        mydmx.setChannel(ii+1, chan[jj+1]) # set DMX channel 2 to 128
        mydmx.setChannel(ii+2, chan[jj+2]) # set DMX channel 3 to 0
        mydmx.setChannel(ii+3, chan[jj+3])    
    mydmx.render()
    if jj >= 60:
        jj = 0
    else:
        jj += 4
    time.sleep(10)
