import bibliopixel
#Load driver for the AllPixel
from bibliopixel.drivers.LPD8806 import *
from bibliopixel.led import *
import bibliopixel.colors as colors
import math
from bibliopixel.animation import *
from threading import Thread

class ColorWipe(BaseMatrixAnim, Thread):
    """Fill the dots progressively along the strip."""
    __lastpos = 0
    __sleeptime = 0.0
    __animpos = 0
    __interrupt = False
    __width = 2

    def __init__(self, led, start=0, end=-1, width=2):
        super(ColorWipe, self).__init__(led, start, end)
        self.__width = width
        Thread.__init__(self)
        self._led.all_off()

    def step(self, amt = 1):
        amt = 2

    def rayanim(self,r,g,b,bright,animpos,animtime):
        self._bright = bright 
        self._color = colors.color_scale((b,r,g), self._bright)
        self.__sleeptime = animtime / self.__width / ( math.fabs(self.__lastpos - animpos) + 4 )
        self.__animpos = animpos
        for i in range(self.__lastpos):
            self._led.drawRect(0,0,self.__width,i+1, self._color) #self._led.set(i, self._color)
        self.__interrupt = True

    def run(self):
        while True:
            diff = self.__lastpos - self.__animpos
            if diff > 0 :
                for i in range(self.__lastpos, self.__animpos-1, -1):
                    self._led.drawRect(0,i,self.__width,i+1, (0,0,0) ) #self._led.setOff(i) 
                    BaseMatrixAnim.run(self, threaded = True, joinThread = False)
                    self.__lastpos = i
                    if self.__interrupt == True:
                        break
                    else:
                        time.sleep(self.__sleeptime)
                self.__interrupt = False    
            elif diff < 0:
                for i in range(self.__lastpos, self.__animpos+1, 1):
                    self._led.drawRect(0,i,self.__width,i+1, self._color)  #self._led.set(i, self._color) 
                    BaseMatrixAnim.run(self, threaded = True, joinThread = False)
                    self.__lastpos = i
                    if self.__interrupt == True:
                        break
                    else:
                        time.sleep(self.__sleeptime)
                self.__interrupt = False
            else:
                time.sleep(0.05)            

coords = [
    [9,10],
    [8,11],
    [7,12],
    [6,13],
    [5,14],
    [4,15],
    [3,16],
    [2,17],
    [1,18],
    [0,19]
]

#causes frame timing information to be output
bibliopixel.log.setLogLevel(bibliopixel.log.CRITICAL)
#set number of pixels & LED type here
driver = DriverLPD8806(num = 20)
#load the LEDStrip class
#led = LEDStrip(driver, threadedUpdate = True)
led = LEDMatrix(driver, width = len(coords[0]), height = len(coords), coordMap = coords, threadedUpdate = True)

#load channel test animation
anim = ColorWipe(led, width = len(coords[0]) )
anim.start()

try:
    #run the animation
    anim.rayanim(255,0,0,255,10,0.8)
    time.sleep(0.7)
    anim.rayanim(255,255,255,40,0,3.0)
except KeyboardInterrupt:
    #Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.update()

