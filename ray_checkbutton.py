#!/usr/bin/python
# -*- coding: UTF-8 -*-
import tkinter as tk
from OSC import *
import types
import thread
import time

window = tk.Tk()
window.title('快捷方式')
window.geometry('200x100')

l = tk.Label(window, bg='yellow', width=20, text='请选择')
l.pack()

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

def print_selection():
    if (var1.get() == 1):# & (var2.get() == 0):
        l.config(text='回归原始时间线')
        var2.set(0)
        var3.set(0)
    elif (var2.get() == 0 & var3.get() == 0):
        l.config(text='请先选择拍对拍或是音符')
        var1.set(1)
        
def print2_selection():
    if (var2.get() == 1):
        l.config(text='新模式')
        var1.set(0)
        var3.set(0)
        to252("/nEW")
        to253("/nEW")                    
    elif (var3.get() == 0):
        var1.set(1)
        l.config(text='回归原始时间线')
        
def print3_selection():  
    if (var3.get() == 1):  
        l.config(text='旧模式')
        var1.set(0)
        var2.set(0)
        to252("/oLD")
        to253("/oLD")            
    elif (var2.get() == 0):
        var1.set(1)
        l.config(text='回归原始时间线')
        
def groupcheck():
    while True:
        NOW = datetime.datetime.now()
        if NOW.minute == 15:
            if NOW.second == 0:
                if NOW.hour == 9:
                    #quitmax()
                    to252("/nEW")
                    to253("/nEW")
                    time.sleep(0.5)
        elif NOW.minute == 28:
            if NOW.second == 30:
                    quitmax()
                    to252("/oLD")
                    to253("/oLD")
                    time.sleep(0.5)
        elif NOW.minute == 58:
            if NOW.second == 30:
                    #quitmax()
                    to252("/nEW")
                    to253("/nEW")
                    time.sleep(0.5)
        time.sleep(0.5)
        
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

thread.start_new_thread(groupcheck,())

window.mainloop()