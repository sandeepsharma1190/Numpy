### arrays in Numpy###
#import numpy as np
from numpy import *
arr = array([1,2,3,4,5])
print(arr.dtype)    # to check datatype

from numpy import *
arr = array([1,2,3,4,5.0])
print(arr.dtype) 

arr+2

arr = array([1,2,3,4,5], float)
print(arr.dtype)

#linspace
# lin_arr = linspace(0,15,20) 
#count will start from 0, it will go till 15, but in 20 parts

print (lin_arr)

#arange
range_arr = arange(1,15,2)
print (range_arr) 

# zeros
arr_z = zeros(5)
arr_z = np.zeros(10)

# once
arr_o = np.ones(5)
arr_o = ones(15, int)

############# Add values
arr = array([1,2,3,4,5])
arr = arr+5
print (arr)
#[ 6  7  8  9 10]

arr1 = array([1,2,3,4,5])
arr2 = array([3,4,5,6,7])
arr3 = arr1+arr2
print (arr3)

print (np.concatenate([arr1, arr2]))

####### Trignometry
arr1 = array([1,2,3,4,5])
print (sin(arr1))
print (cos(arr1))

print (sqrt(arr1))      #squareroot
print (sum(arr1))
print (min(arr1))
print (max(arr1))

### Copying an array
arr1 = array([1,2,3,4,5])
arr2 = arr1
print (arr1)
print (arr2)
print (id(arr1))
print (id(arr2))
arr1[1] = 7

#Shallow copy
arr1 = array([1,2,3,4,5])
arr2 = arr1.view()
print (arr1)
print (arr2)
print (id(arr1))
print (id(arr2))

'''or Deep copy'''
arr1 = array([1,2,3,4,5])
arr2 = arr1.copy()
print (arr1)
print (arr2)
print (id(arr1))
print (id(arr2))
arr1[1] = 7
