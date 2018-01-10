import OSC
import random

cc = OSC.OSCClient()
cc.connect(('192.168.11.134', 7730))   # localhost, port 57120
#cc.connect(('127.0.0.1', 6666))
def click(msg):
    global cc
    oscmsg = OSC.OSCMessage()
    oscstr = "/motor"
    oscmsg.setAddress(oscstr)
    pos = random.randint(0,128)
    speed = random.randint(50,200)
    print("%s %d %d %d" % (oscstr, 1, pos, speed))
    oscmsg.append(1)
    oscmsg.append(pos)
    oscmsg.append(speed)
    cc.send(oscmsg)

click(1)
	


