import time
import numpy
import pyaudio
import fluidsynth
import analyse

CHUNK = 4096
pa = pyaudio.PyAudio()
strm = pa.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input_device_index = 0,
    input = True,
    frames_per_buffer = CHUNK
    )

s = []

fl = fluidsynth.Synth()
fl.start('alsa')
# Initial silence is 1 second
#s = numpy.append(s, fl.get_samples(44100 * 1))

sfid = fl.sfload("FluidR3_GM.sf2")
fl.program_select(0, sfid, 0, 0)

while True:
    try:
        rawsamps = strm.read(CHUNK) # Read raw microphone data
        samps = numpy.fromstring(rawsamps, dtype=numpy.int16) # Convert raw data to NumPy array
        rayfeq = analyse.musical_detect_pitch(samps)
        if rayfeq > 0:
            #strm.stop_stream()
            #fl.noteoff(0, rayint)
            rayint = round(rayfeq,1)
            if rayint >= 43 and rayint <= 62:
                rayloud = analyse.loudness(samps)
                print (rayloud, rayfeq)
                rayampval = raymap(rayloud, -17, -2, 0, 127)
                print(rayampval)
                fl.noteon(0, rayint, 127)
            #strm.start_stream()
        else:
            fl.noteon(0, 60, 127)
            time.sleep(5)
    except IOError, e:
        if e.args[1] == pyaudio.paInputOverflowed:
            rawsamps  = '\x00'*CHUNK
        else:
            raise
fl.delete()

