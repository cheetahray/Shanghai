from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import argparse

parser = argparse.ArgumentParser(description='Print number')
parser.add_argument("-i", "--ip", type=int, help="echo the number you use here")
args = parser.parse_args()
 
m = PyMouse()
k = PyKeyboard()

def combine(god):
    global k
    k.press_key(k.control_key)
    k.type_string(god)
    k.release_key(k.control_key)
    time.sleep(1)

def ktype_string(god,rest):
    global k
    k.type_string(god)
    k.tap_key(k.enter_key)
    time.sleep(rest)

#39 24 23 14
#while True: 
#for ii in range(31,36):
time.sleep(1.5)

ktype_string('ping 192.168.12.114',3)
combine('c')
ktype_string('ping 192.168.12.126',3)
combine('c')
ktype_string('ping 192.168.12.133',3)
combine('c')
ktype_string('ping 192.168.12.134',3)
combine('c')
ktype_string('ping 192.168.12.153',3)
combine('c')
ktype_string('ping 192.168.12.154',3)
combine('c')

for ii in range(46,53):
    #pass
    #ktype_string('ping 192.168.12.' + str(ii),3)
    #combine('c')
    '''
    time.sleep(1)
    ktype_string('5',73)
    '''
    '''
    ktype_string('ssh pi@192.168.12.' + str(ii),6)
    ktype_string('chu67925',2)
    ktype_string('sudo kill -9 $(ps -ef | grep hl | awk \'{print $2}\')', 1)
    ktype_string('exit',1)
    '''
    '''
    ktype_string('ssh pi@192.168.12.' + str(ii),1)
    ktype_string('raspberry',2)
    ktype_string('amixer cset numid=6 70% 70%', 1)
    ktype_string('exit',1)
    '''
    '''
    ktype_string('ssh pi@192.168.12.' + str(ii),6)
    ktype_string('raspberry',2)
    ktype_string('sudo reboot', 1)
    ktype_string('exit',1)
    ktype_string('ssh pi@192.168.12.1' + str(ii),6)
    ktype_string('chu67925',2)
    ktype_string('sudo reboot', 1)
    ktype_string('exit',1)
    '''
    '''
    ktype_string('cd ShanghaiB',1)
    ktype_string('sudo sftp albert@192.168.12.95', 2)
    ktype_string('chu67925', 2)
    ktype_string('cd Shanghai',1)
    ktype_string('get soundfontsender.py',1)
    ktype_string('get artnet.py', 1)
    ktype_string('get ledmatrix.py', 1)
    ktype_string('get fourty.py', 1)
    ktype_string('exit',1)
    '''
    '''
    ktype_string('ssh pi@192.168.12.' + str(ii),1)
    ktype_string('chu67925',2)
    ktype_string('sudo touch /etc/ethers',1)
    ktype_string('chu67925',2)
    ktype_string('sudo chmod 777 /etc/ethers',1)
    ktype_string('arp -n | grep eth0 | awk {\'print $1, $3\'} > /etc/ethers',1)
    ktype_string('cat /etc/ethers',1)
    ktype_string('sudo arp -f',1)
    ktype_string('exit',1)
    '''
