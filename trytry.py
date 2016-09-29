import threading
import socket
from struct import *
import time

port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      
DELAY = 1.2

def raymap(value, istart, istop, ostart, ostop):
    wierd = ostart + (ostop - ostart) * (value - istart) / (istop - istart); 
    print wierd
    return wierd
	
#241
#threading.Timer( 0.11, port.sendto, [pack('BH', 127, 323), ("192.168.12.241", 6666)]).start()
#threading.Timer( 0.12, port.sendto, [pack('BH', 143, 231), ("192.168.12.241", 6666)]).start()
#threading.Timer( 1, port.sendto, [pack('BH', 159, 15), ("192.168.12.241", 6666)]).start() #38 midtom 15~100
#threading.Timer( 2, port.sendto, [pack('BH', 175, 15), ("192.168.12.241", 6666)]).start() #39 lowtom 15~100
#threading.Timer( 0.14, port.sendto, [pack('BH', 191, 231), ("192.168.12.241", 6666)]).start()
#threading.Timer( 3, port.sendto, [pack('BH', 207, 20), ("192.168.12.241", 6666)]).start() #42 snare side 20~64
#threading.Timer( 4, port.sendto, [pack('BH', 223, 13), ("192.168.12.241", 6666)]).start() #41 snare 13~25
#threading.Timer( 5, port.sendto, [pack('BH', 239, 40), ("192.168.12.241", 6666)]).start() #36 Bass drum 40~300

#242
#threading.Timer( 0.11, port.sendto, [pack('BH', 127, 23), ("192.168.12.242", 6666)]).start()
#threading.Timer( 6, port.sendto, [pack('BH', 143, 15), ("192.168.12.242", 6666)]).start()
#threading.Timer( 7, port.sendto, [pack('BH', 159, 13), ("192.168.12.242", 6666)]).start()
#threading.Timer( 8, port.sendto, [pack('BH', 175, 17), ("192.168.12.242", 6666)]).start() 
#threading.Timer( 9, port.sendto, [pack('BH', 191, 13), ("192.168.12.242", 6666)]).start() 
threading.Timer( 0.1, port.sendto, [pack('BH', 207, 300), ("192.168.12.242", 6666)]).start() #44 Pedal Hi-Hat
#threading.Timer( 11, port.sendto, [pack('BH', 223, 17), ("192.168.12.242", 6666)]).start() 
#threading.Timer( 12, port.sendto, [pack('BH', 239, 300), ("192.168.12.242", 6666)]).start() 

#243
#threading.Timer( 0.11, port.sendto, [pack('BH', 127, 23), ("192.168.12.243", 6666)]).start()
#threading.Timer( 6, port.sendto, [pack('BH', 143, 15), ("192.168.12.243", 6666)]).start() #40 Floor tom 15~100
#threading.Timer( 7, port.sendto, [pack('BH', 159, 13), ("192.168.12.243", 6666)]).start() #49 Ride 13~50
#threading.Timer( 8, port.sendto, [pack('BH', 175, 17), ("192.168.12.243", 6666)]).start() #48 Ride Side 17~70
#threading.Timer( 9, port.sendto, [pack('BH', 191, 13), ("192.168.12.243", 6666)]).start() #46 Crush side 13~30
#threading.Timer( 10, port.sendto, [pack('BH', 207, 10), ("192.168.12.243", 6666)]).start() #47 Crush 10~64
#threading.Timer( 11, port.sendto, [pack('BH', 223, 17), ("192.168.12.243", 6666)]).start() #45 Open Hi-Hat 17~30
#threading.Timer( 12, port.sendto, [pack('BH', 239, 300), ("192.168.12.243", 6666)]).start() 

time.sleep(2)
