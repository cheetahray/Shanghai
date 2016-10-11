from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import argparse

parser = argparse.ArgumentParser(description='Print number')
parser.add_argument("-i", "--ip", type=int, help="echo the number you use here")
args = parser.parse_args()
 
m = PyMouse()
k = PyKeyboard()
#39 24 23 14
for ii in range(14,13,-1):
    time.sleep(1)
    k.type_string('ssh pi@192.168.12.' + str(ii) + "\n")
    time.sleep(6)
    k.type_string('raspberry\n')
    time.sleep(2)
    k.type_string('sudo chmod 777 /etc/ethers\n')
    time.sleep(1)
    k.type_string('arp -n | grep eth0 | awk {\'print $1, $3\'} > /etc/ethers\n')
    time.sleep(1)
    k.type_string('cat /etc/ethers\n')
    time.sleep(1)
    k.type_string('sudo arp -f\n')
    time.sleep(1)
    k.type_string('exit\n')
