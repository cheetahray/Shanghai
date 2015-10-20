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

def rayanim(r,g,b,bright,animpos,animtime):
    anim.brightcolor( bright, (b,r,g) )
    if anim.lastIndex+1 > animpos :
        for i in range(anim.lastIndex,animpos-1,-1):
            anim.gogo(rayIndex = i)
            anim.lastIndex = i
            anim.run(threaded = True, joinThread = False)
            time.sleep(animtime)
    elif anim.lastIndex+1 < animpos:
        for i in range(anim.lastIndex,animpos+1,1):
            anim.gogo(rayIndex = i)
            anim.lastIndex = i
            anim.run(threaded = True, joinThread = False)
            time.sleep(animtime)

try:
    #run the animation
    rayanim(255,0,0,255,20,0.5)
    time.sleep(0.5)
    rayanim(0,255,0,150,5,0.5)
    time.sleep(0.5)
    rayanim(0,0,255,75,15,0.5)
    time.sleep(0.5)
    rayanim(255,255,255,30,0,0.5)
except KeyboardInterrupt:
    #Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.update()
