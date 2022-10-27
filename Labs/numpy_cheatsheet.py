"""
NumPy Cheat-Sheet for Python
"""

print("first steps")  
print("______________________NunPy___________________________")
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(np.__version__)

print("To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray")

print(type(arr))
print("______________________________________________________")
a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print("NumPy Arrays provides the ndim attribute that returns an integer that tells us how many dimensions the array have.")
print("dim:",a.ndim)
print("dim:",b.ndim)
print("dim:",c.ndim)
print("dim:",d.ndim) 
print("______________________________________________________")
n5 = np.array([1, 2, 3, 4], ndmin=5)
print(n5)
print("dim:",n5.ndim)