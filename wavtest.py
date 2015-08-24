import numpy
import pyaudio
import analyse
import commands
import time
import math
import wave

# Initialize PyAudio
pyaud = pyaudio.PyAudio()
CHUNK = 8192
lastfeq = 0

# Open input stream, 16-bit mono at 44100 Hz
# On my system, device 2 is a USB microphone, your number may differ.
stream = pyaud.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input_device_index = 0,
    input = True,
    output_device_index = 1,
    output = True,
    frames_per_buffer=CHUNK)

while True:
    # Read raw microphone data
    rawsamps = stream.read(CHUNK)
    # Convert raw data to NumPy array
    samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
    # Show the volume and pitch
    rayfeq = analyse.musical_detect_pitch(samps)
    if rayfeq > 0 and math.fabs(rayfeq-lastfeq) > 2:
        print (analyse.loudness(samps), rayfeq)
        #stream.stop_stream()
        wf = wave.open('thesong.wav', 'rb')
        data = wf.readframes(CHUNK)
        while data != '':
            stream.write(data)
            data = wf.readframes(CHUNK)
        wf.close()
        #title=commands.getoutput("echo \"with_fx :reverb, mix: 0.9, phase: 0.25, room: 1 do sample :guit_em9, rate: 0.5 end\" | sonic_pi")
        time.sleep(10)
        #title=commands.getoutput("echo \"stop\" | sonic_pi")
        #stream.start_stream()
        lastfeq = rayfeq
    else:
        lastfeq = 0
