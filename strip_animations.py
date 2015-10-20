from bibliopixel import LEDStrip
import bibliopixel.colors as colors
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
        
