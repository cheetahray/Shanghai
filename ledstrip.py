import bibliopixel
#Load driver for the AllPixel
from bibliopixel.drivers.LPD8806 import *
from bibliopixel.led import *
import bibliopixel.colors as colors
import math
from bibliopixel.animation import *
from threading import Thread
import RPi.GPIO as GPIO

class ColorWipe(BaseStripAnim, Thread):
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
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(31, GPIO.OUT)
        GPIO.setup(32, GPIO.OUT)
        GPIO.setup(33, GPIO.OUT)
        GPIO.setup(35, GPIO.OUT)
        GPIO.setup(37, GPIO.OUT)
        GPIO.setup(38, GPIO.OUT)
        GPIO.setup(40, GPIO.OUT)
        p31 = GPIO.PWM(31, 50)
        p32 = GPIO.PWM(32, 50)
        p33 = GPIO.PWM(33, 50)
        p35 = GPIO.PWM(35, 50)
        p37 = GPIO.PWM(37, 50)
        p38 = GPIO.PWM(38, 50)
        p40 = GPIO.PWM(40, 50)
        p31.start(0)
        p32.start(100)
        p33.start(0)
        p35.start(0)
        p37.start(0)
        p38.start(0)
        p40.start(0)
        Thread.start(self)

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
                    self.__lastpos = i
                    if self.__interrupt == True:
                        break
                    else:
                        BaseStripAnim.run(self, threaded = True, joinThread = False)
                        time.sleep(self.__sleeptime)
                        BaseStripAnim.stopThread(self)
                self.__interrupt = False    
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
            else:
                time.sleep(0.01)            

