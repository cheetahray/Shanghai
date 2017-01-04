num = 1
highorlow = "low"

raydebug = true
wifiFile = "wifi.txt"
light1File = "light1.txt"
light2File = "light2.txt"
tmp1light = 0
tmp2light = 0
pin=0
btn=1
lightstate=false
_1stpin = 7
_2ndpin = 6
myport = 8008
isudp = false
tmrid = 0
bdid = 1
foid = 2
fiid = 3
foundap = 0
AreWeDone = true
FadeInOutInt = 20
Step1byStep = 1
Step2byStep = 1
whiteyellow = 0
brightness = 0
cfg={}
cfg.ssid = "Drop" .. tostring(num)
cfg.pwd = "nk888888"
cfg.auth=wifi.WPA_WPA2_PSK

gpio.mode(pin, gpio.OUTPUT)
gpio.mode(btn, gpio.INT)
pwm.setup(_1stpin, 100, 0)
pwm.setup(_2ndpin, 100, 0)
pwm.start(_1stpin)
pwm.start(_2ndpin)
wifi.setmode(wifi.STATIONAP)

function findLast(haystack, needle)
    local i=haystack:match(".*"..needle.."()")
    if i==nil then return nil else return i-1 end
end

function readButton(level)
    running, mode = tmr.state(bdid)
    if true == running
    then
        if true == raydebug then
            print("double click")
        end 
    else
        if not tmr.start(bdid) then
            if true == raydebug then
                -- srv:send("No click start")
            end
        else
            if true == raydebug then
                srv:send("click start")
            end
        end
        if true == AreWeDone then
            AreWeDone = false
            Step1byStep = ( final1light / ( 1024 / FadeInOutInt ) )
            Step2byStep = ( final2light / ( 1024 / FadeInOutInt ) )
            if true == raydebug then
                srv:send(Step1byStep)
                srv:send(Step2byStep)
            end
            if (lightstate == true) then
                if not tmr.start(foid) then
                    if true == raydebug then
                        srv:send("No fade out start")
                    end
                else
                    tmp1light = final1light
                    tmp2light = final2light
                    if true == raydebug then
                        srv:send("fade out start")
                    end
                end
            else
                if not tmr.start(fiid) then
                    if true == raydebug then
                        srv:send("No fade in start")
                    end
                else
                    tmp1light = 0
                    tmp2light = 0
                    if true == raydebug then
                        srv:send("fade in start")
                    end                        
                end
            end
        end
    end
end

function readLight(lightFile)
    theduty = 0
    if file.open(lightFile, "r") then
        tempduty = file.readline()
        tempduty = string.sub(tempduty, 0, string.len(tempduty) - 1 )
        theduty = tonumber(tempduty)
        file.close()
    end
    return theduty
end

function writeLight(lightfile,dutycycle) 
    if file.open(lightfile, "w+") then
         file.writeline(tostring(dutycycle))
         file.close()
    end
end 
        
function setmylight(realset)
    final2light = 127 - whiteyellow 
    final1light = ( bit.rshift( whiteyellow * brightness, 4 ) )
    final2light = ( bit.rshift( final2light * brightness, 4 ) )
    if realset == true then    
        if raydebug == true then
            srv:send(final1light)
            srv:send(final2light)
        end        
        lightstate = true
        pwm.setduty(_1stpin, final1light )
        pwm.setduty(_2ndpin, final2light )
    end
end

function checkitout(cc)
    if true == raydebug then
        print(cc)
    end
    if string.len(cc) > 4 then
        wtf = string.find(cc, "77360708")
        writeWifi(string.sub(cc, 0, wtf-1), string.sub(cc, wtf+8))
        srv:send("Successfully Save.")
    else
        if2ndlight = (bit.isset(cc, 7))
        gpio.write(pin, gpio.LOW)
        if if2ndlight == false then
            whiteyellow = ( bit.band(cc, 127) )
        else
            brightness = ( bit.band(cc, 127) )
        end
        setmylight(true)
        if not tmr.stop(tmrid) then
            if true == raydebug then
                srv:send("No savelight stop") 
            end
        end
        if not tmr.start(tmrid) then
            if true == raydebug then
                srv:send("No savelight start")
            end
        end
    end
end

function writeWifi(ssid,password) 
    if file.open(wifiFile, "w+") then
         file.writeline(ssid)
         file.writeline(password)
         file.close()
    end
end 

function apnotright()
    if foundap == 1 then
        wifi.sta.config(cfg.ssid,cfg.pwd)
        foundap = foundap + 1
    else
        if true == raydebug then
            print(cfg.ssid)
        end
        wifi.setmode(wifi.SOFTAP)
        wifi.ap.config(cfg)
        wifi.sta.eventMonStop()
        srv:connect(8118,"192.168.4.255")
        isudp = true
    end 
end

tmr.register(bdid, 20000, tmr.ALARM_SEMI, 
    function() 
        tmr.interval(bdid, 2000)
    end)

tmr.register(tmrid, 100, tmr.ALARM_SEMI, 
    function() 
        gpio.write(pin, gpio.HIGH)
        running, mode = tmr.state(tmrid)
        if false == running then
            if if2ndlight == false then
                writeLight(light1File, whiteyellow)
                if true == raydebug then
                    srv:send(whiteyellow)
                end
            else
                writeLight(light2File, brightness)
                if true == raydebug then
                    srv:send(brightness)
                end
            end 
        end
    end)

