wifiFile = "wifi.txt"
-- 30s time out for a inactive client
sv = net.createServer(net.UDP, 30)

_1stpin = 1
_2ndpin = 2
pwm.setup(_1stpin, 1000, 0)
pwm.setup(_2ndpin, 1000, 0)
--pwm.setup(3, 500, 0)
pwm.start(_1stpin)
pwm.start(_2ndpin)
--pwm.start(3)
myport = 8008

function opennet()
    -- server listens on 80, if data received, print data to console and send "hello world" back to caller
    sv:listen(myport, function(c)
        c:on("receive", function(c, pl) 
            checkitout(pl)
        end)
        -- c:send("hello world")
    end)
end

function checkitout(cc)
    print( cc )
    if string.len(cc) > 1 then
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
        if bit.isset(cc, 7) == 1 then
            pwm.setduty(_1stpin, bit.lshift(bit.band(cc, 127), 3) )
        else
            pwm.setduty(_2ndpin, bit.lshift(bit.band(cc, 127), 3) )
        end
        print (bit.lshift(bit.band(cc, 127), 3))
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

--register callback
wifi.sta.eventMonReg(wifi.STA_IDLE, function() print("STATION_IDLE") end)

-- wifi.sta.eventMonReg(wifi.STA_CONNECTING, function() print("STATION_CONNECTING") end)

wifi.sta.eventMonReg(wifi.STA_WRONGPWD, function() print("STATION_WRONG_PASSWORD") end)

wifi.sta.eventMonReg(wifi.STA_APNOTFOUND, function() 
    print("STATION_NO_AP_FOUND_" .. foundap)
    if foundap == 1 then
        wifi.sta.config(cfg.ssid,cfg.pwd)
        foundap = foundap + 1
    else
        print(cfg.ssid)
        wifi.ap.config(cfg)
        wifi.sta.eventMonStop()
        
        opennet()
    end 
end)

wifi.sta.eventMonReg(wifi.STA_FAIL, function() 
    print("STATION_CONNECT_FAIL")
    wifi.sta.eventMonStop() 
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

    opennet()
end)

wifi.eventmon.register(wifi.eventmon.AP_STACONNECTED, function(T) 
    print("\n\tAP - STATION CONNECTED".."\n\tMAC: "..T.MAC.."\n\tAID: "..T.AID)
    wifi.eventmon.unregister(wifi.eventmon.AP_STACONNECTED)
end)

--unregister callback
wifi.sta.eventMonReg(wifi.STA_IDLE)
