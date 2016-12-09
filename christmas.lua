wifiFile = "wifi.txt"
light1File = "light1.txt"
light2File = "light2.txt"

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
    -- open 'init.lua' in 'a+' mode
    if file.open(lightfile, "w+") then
         -- write 'foo bar' to the end of the file
         file.writeline(tostring(dutycycle))
         file.close()
    end
end 

if not file.exists(light1File) then
    -- writeWifi("bellclass","NoiseKitchen")
    writeLight(light1File,"0")
end
if not file.exists(light2File) then
    -- writeWifi("bellclass","NoiseKitchen")
    writeLight(light2File,"0")
end

_1stpin = 6
_2ndpin = 7
pwm.setup(_1stpin, 1000, readLight(light1File))
pwm.setup(_2ndpin, 1000, readLight(light2File))
--pwm.setup(3, 500, 0)
pwm.start(_1stpin)
pwm.start(_2ndpin)
--pwm.start(3)
myport = 8008

isudp = false
sv = net.createServer(net.UDP)
-- server listens on 80, if data received, print data to console and send "hello world" back to caller
sv:on("receive", function(sv, pl)
    if isudp == true then
        checkitout(pl)
        -- c:send("hello world")
    end
end)
sv:listen(myport)

function checkitout(cc)
    print( cc )
    -- print (string.len(cc))
    if string.len(cc) > 4 then
        count = 1
        ssid = ""
        pwd = ""
        for word in string.gmatch(cc, "%a+") do 
            if count == 1 then
                ssid = word
                count = count + 1
            else
                pwd = word
            end
            print(word) 
        end
        writeWifi(ssid, pwd)
    else
        -- 7th bit is 1 ?
        -- print( bit.isset(c, 7) )
        if2ndlight = (bit.isset(cc, 7))
        myduty = ( bit.lshift(bit.band(cc, 127), 3) )
        if if2ndlight == false then
            pwm.setduty(_1stpin, myduty)
        else
            pwm.setduty(_2ndpin, myduty)
        end
        if not tmr.alarm(0, 550, tmr.ALARM_SINGLE, 
            function() 
            end) 
        then
        else
            if if2ndlight == false then
                writeLight(light1File, myduty)
            else
                writeLight(light2File, myduty)
            end            
        end
    end
end

function writeWifi(ssid,password) 
    -- open 'init.lua' in 'a+' mode
    if file.open(wifiFile, "w+") then
         -- write 'foo bar' to the end of the file
         file.writeline(ssid)
         file.writeline(password)
         file.close()
    end
end 

if not file.exists(wifiFile) then
    -- writeWifi("bellclass","NoiseKitchen")
    writeWifi("DAC-2F(rear)","yellowsub")
end

wifi.setmode(wifi.STATIONAP)
if file.open(wifiFile, "r") then
    ssid = file.readline()
    ssid = string.sub(ssid, 0, string.len(ssid) - 1 )
    pwd = file.readline()
    pwd = string.sub(pwd, 0, string.len(pwd) - 1 )
    wifi.sta.config(ssid, pwd)
    file.close()
end

foundap = 1

cfg={}
cfg.ssid = "DiDiDa"
cfg.pwd = "nk888888"
cfg.auth=wifi.WPA_WPA2_PSK

function apnotright()
    if foundap == 1 then
        wifi.sta.config(cfg.ssid,cfg.pwd)
        foundap = foundap + 1
    else
        print(cfg.ssid)
        wifi.setmode(wifi.SOFTAP)
        wifi.ap.config(cfg)
        wifi.sta.eventMonStop()
        
        isudp = true
    end 
end
--register callback
wifi.sta.eventMonReg(wifi.STA_IDLE, function() print("STATION_IDLE") end)

-- wifi.sta.eventMonReg(wifi.STA_CONNECTING, function() print("STATION_CONNECTING") end)

wifi.sta.eventMonReg(wifi.STA_WRONGPWD, function() print("STATION_WRONG_PASSWORD") end)

wifi.sta.eventMonReg(wifi.STA_APNOTFOUND, function() 
    print("STATION_NO_AP_FOUND_" .. foundap)
    apnotright()
end)

wifi.sta.eventMonReg(wifi.STA_FAIL, function() 
    print("STATION_CONNECT_FAIL" .. foundap)
    apnotright()
end)

--wifi.sta.eventMonReg(wifi.STA_GOTIP, function() print("STATION_GOT_IP") end)

--register callback: use previous state
wifi.sta.eventMonReg(wifi.STA_CONNECTING, function(previous_State)
    if(previous_State==wifi.STA_GOTIP) then 
        print("Station lost connection with access point\n\tAttempting to reconnect...")
    else
        print("STATION_CONNECTING")
    end
end)

wifi.sta.eventMonStart()

wifi.eventmon.register(wifi.eventmon.STA_CONNECTED, function(T) 
    print("\n\tSTA - CONNECTED".."\n\tSSID: "..T.SSID.."\n\tBSSID: "..
    T.BSSID.."\n\tChannel: "..T.channel)
end)

wifi.eventmon.register(wifi.eventmon.STA_GOT_IP, function(T) 
    print("\n\tSTA - GOT IP".."\n\tStation IP: "..T.IP.."\n\tSubnet mask: "..
    T.netmask.."\n\tGateway IP: "..T.gateway)
    wifi.sta.eventMonStop()
    wifi.eventmon.unregister(wifi.eventmon.STA_CONNECTED)
    wifi.eventmon.unregister(wifi.eventmon.STA_GOT_IP)
    wifi.setmode(wifi.STATION)
    isudp = true
end)

wifi.eventmon.register(wifi.eventmon.AP_STACONNECTED, function(T) 
    print("\n\tAP - STATION CONNECTED".."\n\tMAC: "..T.MAC.."\n\tAID: "..T.AID)
    wifi.eventmon.unregister(wifi.eventmon.AP_STACONNECTED)
end)

--unregister callback
wifi.sta.eventMonReg(wifi.STA_IDLE)
