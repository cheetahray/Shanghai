import pysimpledmx
mydmx = pysimpledmx.DMXConnection("/dev/ttyUSB0")
mydmx.setChannel(1, 255) # set DMX channel 1 to full
mydmx.setChannel(2, 255) # set DMX channel 2 to 128
mydmx.setChannel(3, 0) # set DMX channel 3 to 0
mydmx.setChannel(4, 255)
mydmx.render()
