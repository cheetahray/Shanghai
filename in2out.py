#!/usr/bin/env python
import pyaudio
import time

pyaud = pyaudio.PyAudio()

def callback(in_data, frame_count, time_info, status):
    return (in_data, pyaudio.paContinue)

stream = pyaud.open(
    format = pyaudio.paInt16,
    channels = 1,
    rate = 44100,
    input_device_index = 0,
    input = True,
    output_device_index = 0,
    output = True,
    stream_callback=callback
    )

stream.start_stream()

while stream.is_active():
    time.sleep(0.1)

stream.stop_stream()
stream.close()

pyaud.terminate()    
