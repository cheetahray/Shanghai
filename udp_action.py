import socket
import os
import commands
import time

ips = commands.getoutput("/sbin/ifconfig | grep -iA2 \"eth0\" | grep -i \"inet\" | grep -iv \"inet6\" | " +
                         "awk {'print $2'} | sed -ne 's/addr\://p'")
iplist = ips.split(".")
whoami = int(iplist[3])
UDP_IP = iplist[0] + "." + iplist[1] + "." + iplist[2] + "." + str(whoami + 100)
print "target IP is : " + UDP_IP
UDP_PORT = 5005
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind(("", UDP_PORT))

while True:
    udp_cmd = raw_input('Send to Motor Pi--> ')
    print udp_cmd
    starttime = time.time()
    sock.sendto(udp_cmd, (UDP_IP, UDP_PORT))
    data, addr = sock.recvfrom(1024)
    endtime = time.time()
    print data + " " + str(endtime - starttime)



