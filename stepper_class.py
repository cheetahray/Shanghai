#------------------------------------------------------------------------
#Code Written by: Albert Lin from Noise Kitchen
#------------------------------------------------------------------------
import wiringpi2 as io1
from threading import Thread
import time

class stepperdriver(Thread):
    __direction = 0
    __rpm = 60

    def __init__(self,steps_per_rev=12800,p_pin=19,d_pin=26):
        super(stepperdriver, self).__init__()
        self.steps_per_rev = steps_per_rev
        self.p_pin = p_pin
        self.d_pin = d_pin
        self.motor_address = 0
        self.revr = 0
        io1.pinMode(self.d_pin,1)
        io1.pinMode(self.p_pin,1)
        self.start()
        
#------------------------------------------------------------------------
#----------------rotate by laps------------------------------------------
#------------------------------------------------------------------------        
    def rotate(self, direction, laps, rpm, at, dt):
#------------------------------------------------------------------------
#set counter and speed control variables
#------------------------------------------------------------------------
        steps = int(float(laps) * self.steps_per_rev) 
        rpm=float(rpm)
        at=float(at)
        dt=float(dt) 
        direction = int(direction)
        at_steps=int(steps*(at/100))
        dt_steps=int(steps*(dt/100))
        peak_steps=steps - at_steps - dt_steps
        at_WaitTime = int(1000000 / self.steps_per_rev - 8)  #waitTime controls speed
        peak_WaitTime = int(1000000 / (rpm / 60 * self.steps_per_rev) - 8)
        time_Range = (at_WaitTime - peak_WaitTime)
        time_Split = (1 + time_Range) * time_Range / 2 
        at_split_point = int(at_steps / time_Split )
        dt_split_point = int(dt_steps / time_Range )
#------------------------------------------------------------------------
#Set direction of rotation
#------------------------------------------------------------------------
        if direction == -1:
            io1.digitalWrite(self.d_pin,0)
        elif direction == 1:
            io1.digitalWrite(self.d_pin,1)
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#Zero Step Counter
#------------------------------------------------------------------------
        StepCounter = 0
        split_Counter = 0
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#Turn the motor by send pulse
#------------------------------------------------------------------------
        split_Counter = at_split_point 
        adtCounter = 1
        # Start Acceleration loop
        while StepCounter < at_steps:
            #turning the gpio off and on tells the driver to take one step
            io1.digitalWrite(self.p_pin,0)
            if split_Counter == StepCounter:
                if at_WaitTime > peak_WaitTime:
                    at_WaitTime -= 1
                split_Counter = at_split_point * adtCounter + split_Counter 
                adtCounter += 1
            io1.delayMicroseconds(at_WaitTime)        
            io1.digitalWrite(self.p_pin,1)
            StepCounter += 1
        self.motor_address = self.motor_address + direction * StepCounter
        StepCounter = 0
        
        # Start peak loop        
        while StepCounter < peak_steps:
            #turning the gpio off and on tells the driver to take one step
            io1.digitalWrite(self.p_pin,0)
            io1.delayMicroseconds(peak_WaitTime)
            io1.digitalWrite(self.p_pin,1)
            StepCounter += 1
        self.motor_address = self.motor_address + direction * StepCounter
        StepCounter = 0
        
        adtCounter = dt_split_point
        # Start Deceleration loop
        while StepCounter < dt_steps:
            #turning the gpio off and on tells the driver to take one step
            io1.digitalWrite(self.p_pin,0)
            if adtCounter == StepCounter:
                at_WaitTime += 1
                adtCounter += dt_split_point
            io1.delayMicroseconds(at_WaitTime)
            io1.digitalWrite(self.p_pin,1)
            StepCounter += 1
        self.motor_address = self.motor_address + direction * StepCounter   
        print io1.micros()

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
    def gh(self, direction, rpm, offset_rev, ps_pin):
#------------------------------------------------------------------------
#set speed control variables
#------------------------------------------------------------------------
        rpm=float(rpm)
        offset_rev=float(offset_rev)
        peak_WaitTime = int(1000000 / (rpm / 60 * self.steps_per_rev) - 8)
        direction = int(direction)
        offset_steps = int(offset_rev * self.steps_per_rev)
#------------------------------------------------------------------------
#set speed control variables
#------------------------------------------------------------------------
        self.ps_pin = int(ps_pin)
        io1.pinMode(self.ps_pin,0)
#------------------------------------------------------------------------
#Set direction of rotation
#------------------------------------------------------------------------
        if direction == -1:
            io1.digitalWrite(self.d_pin,0)
        elif direction == 1:
            io1.digitalWrite(self.d_pin,1)
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#Zero Step Counter
#------------------------------------------------------------------------
        StepCounter = 0
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#Turn the motor by send pulse
#------------------------------------------------------------------------
        while io1.digitalRead(self.ps_pin):
            io1.digitalWrite(self.p_pin,0)
            io1.delayMicroseconds(peak_WaitTime)        
            io1.digitalWrite(self.p_pin,1)
            StepCounter += 1
        StepCounter = 0
        # Start offset loop        
        io1.delayMicroseconds(50)
        
        if direction == -1:
            io1.digitalWrite(self.d_pin,1)
        elif direction == 1:
            io1.digitalWrite(self.d_pin,0)

        # Start offset loop        
        while StepCounter < offset_steps:
            io1.digitalWrite(self.p_pin,0)
            io1.delayMicroseconds(peak_WaitTime)        
            io1.digitalWrite(self.p_pin,1)
            StepCounter += 1

        StepCounter = 0
        self.motor_address = 0

        
        
