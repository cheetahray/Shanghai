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
#from SocketServer import ThreadingMixIn
from expy.excel import Excel
import datetime
# this method of reporting timeouts only works by convention
# that before calling handle_request() field .timed_out is 
# set to False

def quitmax():
    global bb
    oscmsg = OSCMessage()
    oscmsg.setAddress("/quit")
    oscmsg.append(1)
    print oscmsg
    bb.send(oscmsg)

def to252(msg):
    global cc
    oscmsg = OSCMessage()
    oscmsg.setAddress(msg)
    #oscmsg.append(arg0)
    print oscmsg
    cc.send(oscmsg)

def to253(msg):
    global dd
    oscmsg = OSCMessage()
    oscmsg.setAddress(msg)
    #oscmsg.append(arg0)
    print oscmsg
    dd.send(oscmsg)

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
            print "unlock"

def delallfish():
    global fishcnt
    aa = crm("GAME_BAMEYU&CRM_bonus&ext=1", {}).get('Data')
    for i, val in enumerate(aa):
        value = crm("GetYu", {"phone": val.get('M_ID')})
        if value.get('Data') == val.get('M_ID'):
            print "unlock", val.get('M_ID')
        time.sleep(0.25)
    fishcnt = 0
    bb = crm("GAME_MID&CRM_bonus&ext=1", {}).get('Data')
    for i, val in enumerate(bb):
        value = crm("GetGamesdes", {"phone": val.get('M_ID')})
        if value.get('Data') == val.get('M_ID'):
            print "UNLOCK", val.get('M_ID')
        time.sleep(0.25)


def delfish_callback(path, tags, args, source):
    print (path)
    delallfish()

def doexcel(message, mykey, loginret):
    global sheetrow
    if message.has_key(mykey):
        mynum = mykey[-1:]
        excel.write(sheetrow, 0, message.get(mykey))
        mykey = "user" + mynum + "_id"
        SHEETROWs[mykey] = sheetrow
        sheetrow += 1
        loginret[mykey] = 7-int(mynum)
    return loginret

def doupdate(message, mykey):
    if message.has_key(mykey):
        excel.write(SHEETROWs[mykey], 1, message.get(mykey))
        excel.write(SHEETROWs[mykey], 2, message.get('play_time'))
        if message.get('winner') == mykey:
            excel.write(SHEETROWs[mykey], 3, 1)
        else:
            excel.write(SHEETROWs[mykey], 3, 0)
            
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""
    
class GetHandler(BaseHTTPRequestHandler):
    
    def end_headers (self):
        self.send_header('Access-Control-Allow-Origin', '*')
        BaseHTTPRequestHandler.end_headers(self)
        
    def do_GET(self):
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
        if self.path[1:] == "nEW" or self.path[1:] == "oLD":
            to252("/"+self.path[1:])
            to253("/"+self.path[1:])
        return

    def do_POST(self):
        global sheetrow
        id1way = 0
        id2way = 0
        id3way = 0
        id4way = 0
        id5way = 0
        id6way = 0
        content_len = int(self.headers.getheader('content-length'))
        post_body = self.rfile.read(content_len)
        #print post_body
        message = dict(urlparse.parse_qsl(post_body))
        #print message
        self.send_response(200)
        self.end_headers()
        if self.path[1:] == "login":
            loginret = {}
            doexcel(message,'user_id1',loginret)
            doexcel(message,'user_id2',loginret)
            doexcel(message,'user_id3',loginret)
            doexcel(message,'user_id4',loginret)
            doexcel(message,'user_id5',loginret)
            doexcel(message,'user_id6',loginret)
            if 0 == len(loginret):
                loginret['login'] = 'false'
            else:
                excel.save()
            self.wfile.write(json.dumps(loginret, sort_keys=True, indent=4, separators=(',', ': ')))
            
        elif self.path[1:] == "update":
            updateret = {}
            updateret['update_score'] = message.get('comp_id')
            doupdate(message, 'user1_id')
            doupdate(message, 'user2_id')
            doupdate(message, 'user3_id')
            doupdate(message, 'user4_id')
            doupdate(message, 'user5_id')
            doupdate(message, 'user6_id')
            excel.save()
            self.wfile.write(json.dumps(updateret, sort_keys=True, indent=4, separators=(',', ': ')))
        #data = json.loads(post_body)
        #print data
        #self.wfile.write(data['foo'])
        return

fishcnt = 0
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
bb = OSCClient()
bb.connect(('192.168.0.252', 6666))   # localhost, port 57120
cc = OSCClient()
cc.connect(('192.168.0.252', 8899))   # localhost, port 57120
dd = OSCClient()
dd.connect(('192.168.0.253', 8899))   # localhost, port 57120

NowMode = 0

SHEETROWs = {}
excel = Excel( "C:\Users\NoiseKitchen_\Documents\Shanghai\data.xls", "sheet1", False)
sheet = excel.read()
sheetrow = sheet.nrows

if __name__ == '__main__':
    server = ThreadedHTTPServer(('0.0.0.0', 8899), GetHandler)
    server.timeout = 0.01
    print 'Starting server at http://localhost:8899'
    server.handle_timeout = types.MethodType(handle_timeout, server)
    server2 = OSCServer( ("0.0.0.0", 7111) )
    server2.timeout = 0.01
    # funny python's way to add a method to an instance of a class
    server2.handle_timeout = types.MethodType(handle_timeout2, server2)
    server2.addMsgHandler( "/swim", swim_callback )
    server2.addMsgHandler( "/delfish", delfish_callback )
    #thread.start_new_thread(each_frame2,())
    while True:
        each_frame()
        each_frame2()