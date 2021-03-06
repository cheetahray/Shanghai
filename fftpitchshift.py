#!/usr/bin/env python

from scipy.io import wavfile
import argparse
import numpy as np
import pygame
import sys
import warnings
from pyo import *

def speedx(snd_array, factor):
    """ Speeds up / slows down a sound, by some factor. """
    indices = np.round(np.arange(0, len(snd_array), factor))
    indices = indices[indices < len(snd_array)].astype(int)
    return snd_array[indices]


def stretch(snd_array, factor, window_size, h):
    """ Stretches/shortens a sound, by some factor. """
    phase = np.zeros(window_size)
    hanning_window = np.hanning(window_size)
    result = np.zeros(len(snd_array) / factor + window_size)

    for i in np.arange(0, len(snd_array) - (window_size + h), h*factor):
        # Two potentially overlapping subarrays
        a1 = snd_array[i: i + window_size]
        a2 = snd_array[i + h: i + window_size + h]

        # The spectra of these arrays
        s1 = np.fft.fft(hanning_window * a1)
        s2 = np.fft.fft(hanning_window * a2)

        # Rephase all frequencies
        phase = (phase + np.angle(s2/s1)) % 2*np.pi

        a2_rephased = np.fft.ifft(np.abs(s2)*np.exp(1j*phase))
        i2 = int(i/factor)
        result[i2: i2 + window_size] += hanning_window*a2_rephased.real

    # normalize (16bit)
    result = ((2**(16-4)) * result/result.max())

    return result.astype('int16')

def pitchshift(snd_array, n, window_size=2**13, h=2**11):
    """ Changes the pitch of a sound by ``n`` semitones. """
    global raydiv
    factor = 2**(1.0 * n / ( 12.0 * raydiv )  )
    stretched = stretch(snd_array, 1.0/factor, window_size, h)
    return speedx(stretched[window_size:], factor)


def parse_arguments():
    global raymid 

    description = ('Use your computer keyboard as a "piano"')

    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        '--wav', '-w',
        metavar='FILE',
        type=argparse.FileType('r'),
        default='/home/pi/Shanghai/wav/guitar/' + str(raymid) + '.wav',
        help='WAV file (default: ' + str(raymid) + '.wav)')
    parser.add_argument(
        '--keyboard', '-k',
        metavar='FILE',
        type=argparse.FileType('r'),
        default='/home/pi/pianoputer/typewriter.kb',
        help='keyboard file (default: typewriter.kb)')
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='verbose mode')

    return (parser.parse_args(), parser)

def raysound(arr):
    t = DataTable(size=len(arr), init=arr.T.tolist())
    return TableRead(t, freq=t.getRate(), loop = False, mul = .0001)

def main():

    global raydiv 
    raystart = -100

    s = Server(audio="jack",duplex=0).boot()
    s.start()

    # Parse command line arguments
    (args, parser) = parse_arguments()

    # Enable warnings from scipy if requested
    if not args.verbose:
        warnings.simplefilter('ignore')

    fps, sound = wavfile.read(args.wav.name)

    tones = range(raystart, -50)
    sys.stdout.write('Transponding sound file... ')
    sys.stdout.flush()
    transposed_sounds = [pitchshift(sound, n) for n in tones]
    print('DONE')

    # So flexible ;)
    #pygame.mixer.init(fps, -16, 1, 100)
    # For the focus
    #screen = pygame.display.set_mode((150, 150))

    #keys = args.keyboard.read().split('\n')
    sounds = map(raysound, transposed_sounds)   
    #key_sound = dict(zip(keys, sounds))
    #is_playing = {k: False for k in keys}

    raycnt = 0.0
    for i in sounds:
        rayint = raymid + (raystart + raycnt)/raydiv
        print(rayint)
        rec = Record(i.out(), chnls=1, filename="/home/pi/Shanghai/wav/rayguitar/" + str("%.1f" % rayint) + ".wav")
        Clean_objects(4.5, rec).start()
        raycnt = raycnt + 1
        time.sleep(4.5)

    #while True:
        #event = pygame.event.wait()

        #if event.type in (pygame.KEYDOWN, pygame.KEYUP):
        #    key = pygame.key.name(event.key)

        #if event.type == pygame.KEYDOWN:
        #    if (key in key_sound.keys()) and (not is_playing[key]):
        #        key_sound[key].play(fade_ms=50)
        #        is_playing[key] = True

        #    elif event.key == pygame.K_ESCAPE:
        #        pygame.quit()
        #        raise KeyboardInterrupt

        #elif event.type == pygame.KEYUP and key in key_sound.keys():
             # Stops with 50ms fadeout
        #    key_sound[key].fadeout(50)        
        #    is_playing[key] = False
raydiv = 10.0 
raymid = 53

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Goodbye')
