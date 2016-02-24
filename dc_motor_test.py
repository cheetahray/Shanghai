import time
import motor_lib

motor_lib.io1.wiringPiSetupGpio()

dc_motor_1 = motor_lib.pwmMotorDriver(18,17,22)

while True:
    ts_cmd = raw_input('Direction--> ')
    if ts_cmd == "c":
        dc_motor_1.rotate(1,10)
    if ts_cmd == "w":
        dc_motor_1.rotate(-1,10)
    if ts_cmd == "s":
        dc_motor_1.stop()
