import time
import socket
from struct import *

port = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(44,63):
    port.sendto(pack('BB', 249, 3), ("192.168.12." + str(i), 5005) )
    time.sleep(0.01)
    