#------------------------------------------------------------------------
#----------------rotate by steps-----------------------------------------
#------------------------------------------------------------------------        
    def stepper(self, direction, steps, rpm, at, dt):
#------------------------------------------------------------------------
#set counter and speed control variables
#------------------------------------------------------------------------
        rpm=float(rpm)
        steps = float(steps)
        at=float(at)
        dt=float(dt) 
        direction = int(direction)
        at_steps=int(steps*(at/100))
        dt_steps=int(steps*(dt/100))
        peak_steps=steps - at_steps - dt_steps
        at_WaitTime = int(1000000 / self.steps_per_rev - 8)  #waitTime controls speed
        peak_WaitTime = int(1000000 / (rpm / 60 * self.steps_per_rev) - 8)
        time_Range = (at_WaitTime - peak_WaitTime)
        time_Split = (1 + time_Range) * time_Range / 2 
        at_split_point = int(at_steps / time_Split )
        dt_split_point = int(dt_steps / time_Range )
        print at_steps
        print dt_steps
#------------------------------------------------------------------------
#Set direction of rotation
#------------------------------------------------------------------------
        if direction == -1:
            io1.digitalWrite(self.d_pin,0)
        elif direction == 1:
            io1.digitalWrite(self.d_pin,1)
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#Zero Step Counter
#------------------------------------------------------------------------
        StepCounter = 0
        split_Counter = 0
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#Turn the motor by send pulse
#------------------------------------------------------------------------
        split_Counter = at_split_point 
        adtCounter = 1
        # Start Acceleration loop
        while StepCounter < at_steps:
            #turning the gpio off and on tells the driver to take one step
            io1.digitalWrite(self.p_pin,0)
            if split_Counter == StepCounter:
                if at_WaitTime > peak_WaitTime:
                    at_WaitTime -= 1
                split_Counter = at_split_point * adtCounter + split_Counter 
                adtCounter += 1
            io1.delayMicroseconds(at_WaitTime)        
            io1.digitalWrite(self.p_pin,1)
            StepCounter += 1
            self.motor_address = self.motor_address + direction
        StepCounter = 0
        
        # Start peak loop        
        while StepCounter < peak_steps:
            #turning the gpio off and on tells the driver to take one step
            io1.digitalWrite(self.p_pin,0)
            io1.delayMicroseconds(peak_WaitTime)
            io1.digitalWrite(self.p_pin,1)
            StepCounter += 1
            self.motor_address = self.motor_address + direction
        StepCounter = 0
        
        adtCounter = dt_split_point
        # Start Deceleration loop
        while StepCounter < dt_steps:
            #turning the gpio off and on tells the driver to take one step
            io1.digitalWrite(self.p_pin,0)
            if adtCounter == StepCounter:
                at_WaitTime += 1
                adtCounter += dt_split_point
            io1.delayMicroseconds(at_WaitTime)
            io1.digitalWrite(self.p_pin,1)
            StepCounter += 1
            self.motor_address = self.motor_address + direction
        print io1.micros()

#------------------------------------------------------------------------
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#----------------rotate by steps-----------------------------------------
#------------------------------------------------------------------------        
    def moveto(self, t_position, rpm, at, dt):
        if t_position > self.motor_address:
            direction = 1
        else:
            direction = -1
        steps = abs(self.motor_address - t_position) 
        self.stepper(direction, steps, rpm, at, dt)
#------------------------------------------------------------------------

    def turn_motor(self, direction, rpm):
        self.__direction = direction
        self.__rpm = rpm

    def revr_motor(self, direction, rpm, revr):
        self.revr = self.steps_per_rev * revr / 100
        self.__direction = direction
        self.__rpm = rpm

    def stop_motor(self):
        self.revr = 0
        self.__direction = 0
        
    def run(self):
        while True:
            if 0 != self.__direction:
                direction = self.__direction
                rpm = self.__rpm
#------------------------------------------------------------------------
#set speed control variables
#------------------------------------------------------------------------
                rpm=float(rpm)
                peak_WaitTime =  1 / (rpm / 60 * self.steps_per_rev) 
                #peak_WaitTime = int(1000000 / (rpm / 60 * self.steps_per_rev) - 8)
                direction = int(direction)
                
#------------------------------------------------------------------------
#set speed control variables
#------------------------------------------------------------------------
#------------------------------------------------------------------------
#Set direction of rotation
#------------------------------------------------------------------------
                if direction == -1:
                    io1.digitalWrite(self.d_pin,0)
                    if self.revr > 0:
                        revrbool = True
                elif direction == 1:
                    io1.digitalWrite(self.d_pin,1)
                    if self.revr > 0:
                        revrbool = False
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#Zero Step Counter
#------------------------------------------------------------------------
                StepCounter = 0
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#Turn the motor by send pulse
#------------------------------------------------------------------------
                while True:
                    io1.digitalWrite(self.p_pin,0)
                    time.sleep(peak_WaitTime)
                    io1.digitalWrite(self.p_pin,1)
                    StepCounter += 1
                    if self.revr == StepCounter:
                        io1.digitalWrite(self.d_pin, revrbool)
                        revrbool = not revrbool
                        StepCounter = 0
                    if 0 == self.__direction: 
                        break
                    
                self.motor_address = StepCounter

                StepCounter = 0
            else:
                time.sleep(0.01)
