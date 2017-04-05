import OSC

cc = OSC.OSCClient()
cc.connect(('192.168.12.249', 7000))   # localhost, port 57120
#cc.connect(('127.0.0.1', 6666))
def click(msg):
    global cc
    tracknum = "34"
    oscmsg = OSC.OSCMessage()
    print "%s" % ("/track" + tracknum + "/connect")
    #print "%s" % ("/cue")
    oscmsg.setAddress("%s" % ("/track" + tracknum + "/connect") )
    #oscmsg.setAddress("%s" % ("/cue") )
    oscmsg.append(1)
    cc.send(oscmsg)

click(1)
	


