

import numpy as np

# while creating a numpy array, any data type from above can be explicitly specified.
myArray = np.arange(10)
print(myArray)          # [0 1 2 3 4 5 6 7 8 9]

myArray = np.array(myArray, dtype = np.float32)
print(myArray)          # [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9.]

myArray = np.array(myArray, dtype = np.complex64)
print(myArray)          # [ 0.+0.j  1.+0.j  2.+0.j  3.+0.j  4.+0.j  5.+0.j  6.+0.j  7.+0.j  8.+0.j  9.+0.j]
