#------------------------------------------------------------------------
#Code Written by: Albert Lin from Noise Kitchen
#------------------------------------------------------------------------
import wiringpi2 as io1
import serial
import time

class stepperdriver(object):
    def __init__(self,steps_per_rev=12800,p_pin=19,d_pin=26):
        self.steps_per_rev = steps_per_rev
        self.p_pin = p_pin
        self.d_pin = d_pin
        self.p_direction = -1 #assign picker direction 
        self.motor_address = 0
        io1.pinMode(self.d_pin,1)
        io1.pinMode(self.p_pin,1)
        
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
        try:
            at_split_point = int(at_steps / time_Split )
        except ZeroDivisionError:
            at_split_point = 0
        try:    
            dt_split_point = int(dt_steps / time_Range )
        except ZeroDivisionError:
            dt_split_point = 0
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
        return True
    
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
        # Start offset loop
        while io1.digitalRead(self.ps_pin):
            io1.digitalWrite(self.p_pin,0)
            io1.delayMicroseconds(peak_WaitTime)        
            io1.digitalWrite(self.p_pin,1)
            StepCounter += 1
        io1.delayMicroseconds(50)
        
        if direction == -1:
            io1.digitalWrite(self.d_pin,1)
        elif direction == 1:
            io1.digitalWrite(self.d_pin,0)

        # Start offset loop        
        StepCounter = 0
        while StepCounter < offset_steps:
            io1.digitalWrite(self.p_pin,0)
            io1.delayMicroseconds(peak_WaitTime)        
            io1.digitalWrite(self.p_pin,1)
            StepCounter += 1

        StepCounter = 0
        self.motor_address = 0
        return True
        
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
        try:
            at_split_point = int(at_steps / time_Split )
        except ZeroDivisionError:
            at_split_point = 0
        try:    
            dt_split_point = int(dt_steps / time_Range )
        except ZeroDivisionError:
            dt_split_point = 0
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
        return True

#------------------------------------------------------------------------
#------------------------------------------------------------------------        
#------------------------------------------------------------------------
    def moveto(self, t_position, rpm, at, dt):
        if t_position > self.motor_address:
            direction = 1
        else:
            direction = -1
        steps = abs(self.motor_address - t_position) 
        self.stepper(direction, steps, rpm, at, dt)
        return True
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#------------------------------------------------------------------------        
#------------------------------------------------------------------------
    def picker_action(self, rpm):
        print self.p_direction
        steps = self.steps_per_rev / 24.5
        self.stepper(self.p_direction, steps, rpm, 10, 10)
        self.p_direction = self.p_direction * -1
        return True
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#------------------------------------------------------------------------        
#------------------------------------------------------------------------
    def picker_stopsound(self, stop_range):
        rpm = 200
        #steps = self.steps_per_rev / 8  - self.steps_per_rev / 27 / 2 - 130
        self.stepper(self.p_direction * -1, stop_range, rpm, 0, 20)
        return True
#------------------------------------------------------------------------

#------------------------------------------------------------------------
#------------------------------------------------------------------------        
#------------------------------------------------------------------------
    def picker_release_stop(self, stop_range):
        rpm = 100
        self.stepper(self.p_direction , stop_range, rpm, 40, 0)
        return True
#------------------------------------------------------------------------


##------------------------------------------------------------------------
##------------------------------------------------------------------------
##                   DC Motor control class
##------------------------------------------------------------------------
##------------------------------------------------------------------------  

class pwmMotorDriver(object):
    def __init__(self,p_pin,d1_pin,d2_pin):
        self.__speed = 0
        self.__p_pin = p_pin
        self.__d1_pin = d1_pin
        self.__d2_pin = d2_pin
        io1.pinMode(self.__d1_pin,1)
        io1.pinMode(self.__d2_pin,1)
        io1.pinMode(self.__p_pin,1)
        io1.softPwmCreate(self.__p_pin,0,100)
        io1.digitalWrite(self.__d1_pin,1)
        io1.digitalWrite(self.__d2_pin,1)
    
    def rotate(self, direction, speed):
        if direction == 1:
            io1.digitalWrite(self.__d1_pin,0)
            io1.digitalWrite(self.__d2_pin,1)
            io1.softPwmWrite(self.__p_pin,int(speed))
        if direction == -1:
            io1.digitalWrite(self.__d1_pin,1)
            io1.digitalWrite(self.__d2_pin,0)
            io1.softPwmWrite(self.__p_pin,int(speed))
    def stop(self):
        io1.digitalWrite(self.__d1_pin,1)
        io1.digitalWrite(self.__d2_pin,1)
        io1.softPwmWrite(self.__p_pin,0)
        

