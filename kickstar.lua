cfg={}
cfg.ssid = "kickstar"
cfg.pwd = "noisekitchen"
wifi.ap.config(cfg)
wifi.setmode(wifi.SOFTAP)
ip, nm, gw = wifi.ap.getip()
print(ip)
-- 192.168.4.1
-- for mac,ip in pairs(wifi.ap.getclient()) do
--    print(mac,ip)
-- end

pwm.setup(1, 500, 512)
pwm.setup(2, 500, 512)
pwm.start(1)
pwm.start(2)

s=net.createServer(net.UDP)
s:on("receive", function(s, c)
    print( "7th bit is 1 ? " )
    print( bit.isset(c, 7) )
    print( "6,5,4th bits are?" )
    pwm.setduty(1,1023);
    pwm.setduty(2,350);
    print( bit.rshift(bit.band(c, 127), 4) )
    print( "3th bit is 1 ? " )
    print( bit.isset(c, 4) )
    print( "2,1,0th bits are?" )
    print( bit.band(c, 7) )
    print( "7,6,5,4th bits are 1000 ?" )
    print( bit.rshift(bit.band(c, 128), 4) == 16 )
    print( "3th bit is 1 ? " )
    print( bit.isset(c, 3) )
    print( "0th bits is 1 ?" )
    print( bit.isset(c, 0) )
    print( "1th bits is 1 ?" )
    print( bit.isset(c, 1) )
    print( "2th bits is 1 ?" )
    print( bit.isset(c, 2) )
    -- print(c) 
end)
s:listen(7777)
