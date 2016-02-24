import motor_lib
#------------------------------------------------------------------------


motor_lib.io1.wiringPiSetupGpio()
motor1 = motor_lib.stepperdriver(6400,13,19)#picker_motor
motor2 = motor_lib.stepperdriver(6400,5,6)#volacity_motor

motor2.rotate(1, 6, 120, 0, 0)
motor1.rotate(1, 0.1, 120, 0, 0)
prs = motor1.gh(-1,120,0.975,26)
