import numpy as np
a = np.array([[1,2,3],[4,5,6]])
b = np.array([1,3,5], dtype = 'int16')
print(a)

a.ndim          #to check dimension
a.shape         #to check shape
a.dtype         #to check datatype
a.itemsize      # for item size
a.size          #to get full size

a = np.array([[1,2,3,4], [5,6,7,8]])
print(a)

# to get a specific element [Rows, columns]
a[1,2]

a[0,:]          #to get specific row (row 1)
a[:,2]          #to get specific row (column 3)
a[0,1:4:2]      # start, end, step

my_list = [1,2,3,4,5,6]
array = np.array(my_list, dtype = int)      #dtype not mendatory, but we can explicitly assign datatype using this
print(array)
print(type(array))
array2 = array.reshape(3,2)
print(array2)
array2.shape        #will return the shape of an array
array3 = array.reshape(3,-1)

# 2d array
list1 = [[1,1,1],[2,2,2],[3,3,3]]
arr2d = np.array(list1)
type(arr2d)

print (arr2d[0]) #[1 1 1] first line of matrix
print (arr2d[0][0]) #to pull 1 value in 1 line
#[0][0] rows- [0] and columns - [0]

print(arr2d.dtype)

# Boolean
boolarr = arr2d<3
print (boolarr)

arr2d[boolarr] 
# will show true bools

# for 1-d array single round bracket
# for 2-d array double round bracker
# for 3-d array three round bracker
np.zeros((3,3))
np.zeros(((3,3,3,)))
np.zeros((3,3)) + 5


arr2d_2 = np.array(list1, dtype = float)
print (arr2d_2)
'''to convert dtype'''
arr2d_2.astype('int')
'''to convert into list'''
arr2d_2.tolist()

#to reverse
arr2d[::-1]
arr2d[::-1, ]
arr2d[::-1, ::-1]

'''Nested python lists'''
#my_list1 = [1,2,3,4,5]
#my_list2 = [2,3,4,5,6]
#my_list3 = [9,5,7,3,4]
#
#new_array = np.array[my_list1, my_list2, my_list3]
#print(new_array)
#print(new_array.shape)

# 3d array
x = [[[1,2,3],[1,2,3],[1,2,3]], [[1,2,3],[1,2,3],[1,2,3]], [[1,2,3],[1,2,3],[1,2,3]]]
y = np.array(x)
print (y)

# question
r = range(0, 24)
a = np.arange(24)
print (a)
print (a.ndim)
b = a.reshape(6,4,1)

# to create a 3d array
import array as arr
import numpy as np
arr1 = np.array([[1,2,3,4,5,6], [4,5,6,7,8,9]])

# for 2d
arr2 = arr1.reshape(3,4)

# for 3d
arr3d = arr1.reshape(3,2,2)
'''(in (3,2,2) - we have three 3d array, each with 2 rows 
(1-d array) and 2 columns (each 1-d array with 2 values))'''

# 3x3 numpy array of all values equal = true
np.full((3,3), True)

# By using which syntax you can replace all odd number in the given array with -1
arr[arr%2 ==1] = -1