tmr.register(foid, FadeInOutInt, tmr.ALARM_AUTO, 
    function()
        if(tmp1light > 0) then    
            tmp1light = tmp1light - Step1byStep
            if 0 > tmp1light then
                tmp1light = 0
            end
            pwm.setduty(_1stpin, math.floor(tmp1light))
        end
        if(tmp2light > 0) then    
            tmp2light = tmp2light - Step2byStep
            if 0 > tmp2light then
                tmp2light = 0
            end
            pwm.setduty(_2ndpin, math.floor(tmp2light))
        end
        if(tmp1light == 0 and tmp2light == 0) then
            if not tmr.stop(foid) then
                if true == raydebug then
                    srv:send("No fade out stop")
                end
            else
                lightstate = false 
                AreWeDone = true
                if true == raydebug then
                    srv:send("fade out stop")
                end
            end       
        end
    end)

tmr.register(fiid, FadeInOutInt, tmr.ALARM_AUTO, 
    function()
        if(tmp1light < final1light) then    
            tmp1light = tmp1light + Step1byStep
            if final1light < tmp1light then
                tmp1light = final1light
            end
            pwm.setduty(_1stpin, math.floor(tmp1light))
        end
        if(tmp2light < final2light) then    
            tmp2light = tmp2light + Step2byStep
            if final2light < tmp2light then
                tmp2light = final2light
            end
            pwm.setduty(_2ndpin, math.floor(tmp2light))
        end
        if(tmp1light == final1light and tmp2light == final2light) then
            if not tmr.stop(fiid) then
                if true == raydebug then
                    srv:send("No fade in stop") 
                end
            else
                lightstate = true
                AreWeDone = true
                if true == raydebug then
                    srv:send("fade in stop")
                end
            end       
        end
    end)
--[[
wifi.sta.eventMonReg(wifi.STA_WRONGPWD, 
    function() 
        if true == raydebug then
            print("STATION_WRONG_PASSWORD") 
        end
    end)
]]--
wifi.sta.eventMonReg(wifi.STA_APNOTFOUND, 
    function()
        if true == raydebug then     
            print("STATION_NO_AP_FOUND_" .. foundap)
        end
        apnotright()
    end)

wifi.sta.eventMonReg(wifi.STA_FAIL, 
    function()
        if true == raydebug then    
            print("STATION_CONNECT_FAIL" .. foundap)
        end
        apnotright()
    end)

wifi.sta.eventMonReg(wifi.STA_CONNECTING, 
    function(previous_State)
        --[[
        if(previous_State==wifi.STA_GOTIP) then
            if true == raydebug then        
                print("Station lost connection with access point\n\tAttempting to reconnect...")
            end
        else
        ]]--
            if true == raydebug then
                print("STATION_CONNECTING")
            end
        -- end
    end)

wifi.sta.eventMonStart()

wifi.eventmon.register(wifi.eventmon.STA_CONNECTED, function(T) 
    if true == raydebug then
        print("\n\tSTA - CONNECTED".."\n\tSSID: "..T.SSID.."\n\tBSSID: "..
        T.BSSID.."\n\tChannel: "..T.channel)
    end
end)

wifi.eventmon.register(wifi.eventmon.STA_GOT_IP, function(T) 
    if true == raydebug then
        print("\n\tSTA - GOT IP".."\n\tStation IP: "..T.IP.."\n\tSubnet mask: "..
        T.netmask.."\n\tGateway IP: "..T.gateway)
        -- print(string.sub(T.IP, 0, findLast(T.IP,"%.")) .. "255")
    end
    srv:connect(8118, string.sub(T.IP, 0, findLast(T.IP,"%.")) .. "255" )
    wifi.sta.eventMonStop()
    wifi.eventmon.unregister(wifi.eventmon.STA_CONNECTED)
    wifi.eventmon.unregister(wifi.eventmon.STA_GOT_IP)
    wifi.setmode(wifi.STATION)
    -- wifi.sta.sleeptype(wifi.MODOM_SLEEP)
    isudp = true
end)

wifi.eventmon.register(wifi.eventmon.AP_STACONNECTED, function(T) 
    if true == raydebug then
        print("\n\tAP - STATION CONNECTED".."\n\tMAC: "..T.MAC.."\n\tAID: "..T.AID)
    end
    wifi.eventmon.unregister(wifi.eventmon.AP_STACONNECTED)
end)

if not file.exists(light1File) then
    writeLight(light1File,64)
end

if not file.exists(light2File) then
    writeLight(light2File,64)
end

if not file.exists(wifiFile) then
    writeWifi("JQ-VIP","lifehub123456")
end

whiteyellow = readLight(light1File)
brightness = readLight(light2File)
setmylight(false)
gpio.write(pin, gpio.HIGH)
gpio.trig(btn, highorlow, readButton)

if file.open(wifiFile, "r") then
    ssid = file.readline()
    ssid = string.sub(ssid, 0, string.len(ssid) - 1 )
    pwd = file.readline()
    pwd = string.sub(pwd, 0, string.len(pwd) - 1 )
    wifi.sta.config(ssid, pwd)
    file.close()
end

sv = net.createServer(net.UDP)
sv:on("receive", function(sv, pl)
    if isudp == true then
        checkitout(pl)
    end
end)
sv:listen(myport)

srv = net.createConnection(net.UDP, 0)

readButton(0)