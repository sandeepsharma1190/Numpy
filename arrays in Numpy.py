### arrays in Numpy###
#import numpy as np
from numpy import *
arr = array([1,2,3,4,5])
print(arr.dtype)    # to check datatype

#for int + float values, #Numpy coverts all values automatically
from numpy import *
arr = array([1,2,3,4,5.0])
print(arr.dtype)    # to check datatype

arr+2   # to add 2, we cant performce this operation in list

arr = array([1,2,3,4,5], float) #float will convert all values into float
print(arr.dtype)

'''linspace'''#linspace (start, end and parts)
# lin_arr = linspace(0,15,20) 
#count will start from 0, it will go till 15, but in 20 parts

print (lin_arr)
'''lin_arr = linspace(0,15) in this case, 0 to 15 will be break into 50 parts, 
which is default in linspace'''

#arange (a range)
range_arr = arange(1,15,2)
print (range_arr)       #output : - [ 1  3  5  7  9 11 13]

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
print (id(arr1))    #System address is same
print (id(arr2))
#Shallow copy - if we will make any change in arr1, change will happen in arr2 as well.
arr1[1] = 7 #value will change for arr2 as well
'''or - Shallow copy (same as above)'''
arr1 = array([1,2,3,4,5])
arr2 = arr1.view()
print (arr1)
print (arr2)
print (id(arr1))    #System address is different now
print (id(arr2))

'''or Deep copy'''
arr1 = array([1,2,3,4,5])
arr2 = arr1.copy()
print (arr1)
print (arr2)
print (id(arr1))    #System address is different now
print (id(arr2))
arr1[1] = 7     #Wont make changes in arr2

















