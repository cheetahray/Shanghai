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
    if file.open(lightfile, "w+") then
         file.writeline(tostring(dutycycle))
         file.close()
    end
end 

if not file.exists(light1File) then
    writeLight(light1File,"0")
end
if not file.exists(light2File) then
    writeLight(light2File,"0")
end

pin=4
gpio.mode(pin, gpio.OUTPUT)
gpio.write(pin, gpio.HIGH)

_1stpin = 6
_2ndpin = 7
pwm.setup(_1stpin, 1000, readLight(light1File))
pwm.setup(_2ndpin, 1000, readLight(light2File))
pwm.start(_1stpin)
pwm.start(_2ndpin)
myport = 8008

isudp = false
sv = net.createServer(net.UDP)
sv:on("receive", function(sv, pl)
    if isudp == true then
        checkitout(pl)
    end
end)
sv:listen(myport)

tmrid = 0
tmr.register(tmrid, 100, tmr.ALARM_SEMI, 
    function() 
        gpio.write(pin, gpio.HIGH) 
    end)
    
function checkitout(cc)
    print( cc )
    if string.len(cc) > 4 then
        wtf = string.find(cc, "77360708")
        writeWifi(string.sub(cc, 0, wtf-1), string.sub(cc, wtf+8))
        sv:send("Successful Save.")
    else
        if2ndlight = (bit.isset(cc, 7))
        myduty = ( bit.lshift(bit.band(cc, 127), 3) )
        if if2ndlight == false then
            gpio.write(pin, gpio.LOW)
            pwm.setduty(_1stpin, myduty)
        else
            gpio.write(pin, gpio.LOW)
            pwm.setduty(_2ndpin, myduty)
        end
        running, mode = tmr.state(tmrid)
        if false == running then
            if if2ndlight == false then
                writeLight(light1File, myduty)
            else
                writeLight(light2File, myduty)
            end
        else
            if not tmr.stop(tmrid) then 
                print("uh no") 
            end
        end
        if not tmr.start(tmrid) then 
            print("uh oh") 
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

if not file.exists(wifiFile) then
    writeWifi("dac_public","dac_public")
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

wifi.sta.eventMonReg(wifi.STA_WRONGPWD, function() print("STATION_WRONG_PASSWORD") end)

wifi.sta.eventMonReg(wifi.STA_APNOTFOUND, function() 
    print("STATION_NO_AP_FOUND_" .. foundap)
    apnotright()
end)

wifi.sta.eventMonReg(wifi.STA_FAIL, function() 
    print("STATION_CONNECT_FAIL" .. foundap)
    apnotright()
end)

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
    wifi.sta.sleeptype(wifi.MODOM_SLEEP)
    isudp = true
end)

wifi.eventmon.register(wifi.eventmon.AP_STACONNECTED, function(T) 
    print("\n\tAP - STATION CONNECTED".."\n\tMAC: "..T.MAC.."\n\tAID: "..T.AID)
    wifi.eventmon.unregister(wifi.eventmon.AP_STACONNECTED)
end)
