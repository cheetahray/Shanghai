import serial
import OSC

ser = serial.Serial('COM3', 38400, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
cc = OSC.OSCClient()
cc.connect(('127.0.0.1', 7730))   # localhost, port 57120

def click(msg):
    global cc
    oscmsg = OSC.OSCMessage()
    oscstr = "/motor"
    oscmsg.setAddress(oscstr)
    motonum = 25
    pos = 64
    speed = 50
    print("%s %d %d %d" % (oscstr, motonum, pos, speed))
    oscmsg.append(motonum)
    oscmsg.append(pos)
    oscmsg.append(speed)
    cc.send(oscmsg)

def WindSpeed(one, two):
    _speed = two & 0x7F
    _16 = (one << 8) + two
    _dmx = _16 >> 7
    print _dmx, _speed
    return _dmx, _speed

def checksum(one, two, three):
    print one, two, one+two, three
    if one + ord(s[1]) == ord(s[2]):
        return True
    else:
        return False

speed = 0
dmx = 0

while True:
    idx = 0
    ss = ser.read()
    while idx < len(ss):
        if True == checksum(ord(ss[idx]), ord(ss[idx+1]), ord(ss[idx+2])):
            dmx, speed = WindSpeed(ord(ss[idx]), ord(ss[idx+1]))
            idx+=3
        else:
            idx+=1