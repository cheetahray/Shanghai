from OSC import *
import sys
import types

import stepper_class

stepper_class.io1.wiringPiSetupGpio()
motor1 = stepper_class.stepperdriver(12800,5,6)
motor2 = stepper_class.stepperdriver(12800,27,22)
motor3 = stepper_class.stepperdriver(12800,13,19)
stepper_class.io1.pinMode(26,1)  
stepper_class.io1.digitalWrite(26,0)

server = OSCServer( ("0.0.0.0", 2222) )#This has to be the IP of the RaspberryPi on the network

#def handle_timeout(self):
#    print ("Pi is waiting")

#This here is just to do something while the script recieves no information....
#server.handle_timeout = types.MethodType(handle_timeout, server)

def off_all(path, tags, args, source):
    motor1.stop_motor()
    motor2.stop_motor()
    motor3.stop_motor()
    stepper_class.io1.digitalWrite(26,0)
    
def turn_light(path, tags, args, source):
    motor1.turn_motor(-1,60)
    motor2.turn_motor(1,60)
    motor3.revr_motor(1,60,25)
    stepper_class.io1.digitalWrite(26,1)

#These are all the add-ons that you can name in the TouchOSC layout designer (you can set the values and directories)
server.addMsgHandler("/on", turn_light)
server.addMsgHandler("/off", off_all)
#The way that the MSG Handlers work is by taking the values from set accessory, then it puts them into a function
#The function then takes the values and separates them according to their class (args, source, path, and tags)

try:
    while True:
        server.handle_request()
        
except KeyboardInterrupt:
    print "\nClosing OSCServer."
    server.close()
    print "Waiting for Server-thread to finish"
    motor1.join()

sys.exit(0)
