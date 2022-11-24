def make_show_sound(frequency ,fs=10000):
    fs = fs
    Ts = 1/fs
    f0 = frequency
    t  = np.arange(0,1,Ts)
    x =  np.cos(2 * np.pi * f0 * t)    
    sd.play(x, fs, blocking=True)

    #ploting the cosine function
    plt.plot(t[:100],x[:100])
    plt.grid(axis='both')
    stitle = 'cosine function with freq = ' + str(f0)
    plt.title(stitle)
    #plt.show()
    time.sleep(1)

def cosine_series_1(start=500,stop=20000,jump=500):
    for i in range(start,stop,jump):
        make_show_sound(i)

def cosine_series_2(start=432, stop=20000, jump=2**(1/12)):
    counter = 0
    while start < stop:
        start = start if not counter else start*jump
        make_show_sound(start)
        counter += 1