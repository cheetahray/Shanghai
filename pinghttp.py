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

# this method of reporting timeouts only works by convention
# that before calling handle_request() field .timed_out is 
# set to False

def to243(radar, upordown):
    global ee
    oscmsg = OSCMessage()
    oscmsg.setAddress("/cell")
    oscmsg.append(radar)
    oscmsg.append(upordown)
    print oscmsg
    ee.send(oscmsg)
    
def to245(myauto):
    global ff
    oscmsg = OSCMessage()
    oscmsg.setAddress("/cell")
    oscmsg.append(radar)
    oscmsg.append(upordown)
    print oscmsg
    ff.send(oscmsg)
    
def to247(myauto):
    global gg
    oscmsg = OSCMessage()
    oscmsg.setAddress("/cell")
    oscmsg.append(radar)
    oscmsg.append(upordown)
    print oscmsg
    gg.send(oscmsg)

def quitmax(myquit):
    global bb
    oscmsg = OSCMessage()
    oscmsg.setAddress("/quit")
    oscmsg.append(myquit)
    print oscmsg
    bb.send(oscmsg)

def open252(arg1, arg2, arg3, arg4, arg5, arg6):
    global hh
    oscmsg = OSCMessage()
    oscmsg.setAddress("/comp_id")
    if arg1 > 0:
        oscmsg.append(gamenum[arg1])
    elif arg2 > 0:
        oscmsg.append(gamenum[arg2])
    elif arg3 > 0:
        oscmsg.append(gamenum[arg3])
    elif arg4 > 0:
        oscmsg.append(gamenum[arg4])
    elif arg5 > 0:
        oscmsg.append(gamenum[arg5])
    elif arg6 > 0:
        oscmsg.append(gamenum[arg6])
    oscmsg.append(arg1)
    oscmsg.append(arg2)
    oscmsg.append(arg3)
    oscmsg.append(arg4)
    oscmsg.append(arg5)
    oscmsg.append(arg6)
    print oscmsg
    hh.send(oscmsg)

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

def finalupdate(myDict):
    url = 'http://yyy.yyy.yyy.yyy:7878/update' #https://yyy.yyy.yyy.yyy:7878/更新程式
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}     
    res = requests.post(url, data= 'data=' + urllib.quote(json.dumps(myDict)), headers=headers)
    return json.loads(res.text)#.get('Data')

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

def mode_callback(path, tags, args, source):
    # don't do this at home (or it'll quit blender)
    mode[args[0]] = args[1]
    #print args[0], args[1], path
    
def update_callback(path, tags, args, source):
    # don't do this at home (or it'll quit blender)
    prepareupdate = {}
    winner = ""
    score = 0
    for ii in range(0, len(args), 2):  #比誰最高分
        prepareupdate[idvsradar[args[ii]]] = args[ii+1] #把 osc 傳來的每個人的分數打包進去
        if args[ii+1] > score:
            score = args[ii+1]
            winner = idvsradar[args[ii]] 
    prepareupdate['comp_id'] = gamenum[args[0]] #遊戲流水號
    prepareupdate['play_time'] = str(datetime.datetime.now()) #抓時間
    prepareupdate['winner'] = winner #誰最贏
    print prepareupdate
    print finalupdate(prepareupdate) #準備發出 http request, 檢查 reponse 內容是否格式如此 "update_score":201809010001 
    
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

def findradar():
    if mode[5] == 0:
        #to245(5, 1)    #0 Adult, 1 Child
        mode[5] = 1
        return 5
    if mode[6] == 0:
        #to245(6, 1)
        mode[6] = 1
        return 6
    if mode[7] == 0:
        #to247(7, 1)
        mode[7] = 1
        return 7
    if mode[8] == 0:
        #to247(8, 1)
        mode[8] = 1
        return 8
    if mode[3] == 0:
        #to243(3, 1)
        mode[3] = 1
        return 3
    if mode[4] == 0:
        #to243(4, 1)
        mode[4] = 1
        return 4
    else:
	    print "No radar available"
            
