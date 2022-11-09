from typing import Iterable, Set
import numpy as np
def fix_me(numbers: Iterable[int]) -> Iterable[int]:
    # Return all the even numbers in the parameter numbers.
    return [num for num in numbers if not num%2] 


#print(fix_me(list(range(100))))    
    

def get_shared_items(sets: Iterable[Set[int]]) -> Set[int]:
    # Return the set of numbers that are shared by all sets
    return set.intersection(*sets)


def get_randoms(divby: int) -> int:
    """
    Return a random number ranged betwee 1 and 1000 that is divisable by divby.
    Generate numbers using np.random.randint until you get such a number.
    """
    rand = np.random.randint(1,1000)
    return rand if not rand%divby else get_randoms(divby)


def inner_product_r(v1: Iterable[float], v2: Iterable[float]) -> float:
    sum = 0
    for i in range(len(v1)):
        sum+=v1[i]*v2[i]
    return sum     

def inner_product_c(c1: Iterable[complex], c2: Iterable[complex]) -> complex:
    sum = 0
    for i in range(len(c1)):
        sum+=c1[i]*complex.conjugate(c1[i])
    return sum
    

def inner_product_c_onliner(c1: Iterable[complex], c2: Iterable[complex]) -> complex:
    return sum(map(lambda x : x[0]*x[1].conjugate(), zip(c1, c2)))

# (8 + 3i, −2 + 91i, 3 − 2i, 4), (3.1 − 1.4i, 3 − 9i, −21i, 1 + 12i)
c = complex

print(inner_product_c_onliner([c(8,3), c(-1,91),c(3,-2), c(4,0)],[c(3.1, 1.4), c(3,-9), c(0, -21), c(1, 12)]))





