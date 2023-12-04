# Slicing Function
import numpy as np
arr = np.array([0,1,2,3,4])
print("Array =",arr)

# change the Element of Array
a = arr[2:5]

a[1] = 10
print(a)
print("Array After Slice =",arr)
print(" ")

# To Avoid this type of bug in program, make copy of array by "copy()"
print("In this Use copy()")
arr = np.array([0,1,2,3,4])
print("Array =",arr)

b = arr[2:5].copy()

b[1] = 10
print(b)
print("Array After Slice =",arr)