class tstepdriver(object):
    def __init__(self):
        self.port = serial.Serial("/dev/ttyAMA0", baudrate=57600, timeout=3.0)
        
    def set_attrib(self):
        ts_cmd=[]
        ts_cmd.append('#AAC2')
        ts_cmd.append('#AAR0')
        ts_cmd.append('#ACG70')
        ts_cmd.append('#ACM0')
        ts_cmd.append('#AHC1600')
        ts_cmd.append('#APD1')
        ts_cmd.append('#APL36857')
        ts_cmd.append('#ARC3000')
        ts_cmd.append('#ASL0')
        ts_cmd.append('#ASR10')
        ts_cmd.append('#ASV400')
        ts_cmd.append('#AVL78000')
        ts_cmd.append('#ASD')
        ts_cmd.append('#AMA')
        for i, ts_val in enumerate(ts_cmd):
            print 'Send to T-Step--> ' + ts_val
            self.port.write(ts_val + "\r\n")
            rcv=self.readline(self.port)
            print rcv

        self.port.flush()

    def readline(self,port):
            rv = ""
            while True:
                    ch = port.read()
                    rv += ch
                    if ch=='\n' or ch=='':
                            return rv
                    
    
    def t_zero(self, offset_len):
        #self.port.write("#ASL2\r\n")
        #io1.delayMicroseconds(1000)
        self.port.write("#AOS-1\r\n")
        io1.delayMicroseconds(1000000)
        while True:    
            self.port.write("#AMS\r\n")
            rcv=self.readline(self.port)
            print rcv
            if rcv == "*AMS0\r\n":
                break
        self.port.write("#APM" + repr(offset_len) + "\r\n")
        
        while True:    
            self.port.write("#AMS\r\n")
            io1.delayMicroseconds(9000)
            rcv=self.readline(self.port)
            print rcv
            if rcv == "*AMS0\r\n":
                break 
        self.port.write("#AZP\r\n")
        io1.delayMicroseconds(1000)
        #self.port.write("#ASL1\r\n")
        self.port.flush()
        print "String Zero OK"
        return True
    
    def ms(self):
        self.port.write("#ASM\r\n")
        self.port.flush()
        print "Stop OK"
        return True
    
    def mh(self):
        self.port.write("#AVM400\r\n")
        self.port.flush()
        print "Moving High"
        return True
    
    def ml(self):
        self.port.write("#AVM-400\r\n")
        self.port.flush()
        print "Moving Low"
        return True
    
    def mt(self, target_pitch, m_speed):
        self.port.write("#AVL" + repr(m_speed) + "\r\n")
        io1.delayMicroseconds(8000)
        self.port.write("#ATA" + repr(target_pitch) + "\r\n")
        io1.delayMicroseconds(8000)
        self.port.write("#AVL" + self.speed + "\r\n")
        self.port.flush()
        #while True:    
        #    self.port.write("#AMS\r\n")
        #    rcv=self.readline(self.port)
        #    print rcv
        #    if rcv == "*AMS0\r\n":
        #        print "Table Move OK"
                #self.port.write("#AVL64000\r\n")
        return True
    def mv(self, target_pitch):
        self.port.write("#ATA" + repr(target_pitch) + "\r\n")
        io1.delayMicroseconds(8000)
        self.port.flush()
        return True

    def mr(self, pitch_index):
        while True:    
            self.port.write("#ACP\r\n")
            rcv=self.readline(self.port)
            if rcv[0:4] == "*ACP":
                print "Current Position:" + rcv
                rindex = rcv.index("\r")
                #self.port.write("#ATS" +  repr(pitch_index) + "," + rcv[4:rindex] + "\r\n")
                #self.port.flush()
                return  rcv[4:rindex]    
    
