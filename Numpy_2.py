#Numpy_2 

from numpy import *
import numpy as np

x = np.array([[1,2,3,4,5],[5,6,7,8,9]])
print(x.shape)
x[1, 3]     # To get a specific element
x [0, :]    # to get a specific row
x [:, 3]    # to get a specfic column
x[::-1]     # to reverse a vector
x [0, 1:4:2]
x[1,3] = 18   # to change the value
x [:,2] = 99  # To change value of a single particular column with a single value
x [:, 2] = 3,7  # To change value of a single particular column with a multiple values


'''3-D examples'''
import numpy as np
a = np.arange(24).reshape(2,3,4)
print (a.shape)
a[0]

a = np.array([[1,2],[3,4]])
b = np.array([[5,6], [7,8]])




