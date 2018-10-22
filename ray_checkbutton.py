#!/usr/bin/python
# -*- coding: UTF-8 -*-
import Tkinter as tk
from OSC import *
import types
import thread
import time
import datetime
window = tk.Tk()
window.title('快捷方式')
window.geometry('250x100')

l = tk.Label(window, bg='yellow', width=20, text='请选择')
l.pack()

def to243(myauto):
    global ee
    oscmsg = OSCMessage()
    oscmsg.setAddress("/auto")
    oscmsg.append(myauto)
    print oscmsg
    ee.send(oscmsg)
    
def to245(myauto):
    global ff
    oscmsg = OSCMessage()
    oscmsg.setAddress("/auto")
    oscmsg.append(myauto)
    print oscmsg
    ff.send(oscmsg)
    
def to247(myauto):
    global gg
    oscmsg = OSCMessage()
    oscmsg.setAddress("/auto")
    oscmsg.append(myauto)
    print oscmsg
    gg.send(oscmsg)

def quitmax(myquit):
    global bb
    oscmsg = OSCMessage()
    oscmsg.setAddress("/quit")
    oscmsg.append(myquit)
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

def print_selection():
    global AUTO
    if (var1.get() == 1):# & (var2.get() == 0):
        l.config(text='回归原始时间线')
        var2.set(0)
        var3.set(0)
        AUTO = True
    elif (var2.get() == 0 & var3.get() == 0):
        l.config(text='请先选择拍对拍或是音符')
        var1.set(1)
        
def print2_selection():
    global AUTO
    if (var2.get() == 1):
        l.config(text='新模式')
        var1.set(0)
        var3.set(0)
        quitmax(1)
        to252("/nEW")
        to253("/nEW")                    
        to243(0)
        to245(0)
        to247(0)
        AUTO = False
    elif (var3.get() == 0):
        var1.set(1)
        l.config(text='回归原始时间线')
        
def print3_selection():
    global AUTO  
    if (var3.get() == 1):  
        l.config(text='旧模式')
        var1.set(0)
        var2.set(0)
        quitmax(2)
        to252("/oLD")
        to253("/oLD")
        AUTO = False        
    elif (var2.get() == 0):
        var1.set(1)
        l.config(text='回归原始时间线')
        
def groupcheck():
    global AUTO
    NOW = datetime.datetime.now()
    while True:
        NOW = datetime.datetime.now()
        if False == AUTO:
            pass
        elif NOW.hour == 9 and NOW.minute == 28 and NOW.second == 30:
            quitmax(1)
            to252("/nEW")
            to253("/nEW")
            time.sleep(0.5)
        elif NOW.hour >= 9 and NOW.hour < 22:
            if NOW.minute == 28:
                if NOW.second == 30:
                        quitmax(1)
                        to243(1)
                        to245(1)
                        to247(1)
                        to252("/nEW")
                        to253("/nEW")
                        time.sleep(0.5)
            elif NOW.minute == 58:
                if NOW.second == 30:
                        quitmax(2)
                        to252("/oLD")
                        to253("/oLD")
                        time.sleep(0.5)
        time.sleep(0.5)
AUTO = True        
var1 = tk.IntVar()
var2 = tk.IntVar()
var3 = tk.IntVar()
c1 = tk.Checkbutton(window, text='自动排程', variable=var1, onvalue=1, offvalue=0,
                    command=print_selection)
c2 = tk.Checkbutton(window, text='拍对拍游戏', variable=var2, onvalue=1, offvalue=0,
                    command=print2_selection)
c3 = tk.Checkbutton(window, text='音符', variable=var3, onvalue=1, offvalue=0,
                    command=print3_selection)
c1.pack()
c2.pack()
c3.pack()

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
bb = OSCClient()
bb.connect(('192.168.0.252', 6666))   # localhost, port 57120
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

thread.start_new_thread(groupcheck,())

var1.set(1)

window.mainloop()