import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import time

C = complex

def normip(v,p=2):
    """
    function to compute the natural norm of an input vector.
    Inputs: v - a numpy array (n dim vector) // complex or real
    Outputs: natural norm of v
    """
    # your code here
    return np.sum(np.abs((v**p)))**(1/p)


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

def make_face():
    x = np.zeros([8,8])
    x[1, 1:3]    = 1   # left eye
    x[1, 5:7]    = 1   # right eye
    x[3, 3:5]    = 1   # nose
    x[5:7, 1::5] = 1   # dimples
    x[6, 2:6]    = 1   # mouth
    #plt.imshow(x, cmap='gray')
    #plt.show()
    return x

def flip_vals(npa):
    frame = np.ones([npa.shape[0],npa.shape[1]])
    for i in range(len(npa)):
        for j in range(len(npa[i])):
            if npa[i][j] == 1:
                frame[i][j] = 0
    # plt.imshow(frame, cmap='gray')
    # plt.show()
    return frame


def proximity(matA, matB):
    return np.sum(matA.conjugate() * matB)


def similarity(matA,matB):
    return (proximity(matA,matB))/(normip(matA)*normip(matB))


if __name__ == "__main__":
    def main():
        v = np.array([1, C(0,2), -3, 1, 7])
        # q1.1
        print(normip(v))
        # q1.2
        v2 = np.array([1,5,C(0,3),C(-1, 1),2])
        print([*v2[:]/normip(v2)], sep=", ")
        # q1.3
        v3 = np.array([6,7,C(0,1),C(0,2),7])
        u  = np.array([2,1,C(0,-2), -3, 8])
        print(normip(v3-u))

        #q2.1
        cosine_series_1()
        ## i can hear the sound until 19000
        #q2.2 // the defualt is 432 for making it sound more harmonies
        cosine_series_2(440)

        #q3.1
        bw = make_face()
        plt.imshow(bw, cmap='gray')
        plt.show()
        wb = flip_vals(bw)
        plt.imshow(wb, cmap='gray')
        plt.show()
        p = proximity(bw,bw)

        print(similarity(wb,wb))
    main()