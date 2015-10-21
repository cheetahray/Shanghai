import bibliopixel
#Load driver for the AllPixel
from bibliopixel.drivers.LPD8806 import *
from bibliopixel.led import *
import bibliopixel.colors as colors
import math
from bibliopixel.animation import BaseStripAnim

class ColorWipe(BaseStripAnim, Thread):
    """Fill the dots progressively along the strip."""
    __rayIndex = 0
    lastIndex = 0

    def __init__(self, led, start=0, end=-1):
        super(ColorWipe, self).__init__(led, start, end)
        self.start()

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

    def rayanim(self,r,g,b,bright,animpos,animtime):
        self.brightcolor( bright, (b,r,g) )
        diff = self.lastIndex + 1 - animpos
        animtime = animtime / math.fabs(diff)
                    
    def run(self):
        while True:
            if diff > 0 :
                for i in range(self.lastIndex,animpos-1,-1):
                    self.gogo(rayIndex = i)
                    self.run(threaded = True, joinThread = False)
                    time.sleep(animtime)
                self.lastIndex = animpos
                time.sleep(0.25)
            elif diff < 0:
                for i in range(self.lastIndex,animpos+1,1):
                    self.gogo(rayIndex = i)
                    self.run(threaded = True, joinThread = False)
                    time.sleep(animtime)
                self.lastIndex = animpos
                time.sleep(0.25)
            else:
                time.sleep(0.05)            

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
    anim.rayanim(255,0,0,255,20,3.0)
    time.sleep(15)
    anim.rayanim(0,255,0,150,5,1.5)
    time.sleep(15)
    anim.rayanim(0,0,255,75,15,0.7)
    time.sleep(15)
    anim.rayanim(255,255,255,30,0,0.5)
    time.sleep(15)
except KeyboardInterrupt:
    #Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.update()

