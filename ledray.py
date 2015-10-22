import bibliopixel
#Load driver for the AllPixel
from bibliopixel.drivers.LPD8806 import *
from bibliopixel.led import *
import bibliopixel.colors as colors
import math
from bibliopixel.animation import BaseStripAnim
from threading import Thread

class ColorWipe(BaseStripAnim, Thread):
    """Fill the dots progressively along the strip."""
    __lastpos = 0
    __sleeptime = 0.0
    __animpos = 0
    __interrupt = False

    def __init__(self, led, start=0, end=-1):
        super(ColorWipe, self).__init__(led, start, end)
        Thread.__init__(self)
        self._led.all_off()

    def step(self, amt = 1):
        amt = 2

    def rayanim(self,r,g,b,bright,animpos,animtime):
        self._bright = bright 
        self._color = colors.color_scale((b,r,g), self._bright)
        self.__sleeptime = animtime / ( math.fabs(self.__lastpos - animpos) + 4 )
        self.__animpos = animpos
        for i in range(self.__lastpos):
            self._led.set(i, self._color)
        self.__interrupt = True

    def run(self):
        while True:
            diff = self.__lastpos - self.__animpos
            if diff > 0 :
                for i in range(self.__lastpos, self.__animpos-1, -1):
                    self._led.setOff(i) 
                    BaseStripAnim.run(self, threaded = True, joinThread = False)
                    self.__lastpos = i
                    if self.__interrupt == True:
                        break
                    else:
                        time.sleep(self.__sleeptime)
                self.__interrupt = False    
            elif diff < 0:
                for i in range(self.__lastpos, self.__animpos+1, 1):
                    self._led.set(i, self._color) 
                    BaseStripAnim.run(self, threaded = True, joinThread = False)
                    self.__lastpos = i
                    if self.__interrupt == True:
                        break
                    else:
                        time.sleep(self.__sleeptime)
                self.__interrupt = False
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
anim.start()
try:
    #run the animation
    anim.rayanim(255,0,0,255,20,0.8)
    time.sleep(0.7)
    anim.rayanim(255,255,255,40,0,3.0)
except KeyboardInterrupt:
    #Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.update()

