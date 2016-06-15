num=1

cfg={}
 --cfg.ssid="uucar_" .. num
 --cfg.pwd="nk888888"
 --cfg.ssid="uucar_X"
 --cfg.pwd="noisekitchen"
 wifi.ap.config(cfg)

wifi.setmode(wifi.SOFTAP)

r_a=3 ; r_b=2
l_a=5 ; l_b=4
k_b=7 ; k_a=6

led=8
t_num=0

i_pwm = {0,375,400,450,550,675,800,1023}
c_pwm = {0,375,400,435,485,600,800,1023}
dif_s = {0,70,140,280,490,770,980,1120}

for i = 2,5 do
     pwm.setup(i,1000,0)
     pwm.start(i)
end
gpio.mode(k_a, gpio.OUTPUT)
gpio.write(k_a, gpio.LOW)
gpio.mode(k_b, gpio.OUTPUT)
gpio.write(k_b, gpio.LOW)
gpio.mode(led, gpio.OUTPUT)
gpio.write(led, gpio.LOW)



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
    print(i)
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
    
        gpio.write(led, gpio.HIGH)
        if( bit.rshift(bit.band(c, 240), 4) == 8 ) then
        -- PRESS BTN
            if(bit.band(c, 7)==1) then
            -- A
                if(bit.isset(c, 3)) then 
                    --print("kit")
                    --pwmoutput(k_b,1023)
                    gpio.write(k_b, gpio.HIGH)
                else
                    --pwmoutput(k_b,0)
                    gpio.write(k_b, gpio.LOW)
                end
            elseif(bit.band(c, 7)==2) then
            -- B
                if(bit.isset(c, 3)) then 
                    gpio.write(k_b, gpio.HIGH)
                else
                    gpio.write(k_b, gpio.LOW)
                end
            elseif(bit.band(c, 7)==4) then
            -- C
                if(bit.isset(c, 3)) then 
                    gpio.write(k_b, gpio.HIGH)
                else
                    gpio.write(k_b, gpio.LOW)
                end
            elseif(bit.band(c, 7)==7) then
            -- D
                if(bit.isset(c, 3)) then 
                    gpio.write(k_b, gpio.HIGH)
                else
                    gpio.write(k_b, gpio.LOW)
                end
            end
    
        else
    
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
    
        --tmr.delay(500)
        if not tmr.alarm(t_num, 500, tmr.ALARM_SINGLE, 
            function() 
               gpio.write(led, gpio.LOW)
            end) 
        then
            if(t_num==6) then   
                t_num=0
            else
                t_num=t_num+1
            end 
        end
    end    

end)
s:listen(7777)
