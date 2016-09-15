#------------------------------------------------------------------------
#Code Written by: Albert Lin from Noise Kitchen
#Current Project: noisekitchen.tw
#------------------------------------------------------------------------
#------------------------------------------------------------------------
import motor_lib
import socket
import os
import commands
#------------------------------------------------------------------------
#tp=[]

#==Mapping type of string  S==A==T==B  <===>  0==1==2==3  

whattype = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
1, 1, 1, 1, 1, 1, 1, 2, 2, 2,
2, 2, 2, 3, 3, 3, 3, 3, 2, 1,
1, 1, 0, 0, 0, 1, 1, 2, 2, 3,
3, 3, 3, 2, 2, 2, 2, 2, 2, 1,
1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
0, 0, 0, 0, 0, 0, 0, 1, 2, 0
, 0, 1, 2, 0]



motor_lib.io1.wiringPiSetupGpio()
motor1 = motor_lib.stepperdriver(6400,13,19)#picker_motor (step_per_rotate,pulse,director)
motor2 = motor_lib.stepperdriver(6400,5,6)#volacity_motor
motor3 = motor_lib.pwmMotorDriver(18,22,17)#string_turning_motor(p_pin,in_b_pin,in_a_pin)
motor4 = motor_lib.tstepdriver()#slider_motor


ips = commands.getoutput("/sbin/ifconfig | grep -iA2 \"eth0\" | grep -i \"inet\" | grep -iv \"inet6\" | " +
                         "awk {'print $2'} | sed -ne 's/addr\://p'")
iplist = ips.split(".")
whoami = int(iplist[3])
UDP_IP = iplist[0] + "." + iplist[1] + "." + iplist[2] + "." + str(whoami-100)
whoami = whoami - 101
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(("", UDP_PORT))

soffset = [1910, 1910, 1910, 1910]   # S,A,T,B
           #1      #2      #3      #4      #5      #6      #7      #8      #9      #10
voffset = [5.9849, 5.8849, 5.8849, 6.4849, 6.1849, 5.8849, 5.8849, 5.8849, 6.3849, 5.9849, #10
           5.8849, 5.8849, 5.7849, 5.6849, 5.8849, 5.8849, 5.8849, 5.6349, 6.3749, 5.9849, #20
           6.5849, 5.9849, 6.4349, 6.42,   5.82,   5.62,   5.82,   6.32,   5.7849, 5.8849, #30
           5.8849, 5.8849, 5.8849, 5.8849, 5.6849, 5.8849, 5.9849, 5.8049, 6.1049, 6.12,   #40
           5.82,   5.62,   5.82,   5.8849, 5.9947, 5.9149, 5.8849, 5.7849, 6.1549, 5.3849, #50
           5.6849, 5.8849, 5.8849, 5.8849, 5.6849, 5.7849, 5.8849, 5.8849, 5.8849, 5.8849, #60
           6.1849, 5.9849, 5.7849, 5.8849, 6.0849, 5.9849, 5.8348, 5.8348, 6.4849, 5.8947, #70
           5.8348, 5.5848, 5.8349, 5.82]
poffset=[0.016, 0.016, 0.016, 0.014] #[0.0165, 0.017, 0.016, 0.014]
stop_range = [581, 581, 581, 552] #[585, 583, 581, 552]
v_back_range_array = [0.165, 0.165, 0.175, 0.3]
v_back_range = v_back_range_array[whattype[whoami]]


print("I am" + str(whoami))
motor4.set_attrib()
while True:
    motor1.p_direction = -1
    iftsh = False
    iftph = False
    iftvh = False
    while False == iftsh or False == iftph or False == iftvh:
    #while False:
        data, addr = sock.recvfrom(1024)
        if data == "tsh":
            print("String back home") #tsh change here
    
            srs = motor4.t_zero(soffset[whattype[whoami]])
            if srs == True: #tshe change here
                sock.sendto(data + "e", (UDP_IP, UDP_PORT))
                iftsh = True
        elif data == "tph":
            print("picker back home") #tph change here
            motor2.rotate(1, 7, 60, 0, 0)
            motor1.rotate(1, 0.3, 30, 0, 0)#(direction, laps, rpm, at, dt)
            prs = motor1.gh(-1,60,0.975,26)#gh(self, direction, rpm, offset_rev, ps_pin)
            if prs == True: #tphe change here
                sock.sendto(data + "e", (UDP_IP, UDP_PORT))
                iftph = True
    
        elif data == "tvh":
            print("velocity back home") #tvh change here
    
            print (voffset[whoami])
    
            vrs = motor2.gh(-1,120,voffset[whoami],21)
            motor1.rotate(1, poffset[whattype[whoami]], 120, 0, 0)
            if vrs ==True: #tvhe change here
                sock.sendto(data + "e", (UDP_IP, UDP_PORT))
                iftvh = True
    
    pickspeed = 250
    pickvelocity = 127
    ifpickclock = True
    motorspeed = 0
    while True:
        data, addr = sock.recvfrom(1024)
        if data == 'Home':
            print (data)
            break
        elif data[0] == 't':
            if data[1:] == "sl":
                #child_pid = os.fork()
                #if child_pid == 0:
                print("turn string loose") #tsl change here
                motor3.rotate(1,10)
                #    os._exit(0)
            elif data[1:] == "st": 
                #child_pid = os.fork()
                #if child_pid == 0:
                print("turn string tight") #tst change here
                motor3.rotate(-1,10)
                #    os._exit(0)
            elif data[1:] == "ss":
                #child_pid = os.fork()
                #if child_pid == 0:
                print("stop turn string") #tss change here
                motor3.stop()
                #    os._exit(0)
        elif data[0] == 'a':
            if data[1] == 'a':
                if motor1.p_direction == -1:
                    rpm_vback = 240
                else:
                    rpm_vback = 60
    
                motor1.picker_action(170) #speed define by rpm, 
                print "aa"
            elif data[1] == 's':
                motor1.picker_stopsound(stop_range[whattype[whoami]]) #stop_range
                print "as"
            elif data[1] == 'r':
                motor1.picker_release_stop(stop_range[whattype[whoami]]) #stop_range
                print "ar"
    
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
            elif data[1] == 't':
                table_addr = repr(int(data[2:]))
                print "motor move to " + table_addr
                motor4.mv(table_addr)
                 #   os._exit(0)
            else:
                vindex = data.index('v') 
                motorspeed = int(data[vindex+1:]) 
                #child_pid = os.fork()
                #if child_pid == 0:
                print("Use {0} motor speed to get pitch {1} position".format( motorspeed, int(data[1:vindex]) ) ) #m1v127 change here
                motor4.mt(int(data[1:vindex]), motorspeed)
                #    os._exit(0)
    
