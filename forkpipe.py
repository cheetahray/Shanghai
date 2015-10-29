import os, sys, time

r,w=os.pipe()
r,w=os.fdopen(r,'r',0), os.fdopen(w,'w',0)
direction = -1

pid = os.fork()
if pid:          # Parent
    w.close()
    while 1:
        data=r.readline()
        if not data:
            break
        else:
            print "parent Direction: " + data.strip()
            direction = direction * -1
else:           # Child
    r.close()
    for i in range(10):
        direction = direction * -1 
        print >>w, "Direction is %s" % direction
        w.flush()
        time.sleep(1)
