#------------------------------------------------------------------------
#Code Written by: Albert Lin from Noise Kitchen
#Current Project: noisekitchen.tw
#------------------------------------------------------------------------
#------------------------------------------------------------------------
import stepper_class
import socket
#------------------------------------------------------------------------
tp=[]

stepper_class.io1.wiringPiSetupGpio()
motor1 = stepper_class.stepperdriver(12800,19,26)
motor2 = stepper_class.stepperdriver(12800,20,21)

UDP_IP = "192.168.11.78"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(("", UDP_PORT))

iftsh = False
iftph = False
iftvh = False
#while False == iftsh or False == iftph or False == iftvh:
while False:
    data, addr = sock.recvfrom(1024)
    if data == "tsh":
        print("String back home") #change here
        if True: #change here
            sock.sendto(data + "e", (UDP_IP, UDP_PORT))
            iftsh = True
    elif data == "tph":
        print("picker back home") #change here
        if True: #change here
            sock.sendto(data + "e", (UDP_IP, UDP_PORT))
            iftph = True 
    elif data == "tvh":
        print("velocity back home") #change here
        if True: #change here
            sock.sendto(data + "e", (UDP_IP, UDP_PORT))
            iftvh = True

pickspeed = 250
pickvelocity = 127
ifpickclock = True
motorspeed = 0
while True:
    data, addr = sock.recvfrom(1024)
    #print (data)
    if data[0] == 't':
        if data[1:] == "sl":
            print("turn string loose") #change here
        elif data[1:] == "st": 
            print("turn string tight") #change here
        elif data[1:] == "ss":
            print("stop turn string") #change here
    elif data[0] == 'a':
        if data[1] == 'v':
            pickvelocity = int(data[2:])
        elif data[1] == 'c':
            ifpickclock = True
            pickspeed = int(data[2:])
        elif data[1] == 'w':
            ifpickclock = False
            pickspeed = int(data[2:])
        print("use picker speed = {0}, picker velocity = {1}, is picker clockwise? {2}".format(pickspeed,pickvelocity,ifpickclock)) #change here
    elif data[0] == 'm':
        if data[1] == 'r':
            tpindex = int(data[2:]) 
            tp.append("Remember pitch {0} position".format( tpindex ) ) #change here
            print( tp[ len(tp)-1 ] ) #change here
        elif data[1] == 'h':
            print("left hand move high") #change here
        elif data[1] == 'l':
            print("left hand move low") #change here
        elif data[1] == 's':
            print("left hand stop move") #change here
        else:
            vindex = data.index('v') 
            motorspeed = int(data[vindex+1:]) 
            print("Use {0} motor speed to get pitch {1} position from tp[ int(data[1:vindex]) ]".format( motorspeed, int(data[1:vindex]) ) ) #change here

#motor1.gh(-1,20,0.1,6)
#motor2.gh(1,2,0.1,16)

#motor1.moveto(tp[1],300,20,20)
#stepper_class.io1.delayMicroseconds(500000)
#motor1.moveto(tp[3],300,20,20)
#stepper_class.io1.delayMicroseconds(500000)
#motor1.moveto(tp[5],300,20,20)
#stepper_class.io1.delayMicroseconds(500000)
#motor1.moveto(tp[2],300,20,20)
#stepper_class.io1.delayMicroseconds(500000)
#motor1.moveto(tp[4],300,20,20)
#stepper_class.io1.delayMicroseconds(500000)
#motor1.moveto(tp[6],200,30,30)
#stepper_class.io1.delayMicroseconds(500000)
#motor1.moveto(tp[0],300,20,20)
#stepper_class.io1.delayMicroseconds(500000)
#motor1.moveto(0,300,20,20)
