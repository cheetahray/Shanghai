num=109

cfg={}
 cfg.ssid="ssfar_" .. num
 cfg.pwd="nk888888"
 --cfg.ssid="uucar_X"
 --cfg.pwd="noisekitchen"
 wifi.ap.config(cfg)

if adc.force_init_mode(adc.INIT_ADC)
then 
    node.restart()
end
        
cfg2={
  ip = "192.168.13." .. num,
  netmask = "255.255.255.0",
  gateway = "192.168.13.254"
}
 wifi.sta.config("bellclass","noisekitchen")
 wifi.sta.setip(cfg2)

wifi.setmode(wifi.STATIONAP)

wifi.eventmon.register(wifi.eventmon.STA_CONNECTED, 
function(T) 
 print("CONNECT")
 wificonnect = true
 if(wificonnect) then
    srv = net.createConnection(net.UDP, 0)
    srv:connect(9999,"192.168.13.200")
 end 
end)

wifi.eventmon.register(wifi.eventmon.STA_DISCONNECTED, 
function(T) 
 print("DISCONNECTED")
 wificonnectnum = wificonnectnum+1
 if(wificonnectnum>2) then
    wifi.setmode(wifi.SOFTAP)
    wifi.eventmon.unregister(wifi.eventmon.STA_CONNECTED)
 end
end)

wificonnect = false;
wificonnectnum = 0;
pin_servo = 1
r_a=2 ; r_b=3
l_a=5 ; l_b=6
pin_shoot = 4
led_udp=7 ; led_shot=8
n=0;n2=0

PWM_freq = 50
servo_pulse_lenght = 0

--sv_pwm = {71 ,74,77,80,83,86,89,92,96,100,104,108,112,116,120}
--sv_pwm = {71 ,68,65,62,59,56,53,50,47,44,41,38,35,28,25}
sv_pwm = {25 ,28,32,34,36,38,40,42,44,46,48,50,52,54,56}

-- Setup servo PWM generator
pwm.setup(pin_servo, PWM_freq, servo_pulse_lenght) 
pwm.start(pin_servo) 

i_pwm = {0,375,400,450,550,675,800,1023}
c_pwm = {0,375,400,435,485,600,800,1023}
dif_s = {0,70,140,280,490,770,980,1120}

for i = 2,3 do
     pwm.setup(i,PWM_freq,0)
     pwm.start(i)
end
for i = 5,6 do
     pwm.setup(i,PWM_freq,0)
     pwm.start(i)
end

gpio.mode(pin_shoot, gpio.OUTPUT)
gpio.write(pin_shoot, gpio.LOW)
gpio.mode(led_udp, gpio.OUTPUT)
gpio.write(led_udp, gpio.LOW)
gpio.mode(led_shot, gpio.OUTPUT)
gpio.write(led_shot, gpio.LOW)


function smallmouse()
    num=adc.read(0)
    --print(num)
    if(num>10)  then 
        --print(num)
        n=n+1
        n2=0
        if(n>2) then 
            gpio.write(led_shot, gpio.HIGH)
            if(wificonnect) then 
                srv:send("@")
                --print("!")
            end
            print("@")
            n=0 
        end 
    else    
        n2=n2+1
        if(n2>10) then 
            gpio.write(led_shot, gpio.LOW)
            n=0 
        end 
       
    end
end
        

function turnwheel(b,pwm,lr)
  if(lr) then
    p_a = l_a
    p_b = l_b
    --print("leftwheel")
  else
    p_a = r_a
    p_b = r_b
    --print("rightwheel")
  end
  if(b) then
        pwmoutput(p_a,0)
        pwmoutput(p_b,pwm)
        --print("clockwise pwm is ",pwm)
    else
        pwmoutput(p_a,pwm)
        pwmoutput(p_b,0)
        --print("anti-clockwise pwm is ",pwm)
    end
end


function pwmoutput(p,i)
    print(p..";"..i)
    pwm.setduty(p, i)
    --print((tmr.now()-inittime)/1000)
end

s=net.createServer(net.UDP)
s:on("receive", function(s, c)
    --inittime = tmr.now()
    --print( c )
    --print( bit.band(c, 7) ) --level for forwards/backwards
    --print( bit.isset(c, 3) ) -- bool for forwards/backwards
    --print( bit.rshift(bit.band(c, 127), 4) ) -- level for left/right 
    --print( bit.isset(c, 7)  ) -- bool for left/right
    if not tmr.alarm(0, 100, tmr.ALARM_SINGLE, 
        function() 
        end) 
    then
    else
    
        if( bit.rshift(bit.band(c, 240), 4) == 8 ) then
            if(bit.band(c, 15)==0) then
                gpio.write(pin_shoot, gpio.LOW)
                print("shoot off")
            else
                servo_pulse_lenght = sv_pwm[bit.band(c, 15)]
                print(bit.band(c, 15)..";servo:" .. sv_pwm[bit.band(c, 15)])
                pwm.setduty(pin_servo, servo_pulse_lenght)
                gpio.write(pin_shoot, gpio.HIGH)
            end

        else
            --print( c )
            if(bit.band(c, 7)== 0) then
            -- circling
                --[[
                if(bit.isset(c, 7)) then
                    leftwheel(0,0)
                    rightwheel(1,i_pwm[bit.rshift(bit.band(c, 127), 4)+1])
                else
                    rightwheel(0,0)
                    leftwheel(1,i_pwm[bit.rshift(bit.band(c, 127), 4)+1])
                end 
                --]]
                turnwheel(bit.isset(c,7),c_pwm[bit.rshift(bit.band(c, 127), 4)+1],false)
                turnwheel(not(bit.isset(c,7)),c_pwm[bit.rshift(bit.band(c, 127), 4)+1],true)
            else
                constantSpeed = i_pwm[bit.band(c, 7)+1]
                difSpeed = constantSpeed - dif_s[bit.rshift(bit.band(c, 127), 4)+1]
                bool = bit.isset(c, 3)
                if(difSpeed<0) then 
                    difSpeed = bit.bnot(difSpeed)
                    bool=not bool
                end
            
                if(bit.isset(c, 7)) then
                --turn left
                    turnwheel(bit.isset(c,3),constantSpeed,false)
                    turnwheel(bool,difSpeed,true)
                else
                --turn right
                    turnwheel(bit.isset(c,3),constantSpeed,true)
                    turnwheel(bool,difSpeed,false)
                end  
            end
      
        end
    
    end    
    --tmr.delay(500)
    if not tmr.alarm(1, 500, tmr.ALARM_SINGLE, 
        function() 
           gpio.write(led_udp, gpio.LOW)
        end) 
    then
    else
        gpio.write(led_udp, gpio.HIGH)
    end

end)
s:listen(7777)



if not tmr.alarm(2, 20, tmr.ALARM_AUTO, 
    function()
        smallmouse()        
    end) 
then 
    --smallmouse()    
end
