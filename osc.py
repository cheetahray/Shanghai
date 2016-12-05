import OSC

cc = OSC.OSCClient()
cc.connect(('192.168.12.249', 7000))   # localhost, port 57120

def click(msg):
    global cc
    oscmsg = OSC.OSCMessage()
    print "%s" % ("/track13/connect")
    oscmsg.setAddress("%s" % ("/track13/connect") )
    oscmsg.append(1)
    cc.send(oscmsg)

click(1)
	


