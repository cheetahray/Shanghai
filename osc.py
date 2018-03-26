import OSC
import random
import time

cc = OSC.OSCClient()
dd = OSC.OSCClient()
cc.connect(('127.0.0.1', 7110))   # localhost, port 57120
dd.connect(('127.0.0.1', 4808))
def click(msg):
    global cc
    unit = random.randint(1,1)
    oscmsg = OSC.OSCMessage()
    oscstr = "/motor"
    oscmsg.setAddress(oscstr)
    pos = random.randint(0,127)
    speed = random.randint(200,300)
    acc = random.randint(1000,2000)
    oscmsg.append(unit)
    oscmsg.append(pos)
    oscmsg.append(speed)
    oscmsg.append(acc)
    print oscmsg
    cc.send(oscmsg)

def double(msg):
    global dd
    unit = random.randint(24,24)
    oscmsg = OSC.OSCMessage()
    oscstr = "/motor"
    oscmsg.setAddress(oscstr)
    pos = random.randint(0,127)
    speed =random.randint(0,4)
    oscmsg.append(unit)
    oscmsg.append(pos)
    oscmsg.append(speed)
    oscmsg.append(random.randint(0,4))
    print oscmsg
    dd.send(oscmsg)

while True:
    click(1)
    time.sleep(0.5)
    #double(1)
    time.sleep(0.5)