def doexcel(message, mykey, loginret):
    global sheetrow
    if message.has_key(mykey):
        mynum = mykey[-1:] #只是很無聊地把 user_id1 變成 user1_id
        excel.write(sheetrow, 0, message.get(mykey)) #把手機號放到 excel 的第一行
        mykey = "user" + mynum + "_id"
        SHEETROWs[mykey] = sheetrow #暫時 mapping user_id 是 excel 第幾列
        sheetrow += 1 
        idforradar = findradar() #check 雷達柱要 mode 0, 回傳雷達 ID 3~8, 應該要有 error handling, 我甚麼都沒寫
        idvsradar[idforradar] = mykey #暫時mapping 雷達 ID with 玩家user_id
        loginret[mykey] = idforradar #mapping 玩家user_id with 雷達 ID, 用意是回傳玩家分配到哪一個柱子
        gamenum[idforradar] = message.get("comp_id") #暫時mapping 雷達ID with 開局流水號
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
        if self.path[1:] == "nEW":
            quitmax(1)
            to252("/"+self.path[1:])
            to253("/"+self.path[1:])
        elif self.path[1:] == "oLD":
            quitmax(2)
            to252("/"+self.path[1:])
            to253("/"+self.path[1:])
        return

    def do_POST(self): #手機端進入點
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
        message = dict(urlparse.parse_qsl(post_body)) #解析 login 的 json 
        #print message
        self.send_response(200)
        self.end_headers()
        if self.path[1:] == "login": # /not login.php 
            loginret = {}     
            doexcel(message,'user_id1',loginret)
            doexcel(message,'user_id2',loginret)
            doexcel(message,'user_id3',loginret)
            doexcel(message,'user_id4',loginret)
            doexcel(message,'user_id5',loginret)
            doexcel(message,'user_id6',loginret)
            if 0 == len(loginret): #如果是0 甚麼都沒分到 錯誤
                loginret['login'] = 'false'
            else:
                arg1 = 0
                arg2 = 0
                arg3 = 0
                arg4 = 0
                arg5 = 0
                arg6 = 0
                print loginret
                if loginret.has_key('user1_id'):
                    arg1 = loginret['user1_id']
                if loginret.has_key('user2_id'):
                    arg2 = loginret['user2_id']
                if loginret.has_key('user3_id'):
                    arg3 = loginret['user3_id']
                if loginret.has_key('user4_id'):
                    arg4 = loginret['user4_id']
                if loginret.has_key('user5_id'):
                    arg5 = loginret['user5_id']
                if loginret.has_key('user6_id'):
                    arg6 = loginret['user6_id']
                open252(arg1, arg2, arg3, arg4, arg5, arg6) # 傳遊戲流水號 1st雷達柱子號 2nd雷達柱子號 3rd雷達柱子號 4th雷達柱子號 5th雷達柱子號 6th雷達柱子號
                excel.save()
            self.wfile.write(json.dumps(loginret, sort_keys=True, indent=4, separators=(',', ': ')))
            
        elif self.path[1:] == "update": #也是垃圾 沒有用到
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
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
cc = OSCClient()
cc.connect(('192.168.0.252', 8899))   # localhost, port 57120
dd = OSCClient()
dd.connect(('192.168.0.253', 8899))   # localhost, port 57120
ee = OSCClient()
ee.connect(('192.168.0.243', 12001))   # localhost, port 57120
ff = OSCClient()
ff.connect(('192.168.0.245', 12001))   # localhost, port 57120
gg = OSCClient()
gg.connect(('192.168.0.247', 12001))   # localhost, port 57120
hh = OSCClient()
hh.connect(('192.168.0.252', 12002))   # localhost, port 57120
preparupdate = {}
NowMode = 0
idvsradar = {}
SHEETROWs = {}
excel = Excel( "C:\Users\NoiseKitchen_\Documents\Shanghai\data.xls", "sheet1", False)
sheet = excel.read()
sheetrow = sheet.nrows
gamenum = {}
mode = [0,0,0,0,0,0,0,0,0,0]

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
    server2.addMsgHandler( "/mode", mode_callback )
    server2.addMsgHandler( "/update", update_callback )
    #thread.start_new_thread(each_frame2,())
    while True:
        each_frame()
        each_frame2()