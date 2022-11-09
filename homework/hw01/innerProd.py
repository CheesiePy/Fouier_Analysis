from typing import Iterable
import numpy as np
C = complex

def inner_product(c1: Iterable[complex], c2: Iterable[complex]) -> complex:
    if(len(c1)!=len(c2)):
        raise ValueError("Vectors must be of same length")
    return sum(map(lambda x : x[0]*x[1].conjugate(), zip(c1, c2)))


def main():
    u = np.array([C(0, 2), C(3, 0), C(5, 0), C(-2, 0), C(5, 0)])
    v = np.array([C(0, 1), C(0, -1), C(2, 0), C(1, 0), C(5, 0)])
    w = np.array([C(2, 0), C(3, 0), C(0, -3), C(-1, 0), C(3, 0)])
    print(inner_product(u, 2*v))
    print(inner_product(u,v+2*w))
main()    