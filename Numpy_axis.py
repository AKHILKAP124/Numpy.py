import numpy as np

array1 = np.array([[0,1,1],
                  [4,5,1]])
array2 = np.array([[2,3],
                  [1,2],
                  [9,10]])

# axis = 1 is Row and axis = 0 is Column
# Sum of axis
Sum = array1.sum(axis=1)
Sum1 = array1.sum(axis=0)

# Dot Function
dot = np.dot(array1,array2)
# Cross Product 
cross =np.cross(array1,array2.transpose())

print(" ")
print("Array1 is:",array1)
print(" ")
print("Array2 is:",array2)
print(" ")
print("Sum of axis 1 that are Rows =",Sum)
print(" ")
print("Sum of axis 0 that are Column =",Sum1)
print(" ")
print("Dot Product of array1 and array2 =",dot)
print(" ")
print("Cross Product of array1 and array2 =",cross) 
