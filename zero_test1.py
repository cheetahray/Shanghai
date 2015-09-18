#------------------------------------------------------------------------
#Code Written by: Albert Lin from Noise Kitchen
#Current Project: noisekitchen.tw
#------------------------------------------------------------------------
#------------------------------------------------------------------------
import stepper_class
import socket
#------------------------------------------------------------------------
tp=[]
tp.append(12800)
tp.append(25600)
tp.append(38400)
tp.append(51200)
tp.append(64000)
tp.append(76800)
tp.append(89600)

UDP_IP = "192.168.11.27"
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(("127.0.0.1", UDP_PORT))

data, addr = sock.recvfrom(1024)
if data == "tsh":
    print("壓弦 回 Home")
    if True: #如果壓弦回 Home 成功
        sock.sendto(data + "e", (UDP_IP, UDP_PORT))
elif data == "tph":
    print("picker 回 Home")
    if True: #如果 picker 回 Home 成功
        sock.sendto(data + "e", (UDP_IP, UDP_PORT))
elif data == "tvh":
    print("velocity 回 Home")
    if True: #如果 velocity 回 Home 成功
        sock.sendto(data + "e", (UDP_IP, UDP_PORT))
elif data == "tsl":    
    print("弦轉鬆")
elif data == "tst":
    print("弦轉緊")
elif data == "tss":
    print("弦轉停")

stepper_class.io1.wiringPiSetupGpio()
motor1 = stepper_class.stepperdriver(12800,19,26)
motor2 = stepper_class.stepperdriver(12800,20,21)

motor1.gh(-1,20,0.1,6)
motor2.gh(1,2,0.1,16)

motor1.moveto(tp[1],300,20,20)
stepper_class.io1.delayMicroseconds(500000)
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
motor1.moveto(0,300,20,20)
