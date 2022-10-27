import numpy as np
import timeit
import time
from typing import List

def add_map(vector: List[int], change: int) -> List[int]:
    return list(map(lambda x: x + change, vector))

def add_loop(vector: List[int], change: int) -> List[int]:
    for i in range(len(vector)):
        vector[i] += change
    return vector  






def measure_run_diff_try(vec_size: int, num_tests: int) -> float:
    # this function returns the diffecence between numpy array and list
    # in terms of time
    # vec_size: the size of the vector
    # num_tests: the number of tests to run
    # return: the difference between numpy array and list in terms of time
    arr = np.array(range(vec_size))
    list1 = list(range(vec_size))
    time1 = timeit.timeit(lambda: add_map(arr, 1), number=num_tests)
    time2 = timeit.timeit(lambda: add_loop(arr, 1), number=num_tests)
    return (time1 - time2)



def lab_func():
    v = np.array(5)
    print(v.shape)
    print(v)

    v = np.array([1,2,3,4,5])
    print(v.shape)
    print(v)

    v = np.array([[1,2,3,4,5]])
    print(v.shape)
    print(v)

    u = v.reshape((-1, 1))
    print(u)

    m = u*v
    print(m.shape)
    print(m)


    m = v*u
    print(m.shape)
    print(m)

    m = v@u
    print(m.shape)
    print(m)

    m = u@v
    print(m.shape)
    print(m)

    print(v*v)
    # print(v@v) # -> error
    print("------------")

    print(v*10)


    num_interations = 10000
    vector_size = 1000

    py_list = list(range(vector_size))
    start_pytime = time.time()
    for i in range(num_interations):
        py_list = add_loop(py_list , 1)
    print(time.time() - start_pytime)

    numpy_list = np.array(range(vector_size))
    start_nptime = time.time()
    for i in range(num_interations):
        numpy_list += 1
    print(time.time() - start_nptime)



def mult_map(vector: List[int], change: int) -> List[int]:
    return list(map(lambda x: x * change, vector))



def measure_run_diff(vec_size: int, num_tests: int) -> float:
    py_list_total = 0
    numpy_list_total = 0

    for i in range(num_tests):
        py_list = list(range(vec_size))
        start_pylist = time.time()
        for i in range(vec_size):
            py_list[i] *= 3
        py_time = time.time() - start_pylist
        py_list_total += py_time
    print(py_list_total)

    for i in range(num_tests):
        numpy_list = np.array(range(vec_size))
        start_nplist = time.time()
        numpy_list*3
        numpy_time = time.time() - start_nplist
        numpy_list_total += numpy_time
    print(numpy_list_total)

    print(py_list_total - numpy_list_total)    

measure_run_diff(1000, 10000)

