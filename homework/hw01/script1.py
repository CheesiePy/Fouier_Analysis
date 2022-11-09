import numpy as np
from matplotlib import pyplot as plt
import innerProd as ip

def main():
    Ts = 1 / 44100
    x = np.arange(0, 1 - Ts, Ts)

    y1 = np.cos(2 * np.pi * 1 * x)
    plt.plot(x, y1)
    plt.show()

    y2 = np.sin(2 * np.pi * 1 * x)
    plt.plot(x, y1, 'b', x, y2, 'r')
    plt.show()

    print(ip.inner_prod(y1, y2))


main()
