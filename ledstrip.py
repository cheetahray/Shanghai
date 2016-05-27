import bibliopixel
#Load driver for the AllPixel
from bibliopixel.drivers.LPD8806 import *
from bibliopixel.led import *
import bibliopixel.colors as colors
import math
from bibliopixel.animation import *
from threading import *

class ColorWipe(BaseStripAnim, Thread):
    """Fill the dots progressively along the strip."""
    __lastpos = 0
    __sleeptime = 0.0
    __animpos = 0
    __interrupt = False
    __width = 2
    __cv = None
    __isartnet = False
    
    def __del__(self):
        self._led.all_off()
        self._led.update()
    
    def __init__(self, led, start=0, end=-1, width=2):
        super(ColorWipe, self).__init__(led, start, end)
        self.__width = width
        Thread.__init__(self)
        self._led.all_off()
        self.__cv = Condition()
        self._led.setMasterBrightness(255)
        Thread.start(self)

    def step(self, amt = 1):
        pass

    def cleargb(self):
        self._led.all_off()
        self._led.update()

    def drawone(self,x,y,r,g,b):
        r += 30
        g += 30
        b += 30
        if(r > 255):
           r = 255 
        if(g > 255):
           g = 255 
        if(b > 255):
           b = 255 
        self._led.setRGB(y,b,r,g)
        if False == self.__isartnet:
            #self.__cv.acquire()
            #self.__cv.notify()
            #self.__cv.release()
            BaseStripAnim.stopThread(self)
            BaseStripAnim.run(self, fps = 25, threaded = True, joinThread = False)
            self.__isartnet = True
        
    def rayanim(self,r,g,b,bright,animpos,animtime):
        self._bright = bright 
        self._color = colors.color_scale((b,r,g), self._bright)
        self.__sleeptime = animtime / ( math.fabs(self.__lastpos - animpos) + 4 )
        self.__animpos = animpos
        for i in range(self.__lastpos):
            self._led.set(i, self._color)
        self.__isartnet = False
        self.__interrupt = True
        self.__cv.acquire()
        self.__cv.notify()
        self.__cv.release()

    def run(self):
        while True:
            diff = self.__lastpos - self.__animpos
            if diff > 0 :
                for i in range(self.__lastpos, self.__animpos-1, -1):
                    self._led.setOff(i) 
                    self.__lastpos = i
                    if self.__interrupt == True:
                        break
                    else:
                        BaseStripAnim.run(self, threaded = True, joinThread = False)
                        time.sleep(self.__sleeptime)
                        BaseStripAnim.stopThread(self)
                self.__interrupt = False    
                BaseStripAnim.stopThread(self)
            elif diff < 0:
                for i in range(self.__lastpos, self.__animpos+1, 1):
                    self._led.set(i, self._color) 
                    self.__lastpos = i
                    if self.__interrupt == True:
                        break
                    else:
                        BaseStripAnim.run(self, threaded = True, joinThread = False)
                        time.sleep(self.__sleeptime)
                        BaseStripAnim.stopThread(self)
                self.__interrupt = False
                BaseStripAnim.stopThread(self)
            #elif True == self.__isartnet:
                #BaseStripAnim.run(self, sleep = 0.04, threaded = True, joinThread = False)
                #time.sleep(0.04)
                #BaseStripAnim.stopThread(self)
            else:
                self.__cv.acquire()
                self.__cv.wait() #time.sleep(0.01)            
                self.__cv.release()

#causes frame timing information to be output
#log.setLogLevel(log.CRITICAL)
#set number of pixels & LED type here
#driver = DriverLPD8806(num = 20)
#load the LEDStrip class
#led = LEDStrip(driver, threadedUpdate = True)
#load channel test animation
#anim = ColorWipe(led) 

#anim.rayanim(255,255,255,255,20,20)
