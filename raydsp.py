from pyo import *

s = Server(audio="jack").boot()
s.start()
a = SfPlayer("/home/pi/Shanghai/wav/Strat F- 52.wav", loop=False, mul=.4)
b = Freeverb(a, size=[.79,.8], damp=.9, bal=.3).out()
time.sleep(10)
print("ray")
