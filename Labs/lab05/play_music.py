import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time


def create_sin(seconds, fs, freq):
    x = np.arange(0, seconds, 1/fs)
    return np.sin(2 * np.pi * x * freq)

def create_tone(seconds, fs, freqs):
    return sum(map(lambda freq: create_sin(seconds, fs, freq), freqs))

def play_tone(seconds, fs, freqs):
    tone = create_tone(seconds, fs, freqs)
    sd.play(tone, fs)
    time.sleep(seconds)
    sd.stop()

def main():
    play_tone(1, 44100, (1209, 697))
    
main()