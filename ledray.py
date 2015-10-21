import bibliopixel
#causes frame timing information to be output
bibliopixel.log.setLogLevel(bibliopixel.log.CRITICAL)

#Load driver for the AllPixel
from bibliopixel.drivers.LPD8806 import *
#set number of pixels & LED type here 
driver = DriverLPD8806(num = 20)

#load the LEDStrip class
from bibliopixel.led import *
led = LEDStrip(driver, threadedUpdate = True)

#load channel test animation
from strip_animations import *
import bibliopixel.colors as colors
anim = ColorWipe(led)

import math

def rayanim(r,g,b,bright,animpos,animtime):
    anim.brightcolor( bright, (b,r,g) )
    diff = anim.lastIndex + 1 - animpos
    animtime = animtime / math.fabs(diff)
    if diff > 0 :
        for i in range(anim.lastIndex,animpos-1,-1):
            anim.gogo(rayIndex = i)
            anim.run(threaded = True, joinThread = False)
            time.sleep(animtime)
        anim.lastIndex = animpos
        time.sleep(0.2)
    elif diff < 0:
        for i in range(anim.lastIndex,animpos+1,1):
            anim.gogo(rayIndex = i)
            anim.run(threaded = True, joinThread = False)
            time.sleep(animtime)
        anim.lastIndex = animpos
        time.sleep(0.2)
try:
    #run the animation
    rayanim(255,0,0,255,20,3.0)
    rayanim(0,255,0,150,5,1.5)
    rayanim(0,0,255,75,15,0.7)
    rayanim(255,255,255,30,0,0.5)
except KeyboardInterrupt:
    #Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.update()
