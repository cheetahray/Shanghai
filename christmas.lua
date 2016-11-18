wifiFile = "wifi.txt"

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
    writeWifi("bellclass","NoiseKitchen")
end

-- open 'init.lua', print the first line.
--[[
if file.open(wifiFile, "r") then
    cfg.ssid = file.readline()
    cfg.ssid = string.sub(cfg.ssid, 0, string.len(cfg.ssid) - 1 )
    cfg.pwd = file.readline()
    cfg.pwd = string.sub(cfg.pwd, 0, string.len(cfg.pwd) - 1 )
    file.close()
end
--]]

wifi.setmode(wifi.STATIONAP)
wifi.sta.config("DAC-1F(rear)","yellowsub")
foundap = 1

cfg={}
cfg.ssid = "HornHorn"
cfg.pwd = "nk88888888"
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
end)

--unregister callback
--wifi.sta.eventMonReg(wifi.STA_IDLE)
