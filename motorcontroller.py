#------------------------------------------------------------------------
#Code Written by: Albert Lin from Noise Kitchen
#Current Project: noisekitchen.tw
#------------------------------------------------------------------------
#------------------------------------------------------------------------
import motor_lib
import socket
import os
#------------------------------------------------------------------------
#tp=[]

motor_lib.io1.wiringPiSetupGpio()
motor1 = motor_lib.stepperdriver(6400,20,16)#picker_motor
motor2 = motor_lib.stepperdriver(6400,24,23)#volacity_motor
motor3 = motor_lib.pwmMotorDriver(17,27,22)#string_turning_motor
motor4 = motor_lib.tstepdriver()#slider_motor


UDP_IP = "192.168.12.78"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(("", UDP_PORT))

iftsh = False
iftph = False
iftvh = False
while False == iftsh or False == iftph or False == iftvh:
#while False:
    data, addr = sock.recvfrom(1024)
    if data == "tsh":
        print("String back home") #tsh change here
        srs = motor4.t_zero(640)
        if srs == True: #tshe change here
            sock.sendto(data + "e", (UDP_IP, UDP_PORT))
            iftsh = True
    elif data == "tph":
        print("picker back home") #tph change here
        motor2.rotate(-1, 3, 60, 0, 0)
        prs = motor1.gh(1,10,0.014,21)
        if prs == True: #tphe change here
            sock.sendto(data + "e", (UDP_IP, UDP_PORT))
            iftph = True
    elif data == "tvh":
        print("velocity back home") #tvh change here
        vrs = motor2.gh(1,60,2.45,25)
        if vrs ==True: #tvhe change here
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
            #child_pid = os.fork()
            #if child_pid == 0:
            print("turn string loose") #tsl change here
            motor3.rotate(1,40)
            #    os._exit(0)
        elif data[1:] == "st":
            #child_pid = os.fork()
            #if child_pid == 0:
            print("turn string tight") #tst change here
            motor3.rotate(-1,40)
            #    os._exit(0)
        elif data[1:] == "ss":
            #child_pid = os.fork()
            #if child_pid == 0:
            print("stop turn string") #tss change here
            motor3.stop()
            #    os._exit(0)
    elif data[0] == 'a':
        if data[1] == 'v':
            pickvelocity = int(data[2:])
        elif data[1] == 'a':
            motor1.picker_action(200)
        elif data[1] == 's':
            motor1.picker_stopsound()
    elif data[0] == 'm':
        if data[1] == 'r':
            tpindex = int(data[2:])
            print "record pitch address" + str(tpindex)
            rrs = motor4.mr(tpindex)
            sock.sendto(str(rrs), (UDP_IP, UDP_PORT)) #tp.append(rrs)
        elif data[1] == 'h':
            #child_pid = os.fork()
            #if child_pid == 0:
            print("left hand move high") #mh change here
            motor4.mh()
             #   os._exit(0)
        elif data[1] == 'l':
            #child_pid = os.fork()
            #if child_pid == 0:
            print("left hand move low") #ml change here
            motor4.ml()
             #   os._exit(0)
        elif data[1] == 's':
            #child_pid = os.fork()
            #if child_pid == 0:
            print("left hand stop move") #ms change here
            motor4.ms()
             #   os._exit(0)
        else:
            vindex = data.index('v')
            motorspeed = int(float(data[vindex+1:]) / 127.0 * 64000)
            #child_pid = os.fork()
            #if child_pid == 0:
            print("Use {0} motor speed to get pitch {1} position".format( motorspeed, int(data[1:vindex]) ) ) #m1v127 change here
            #    os._exit(0)
