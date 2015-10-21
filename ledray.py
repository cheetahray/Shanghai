import bibliopixel
#Load driver for the AllPixel
from bibliopixel.drivers.LPD8806 import *
from bibliopixel.led import *
import bibliopixel.colors as colors
import math
from bibliopixel.animation import BaseStripAnim

class ColorWipe(BaseStripAnim):
    """Fill the dots progressively along the strip."""
    __rayIndex = 0
    lastIndex = 0

    def __init__(self, led, start=0, end=-1):
        super(ColorWipe, self).__init__(led, start, end)

    def brightcolor(self, bright, color):
        self._bright = bright
        self._color = colors.color_scale(color, self._bright)

    def gogo(self, rayIndex = 0): 
        self.__rayIndex = rayIndex
        self._led.all_off()
        #self._led.update()

    def step(self, amt = 1):
        for i in range(self.__rayIndex):
            self._led.set(i, self._color)

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

#causes frame timing information to be output
bibliopixel.log.setLogLevel(bibliopixel.log.CRITICAL)
#set number of pixels & LED type here
driver = DriverLPD8806(num = 20)
#load the LEDStrip class
led = LEDStrip(driver, threadedUpdate = True)
#load channel test animation
anim = ColorWipe(led)
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
