#DFT - Discrete Fourier Transform
#FFT - Fast Fourier Transform

import numpy as np
import matplotlib.pyplot as plt

# 10 seconds of data sampled at 1000 Hz
T = 10.0
fs = 10000
L = T * fs
f0 = 50
x_noise = np.random.randn(0, 1, L)
nn_sig = np.linspace(0, 0.5, fs/2)
sig = np.cos(2 * np.pi * f0 * nn_sig)
x_noise[6*fs:6.5*fs] += sig

