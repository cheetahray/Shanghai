#!/usr/bin/python
# -*- coding: UTF-8 -*-
from BaseHTTPServer import BaseHTTPRequestHandler
import urlparse, json
import datetime
from OSC import *
import types
from BaseHTTPServer import HTTPServer
import random    
import requests
import urllib
import thread
from SocketServer import ThreadingMixIn
# this method of reporting timeouts only works by convention
# that before calling handle_request() field .timed_out is 
# set to False

def over(msg,arg0,arg1,arg2):
    global cc
    oscmsg = OSCMessage()
    oscmsg.setAddress(msg)
    oscmsg.append(arg0)
    oscmsg.append(arg1)
    oscmsg.append(arg2)
    print oscmsg
    cc.send(oscmsg)

def crm(url2, myDict):
    url = 'http://183.131.3.182:9002/query.ashx?method=' #'http://47.97.194.91:8686/query.ashx?method='
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}     
    res = requests.post(url+url2, data= 'data=' + urllib.quote(json.dumps(myDict)), headers=headers)
    return json.loads(res.text)#.get('Data')
    
def handle_timeout2(self):
    self.timed_out = True

def handle_timeout(self):
    self.timed_out = True

def each_frame():
    # clear timed_out flag
    server.timed_out = False
    # handle all pending requests then return
    while not server.timed_out:
        server.handle_request()

def each_frame2():
    # clear timed_out flag
    server2.timed_out = False
    # handle all pending requests then return
    while not server2.timed_out:
        server2.handle_request()

def swim_callback(path, tags, args, source):
    global fishcnt
    # don't do this at home (or it'll quit blender)
    #global run
    #run = False
    print (path, args[0], args[1]) #tel 1/0
    if 1 == args[1]:
        fishcnt += 1
        print "plus"
    elif 0 == args[1]:
        value = crm("GetYu", {"phone": args[0]})
        if value.get('Data') == args[0]:
            fishcnt -= 1
            YuList.remove(args[0])
            print "unlock"

def delallfish():
    global fishcnt
    for ii in YuList:
        value = crm("GetYu", {"phone": ii})
        if value.get('Data') == ii:
            print "unlock", ii
        time.sleep(0.25)
    del YuList[:]
    fishcnt = 0

def delfish_callback(path, tags, args, source):
    print (path)
    delallfish()

