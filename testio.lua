l_a=1
l_b=2
r_a=3
r_b=4
k_a=5
k_b=6

i_pwm = {0,351,463,575,687,799,911,1023}

for i = 1,5 do
     pwm.setup(i,512,0)
     pwm.start(i)
     --print(i)
     --gpio.mode(4+i, gpio.OUTPUT)
     --gpio.write(4+i, gpio.HIGH)
end

c = 16

_0to2 = bit.band(c, 7)
_3isTrue= bit.isset(c, 3)
_4to6 = bit.rshift(bit.band(c, 127), 4) 
_7isTrue = bit.isset(c, 7)

print( _0to2 )
print( _3isTrue )
print( _4to6 )
print( _7isTrue )

_0to2 = _0to2 + 1 
_4to6 = _4to6 + 1

function pwmoutput(p,i)
    print (p)
    print (i)
    pwm.setduty(p, i)
end

if( bit.band(c, 128) == 128 ) then
    print("kit")
    --print(bit.band(c, 7))
else
    --speed1= bit.band(c, 7) > 0)
    if( 1 == _0to2 ) then
        if(_7isTrue) then
            pwmoutput(l_b,i_pwm[_4to6])
            pwmoutput(l_a,i_pwm[1])
            pwmoutput(r_a,i_pwm[_4to6])
            pwmoutput(r_b,i_pwm[1])
        else
            pwmoutput(r_b,i_pwm[_4to6])
            pwmoutput(r_a,i_pwm[1])
            pwmoutput(l_a,i_pwm[_4to6])
            pwmoutput(l_b,i_pwm[1])
        end
    else
        if(_7isTrue) then
            if(_3isTrue) then
                pwmoutput(l_a,i_pwm[_0to2])
                pwmoutput(l_b,0)
                pwmoutput(r_b,0)
                if( 0 == _4_6 ) then
                    pwmoutput(r_a,i_pwm[_0to2])
                else
                    pwmoutput(r_a,i_pwm[_0to2 - _4to6 + 1])
                end
            else
                pwmoutput(l_b,i_pwm[_0to2])
                pwmoutput(l_a,0)
                pwmoutput(r_a,0)
                if( 0 == _4_6 ) then
                    pwmoutput(r_b,i_pwm[_0to2])
                else
                    pwmoutput(r_b,i_pwm[_0to2 - _4to6 + 1])
                end
            end
        else
            if(_3isTrue) then
                pwmoutput(r_a,i_pwm[_0to2])
                pwmoutput(r_b,0)
                pwmoutput(l_b,0)
                if( 0 == _4_6 ) then
                    pwmoutput(l_a,i_pwm[_0to2])
                else
                    pwmoutput(l_a,i_pwm[_0to2 - _4to6 + 1])
                end
            else
                pwmoutput(r_b,i_pwm[_0to2])
                pwmoutput(r_a,0)
                pwmoutput(l_a,0)
                if( 0 == _4_6 ) then
                    pwmoutput(l_b,i_pwm[_0to2])
                else
                    pwmoutput(l_b,i_pwm[_0to2 - _4to6 + 1])
                end
            end
        end
    end
end