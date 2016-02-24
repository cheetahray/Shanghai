# Read in a WAV and find the freq's
import pyaudio
import wave
import numpy as np
import pitchtools

chunk = 8192

# open up a wave
#wf = wave.open('test-tones/440hz.wav', 'rb')
swidth = pyaudio.paInt16
RATE = 44100
# use a Blackman window
window = np.blackman(chunk)
# open stream
p = pyaudio.PyAudio()
stream = p.open(format = swidth,
                channels = 1,
                rate = RATE,
                input_device_index = 0,
                input = True,
                output_device_index = 0,
                output = False,
                frames_per_buffer = chunk
)

# read some data
while True:
    try:
        data = stream.read(chunk)
        # play stream and find the frequency of each chunk

        # while len(data) == chunk*swidth:

        # write data out to the audio stream
        #stream.write(data)
        # unpack the data and times by the hamming window
        indata = np.array(wave.struct.unpack("%dh"%(len(data)*4/swidth),\
                                         data))*window
        # Take the fft and square each value
        fftData=abs(np.fft.rfft(indata))**2
        # find the maximum
        which = fftData[1:].argmax() + 1
        # use quadratic interpolation around the max
        if which != len(fftData)-1:
            y0,y1,y2 = np.log(fftData[which-1:which+2:])
            x1 = (y2 - y0) * .5 / (2 * y1 - y2 - y0)
            # find the frequency and output it
            thefreq = (which+x1)*RATE/chunk
        else:
            thefreq = which*RATE/chunk
        thenote = pitchtools.f2m(thefreq)
        #if thenote > 30 and thenote < 90:
        print "The freq is %f Hz. Note is %f" % (thefreq, thenote)
    except IOError, e:
        if e.args[1] == pyaudio.paInputOverflowed:
            pass
        else:
            raise
stream.close()
p.terminate()
