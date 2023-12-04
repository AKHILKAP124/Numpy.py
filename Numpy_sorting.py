import numpy as np

array = np.array([[1,11,9],
                  [4,5,1]])

sort1 = np.sort(array) # sort axis 1 by default (Rows)
sort0 = np.sort(array, axis=0) # sort axis 0 (Columns)

print(" ")
print("Sorted Rows are =",sort1)
print(" ")
print("Sorted Columns are =",sort0)