def scene_callback(path, tags, args, source):
    global NowMode, fishcnt
    # don't do this at home (or it'll quit blender)
    #global run
    #run = False
    #add old data then restore back
    print (path, args[0], args[1]) #Mode auto/hand
    NowMode = args[0]
    fishcnt = 0
    #now = datetime.datetime.now()
    #print now.year, now.month, now.day, now.hour, now.minute, now.second

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    
class GetHandler(BaseHTTPRequestHandler):
    
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        BaseHTTPRequestHandler.end_headers(self)
        
    def do_GET(self):
        global fishcnt
        '''
        parsed_path = urlparse.urlparse(self.path)
        message = '\n'.join([
            'CLIENT VALUES:',
            'client_address=%s (%s)' % (self.client_address,
                self.address_string()),
            'command=%s' % self.command,
            'path=%s' % self.path,
            'real path=%s' % parsed_path.path,
            'query=%s' % parsed_path.query,
            'request_version=%s' % self.request_version,
            '',
            'SERVER VALUES:',
            'server_version=%s' % self.server_version,
            'sys_version=%s' % self.sys_version,
            'protocol_version=%s' % self.protocol_version,
            '',
            ])
        '''
        message = dict(urlparse.parse_qsl(urlparse.urlsplit(self.path).query))
        self.send_response(200)
        self.end_headers()
        '''
        if message.has_key('barcode') and message.has_key('game'):
            value = crm("PlayGames", {"phone": message.get('barcode')})
            #print value.get('Data')
            if value.get('Data') == "C":
                print "OnGame 1"
                self.wfile.write(json.dumps({"OnGame":"1"}, sort_keys=True, indent=4, separators=(',', ': ')))
            else:
                print "OnGame 0"
                self.wfile.write(json.dumps({"OnGame":"0"}, sort_keys=True, indent=4, separators=(',', ': ')))
        '''
        if message.has_key('m_id'): # Got to change to http request
            
            '''
            value = crm("PlayGames", {"phone": message.get('m_id')})
            if value.get('Data') == "B":
                print "Not be a member yet."   #如果此會員還沒註冊，回傳 /error 0or1or2...
                self.wfile.write(json.dumps({"Result":"0", "errmsg":"不是会员，抱歉"}, sort_keys=True, indent=4, separators=(',', ': ')))
            '''
            if message.has_key('put') and message.get('put') == 'no':
                value = crm("CheckYu", {"phone": message.get('m_id')})
                #print value.get('Data')
                if value.get('Data') == "C":
                    print "OnScreen 1"
                    self.wfile.write(json.dumps({"OnScreen":"1"}, sort_keys=True, indent=4, separators=(',', ': ')))
                else:
                    print "OnScreen 0"
                    self.wfile.write(json.dumps({"OnScreen":"0"}, sort_keys=True, indent=4, separators=(',', ': ')))
            else:
                boolMode = False
                print "Now is ", fishcnt
        
                now = datetime.datetime.now()
                if False: #now.minute % 30 == 28 :
                    print "Close to halftime show"
                    self.wfile.write(json.dumps({"Result": "0", "errmsg":"要整点秀了"}, sort_keys=True, indent=4, separators=(',', ': ')))
                        
                elif NowMode == GameMode and fishcnt < 6:
                    boolMode = True
                elif NowMode == StandbyMode and fishcnt < 12:
                    boolMode = True
                
                if(False == boolMode):
                    print "Result 0"
                    self.wfile.write(json.dumps({"Result": "0", "errmsg":"鱼池满了"}, sort_keys=True, indent=4, separators=(',', ': ')))
                else:
                
                    value = crm("SetYu", {"phone": message.get('m_id')})
                    if value.get('Data') == "C":
                        print "Just in your game."
                        self.wfile.write(json.dumps({"Result":"0", "errmsg":"您还在大屏上"}, sort_keys=True, indent=4, separators=(',', ': ')))
                    elif isinstance(value.get('Data'), dict):
                        print value
                        cpan = value.get('Data').get('C_PAN')
                        #print cpan[-1:]
                        over("/swimplayer", message.get('m_id'), int(value.get('Data').get('C_ID')), int(cpan[-1:])) #phone number, role number, color num         
                        sock.sendto(message.get('m_id') + "!@#" + value.get('Data').get('C_NAME').encode('utf8'),("192.168.1.200",8765))
                        '''
                        god = random.randint(10000000000,99999999999)
                        over("/swimplayer", str(god), random.randint(0,11), random.randint(0,2)) #phone number, role number, color num         
                        '''
                        #sock.sendto(message.get('m_id') + "!@#" + "N+Ray",("192.168.1.200",8765))
                        YuList.append(message.get('m_id'))
                        self.wfile.write(json.dumps({"Result":"1"}, sort_keys=True, indent=4, separators=(',', ': ')))
                    else:
                        print value
            '''
            else: #elif value.get('Data')[0] == "A":
                #XF_VIPCODE = value.get('Data')[value.get('Data').index(":")+1:]
                print "Not opened card yet."     
                self.wfile.write(json.dumps({"Result":"0", "errmsg":"尚未开卡，抱歉"}, sort_keys=True, indent=4, separators=(',', ': ')))  
            '''
        else:
            self.wfile.write(json.dumps({"Result":"0", "errmsg":"没手机号"}, sort_keys=True, indent=4, separators=(',', ': ')))
        return

    def do_POST(self):
        content_len = int(self.headers.getheader('content-length'))
        post_body = self.rfile.read(content_len)
        self.send_response(200)
        self.end_headers()

        data = json.loads(post_body)

        self.wfile.write(data['foo'])
        return

fishcnt = 0
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
cc = OSCClient()
cc.connect(('192.168.1.200', 6666))   # localhost, port 57120
StandbyMode = 1
GameMode = 2
ShowMode = 3
NowMode = 1
YuList = []

if __name__ == '__main__':
    server = ThreadedHTTPServer(('0.0.0.0', 6161), GetHandler)
    server.timeout = 0.001
    print 'Starting server at http://localhost:6161'
    server.handle_timeout = types.MethodType(handle_timeout, server)
    server2 = OSCServer( ("0.0.0.0", 7111) )
    server2.timeout = 0.001
    # funny python's way to add a method to an instance of a class
    server2.handle_timeout = types.MethodType(handle_timeout2, server2)
    server2.addMsgHandler( "/swim", swim_callback )
    server2.addMsgHandler( "/Scene", scene_callback )
    server2.addMsgHandler( "/delfish", delfish_callback )
    #thread.start_new_thread(each_frame2,())
    while True:
        each_frame()
        each_frame2()