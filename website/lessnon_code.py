
import numpy as np
import matplotlib.pyplot as plt

# lets create numpy arrays 

a = np.array([1, 2, 3, 4, 5])
b = np.array([1, -1, 1, -1, 1])


# np array methods

# print(a.shape) # 

# print(a.size) # number of elements

# np.random.seed(0) # seed is used to generate same random numbers everytime 

x1 = np.random.randint(10, size=10)
x2 = np.random.randint(2, size=(5, 3))
x3 = np.random.randint(10, size=(2, 3, 5))
x4 = np.random.randn(10000)
x5 = np.random.randn(10000, 2)

print("x1 :\n", x1)
print("x2 :\n", x2)
print("x3 :\n", x3)
print("x4 :\n", x4)

print("x3 dim: ", x3.ndim)
print("x5 dim: ", x5.ndim)
print("x5 type: ", x5.dtype)

plt.plot(x4)