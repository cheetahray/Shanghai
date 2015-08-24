#!/usr/bin/env python
import numpy
import pyaudio
import analyse
import commands
import time
import math
import wave

chunk = 1024
#wf = wave.open('thesong.wav', 'rb')
pyaud = pyaudio.PyAudio()
lastfeq = 0

#print(pyaud.get_format_from_width(wf.getsampwidth()))
#print(wf.getnchannels())
#print(wf.getframerate())

stream = pyaud.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input = True,
    output = True)

while True:
    # Read raw microphone data
    rawsamps = stream.read(chunk)
    # Convert raw data to NumPy array
    samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
    rayfeq = analyse.musical_detect_pitch(samps)
    #print (analyse.loudness(samps), rayfeq)
    if rayfeq > 0 and math.fabs(rayfeq-lastfeq) > 2:
        print (analyse.loudness(samps), rayfeq)
        wf = wave.open('thesong.wav', 'rb')
        stream.close()
        stream = pyaud.open(
            format = pyaud.get_format_from_width(wf.getsampwidth()),
            channels = wf.getnchannels(),
            rate = wf.getframerate(),
            input = False,
            output = True)
        data = wf.readframes(chunk)
        while data != '':
            stream.write(data)
            data = wf.readframes(chunk)
        wf.close()
        stream.close() 
        stream = pyaud.open(
            format = pyaudio.paInt16,
            channels = 1,
            rate = 44100,
            input = True,
            output = False)
        lastfeq = rayfeq
    else:
        lastfeq = 0

pyaud.terminate()
