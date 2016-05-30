print("PWM Function test")
pearlpwm = 8
pwm.setup(pearlpwm,1000,1023);
pwm.start(pearlpwm);
pwm.setup(1,1000,1023);
pwm.start(1);
pwm.setup(2,1000,1023);
pwm.start(2);
pwm.setup(3,1000,1023);
pwm.start(3);
pwm.setup(4,1000,1023);
pwm.start(4);
pwm.setup(5,1000,1023);
pwm.start(5);
pwm.setup(6,1000,1023);
pwm.start(6);
pwm.setup(7,1000,1023);
pwm.start(7);
    
local r=512;
local flag=1;
tmr.alarm(2,500,1,function()
    pwm.setduty(pearlpwm,r);
    print (r)
    if flag==1 then 
        r=r-50;        
        if r<0 then 
            flag=0 
            r=0 
        end
    else
        r= r+50;    
        if r>1023 then 
            flag=1 
            r=1023 
        end
    end
end)
