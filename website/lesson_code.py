import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time

def innerProduct(v1, v2, normal=1):
    ip = sum(v1 * v2)
    if(normal == 1):
        n1 = np.sqrt(sum(v1 * v1))
        n2 = np.sqrt(sum(v2 * v2))
        ip /= n1 * n2
    return ip        

    


f0 = 1000  # Hz
fs = 10000 # frames per second
duration = 10 # seconds
time_signal = 0.7  
n_signal = int(time_signal * fs) # number of frames in signal
Ts = 1/fs # seconds per frame
L = int(fs * duration) # number of frames in total 
nn_signal = np.linspace(0, time_signal, n_signal) # time vector for signal
time_total = np.linspace(0, duration, L) # time vector for total
t_start = 7
n_start = int(t_start * fs)
frame = n_signal
step = 100


x_noise = np.random.randn(L) # noise signal
plt.plot(time_total[:step], x_noise[:step])
#plt.show()
signal = np.cos(2 * np.pi * f0 * nn_signal)
plt.plot(nn_signal[:step], signal[:step])
#plt.show()
xn_signal = np.copy(x_noise)
xn_signal[n_start : n_start + n_signal] += 0.2*signal
plt.plot(time_total[n_start-10000 : n_start + 10000 + n_signal], xn_signal[n_start - 10000 : n_start + n_signal + 10000])
#plt.show()

j = 0
ip_len = int((L - frame) / step)
ip = np.zeros(ip_len)
nn_ip = np.arange(0, ip_len) * step
time_total_ip = nn_ip * Ts

for j in range(ip_len):
    x_test = xn_signal[j * step : j * step + frame]
    ip[j] = innerProduct(x_test, signal, 1)

plt.plot(ip)
plt.show()

toa = np.where(ip == np.max(ip))

nn_signal = np.linspace(0,1, n_signal)
mu = 0.1 
x_chirp = np.cos(2*np.pi * f0 * nn_signal + 2*np.pi * mu * nn_signal**2)
plt.plot(x_chirp[:-250])
plt.show()
# t = np.arange(0, 5, Ts)
# y = np.cos(2* np.pi * t * f0)
# sd.play(signal, f0, blocking=True)
# time.sleep(1)
# sd.stop()
