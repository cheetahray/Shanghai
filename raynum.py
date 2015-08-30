import numpy
import pyaudio
import analyse

# Initialize PyAudio
pyaud = pyaudio.PyAudio()
CHUNK = 8192

# Open input stream, 16-bit mono at 44100 Hz
# On my system, device 2 is a USB microphone, your number may differ.
stream = pyaud.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input_device_index = 1,
    input = True,
    output_device_index = 1,
    output = False,
    frames_per_buffer=CHUNK
    )

while True:
    # Read raw microphone data
    rawsamps = stream.read(CHUNK)
    # Convert raw data to NumPy array
    samps = numpy.fromstring(rawsamps, dtype=numpy.int16)
    # Show the volume and pitch
    print (analyse.loudness(samps), analyse.musical_detect_pitch(samps))
