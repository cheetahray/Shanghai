#------------------------------------------------------------------------
#Code Written by: Albert Lin from Noise Kitchen
#Current Project: noisekitchen.tw
#------------------------------------------------------------------------

#Step 1: Import necessary libraries 
#------------------------------------------------------------------------
import sys
import motor_lib
#------------------------------------------------------------------------

#Step 2: read the direction and number of steps; if steps are 0 exit 
#------------------------------------------------------------------------
try: 
    direction = sys.argv[1]
    laps = float(sys.argv[2])
    rpm= float(sys.argv[3])
    at= float(sys.argv[4])
    dt= float(sys.argv[5])
except:
    laps = 0

motor_lib.io1.wiringPiSetupGpio()
motor1 = motor_lib.stepperdriver(6400,13,19)
motor1.rotate(direction, laps,rpm,at,dt)
