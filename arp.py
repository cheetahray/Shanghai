from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
import argparse

parser = argparse.ArgumentParser(description='Print number')
parser.add_argument("-i", "--ip", type=int, help="echo the number you use here")
args = parser.parse_args()
 
m = PyMouse()
k = PyKeyboard()
mylist = [115,146,151,15,46,51]

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
'''
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
'''
for ii in range(1,255):
    #pass
    ktype_string('ping 192.168.0.' + str(ii),3)
    combine('c')
    '''
    time.sleep(1)
    ktype_string('5',73)
    '''
    '''
    if ii > 100:
        ktype_string('ssh pi@192.168.12.' + str(ii),6)
        ktype_string('chu67925',2)
        ktype_string('sudo kill -9 $(ps -ef | grep hl | awk \'{print $2}\')', 1)
        ktype_string('exit',1)
    else:    
        ktype_string('ssh pi@192.168.12.' + str(ii),1)
        ktype_string('raspberry',2)
        ktype_string('amixer cset numid=6 70% 70%', 1)
        ktype_string('exit',1)
    '''    

    '''
    ktype_string('ssh pi@192.168.12.' + str(ii),6)
    ktype_string('raspberry',2)
    '''
    '''    
    if False:
        ktype_string('sudo vi /etc/rc.local', 1)
        ktype_string(':20,20d', 1)
        ktype_string(':wq', 1)
        ktype_string('sudo vi /etc/profile', 1)
        ktype_string(':$', 1)
        ktype_string('o', 1)
        ktype_string('pd -nogui -audiodev 4 /home/pi/Desktop/pi_main.pd &', 1)
        k.tap_key(k.escape_key)
        ktype_string(':wq', 1)
        ktype_string('cd /home/pi/.config/syncthing/', 1)
        ktype_string('rm key.pem cert.pem', 1)
    elif False:    
        ktype_string('sudo vi config.xml', 1)
        ktype_string(':%s/UOFQ5CD-YI5SSQL-OJHYVAD-FMLGCTH-QL3ESS7-KPEZH2V-OEQRIRQ-X2RXPA3/VLBSPRN-X34X7RG-ABZYFAZ-Z4PC3KG-MZ6XKTY-M4EDQ7M-IBJHNDY-L34ENAM', 1)
        ktype_string(':%s/raspberrypi/Pi6', 1)
        ktype_string(':wq', 1)
        ktype_string('sudo reboot',1)
    else:
        ktype_string(' ',1)
        ktype_string('ps aux | grep pi_main',1)
        ktype_string('ps aux | grep sync',1)
        ktype_string('sudo shutdown -h now',1)
    '''
    '''
    else:    
        ktype_string('ssh pi@192.168.12.' + str(ii),6)
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
