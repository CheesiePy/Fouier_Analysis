import numpy as np
import matplotlib.pyplot as plt
import time
import sounddevice as sd

fs = 44100 # sampling rate
Ts = 1 / fs # sampling interval
f0 = 440 # frequency of the signal

tt = np.arange(0, 1-Ts, Ts) # time vector
xx = np.sin(2 * np.pi * f0 * tt) # signal vector
yy = np.cos(2 * np.pi * f0 * xx) # signal vector
# plt.plot(xx, tt)
# plt.show()
# data = np.random.uniform(-1, 1, fs)
sd.play(xx, fs, blocking=True)
