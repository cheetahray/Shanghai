import OSC
import random
import time

cc = OSC.OSCClient()
dd = OSC.OSCClient()
cc.connect(('127.0.0.1', 7110))   # localhost, port 57120
dd.connect(('127.0.0.1', 4808))

def stop(unit):
    global cc
    oscmsg = OSC.OSCMessage()
    oscstr = "/stop"
    oscmsg.setAddress(oscstr)
    oscmsg.append(unit)
    print oscmsg
    cc.send(oscmsg)

def click(unit, pos, speed):
    global cc
    #unit = random.randint(5,5)
    oscmsg = OSC.OSCMessage()
    oscstr = "/motor"
    oscmsg.setAddress(oscstr)
    #pos = random.randint(120,120)
    #speed = random.randint(200,300)
    acc = speed#random.randint(1000,2000)
    oscmsg.append(unit)
    oscmsg.append(pos)
    oscmsg.append(speed)
    oscmsg.append(acc)
    print oscmsg
    cc.send(oscmsg)

#while True:
for unit in range(1,25):
    click(unit, 0, 0)
    time.sleep(0.1)
#stop(6)