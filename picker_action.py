import motor_lib
import time
#------------------------------------------------------------------------


motor_lib.io1.wiringPiSetupGpio()
motor1 = motor_lib.stepperdriver(6400,13,19)#picker_motor

motor1.picker_action(100)

#motor_lib.io1.delayMicroseconds(800000)
#motor1.picker_stopsound()
#motor_lib.io1.delayMicroseconds(800000)
time.sleep(1)
motor1.picker_action(100)
#motor_lib.io1.delayMicroseconds(800000)
#motor1.picker_stopsound()
#motor_lib.io1.delayMicroseconds(800000)

#motor1.picker_action(300)
#motor_lib.io1.delayMicroseconds(800000)
#motor1.picker_stopsound()
#motor_lib.io1.delayMicroseconds(800000)

#motor1.picker_action(300)
#motor_lib.io1.delayMicroseconds(800000)
#motor1.picker_stopsound()
#motor_lib.io1.delayMicroseconds(800000)
