import bibliopixel
#causes frame timing information to be output
bibliopixel.log.setLogLevel(bibliopixel.log.DEBUG)

#Load driver for the AllPixel
from bibliopixel.drivers.LPD8806 import *
#set number of pixels & LED type here 
driver = DriverLPD8806(num = 20)

#load the LEDStrip class
from bibliopixel.led import *
led = LEDStrip(driver)

#load channel test animation
#from bibliopixel.animation import StripChannelTest
from strip_animations import *
#anim = StripChannelTest(led)
#anim = Rainbow(led)
anim = RainbowCycle(led)
#anim = LarsonRainbow(led)

try:
	#run the animation
    anim.run()
except KeyboardInterrupt:
	#Ctrl+C will exit the animation and turn the LEDs offs
    led.all_off()
    led.update()
