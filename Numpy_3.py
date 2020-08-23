import numpy as np

list1 = [[1,1,1],[2,2,2],[3,3,3]]
arr2d = np.array(list1)
print (arr2d)
arr2d.astype('str')
arr2d = arr2d.astype(float)

# can only convert float (confirmation needed)
np.nan
np.inf
arr2d[0][0] = np.nan
arr2d[0][1] = np.inf
print (arr2d)

np.isnan(arr2d)
np.isinf(arr2d)
#for both nan and inf
missing_flag = np.isnan(arr2d) | np.isinf(arr2d)
print (missing_flag)

# Replace inf and nan with 0
arr2d[missing_flag]
arr2d[missing_flag] = 0
print (arr2d)

# Stats ops
# mean, std and variance
arr2d.mean()
arr2d.max()
arr2d.min()
arr2d.std()
arr2d.var() #  Variance is sqr of std
arr2d.cumsum()  # cumulative sum

# to create an array from an array
arr1 = arr2d[:2, :2]
print (arr1)

arr2 = arr2d[1:3, 1:3]
print (arr2)

np.unique(arr2d) # for unique values

#Reshape
a = arr2d.reshape(1,9)
print (a)
a.ndim
arr2d.reshape(9,1)

#when we dont know size of array
# flatten change entire matrix into a signel array (1-d array)
# flatten creates a copy
a = arr2d.flatten()
print (a)
# changes done to 'a' wont affect parent array 'arr2d.flatten'

# ravel is same as flatten, but it creats refrence,
b = arr2d.ravel()
print (b)
# changes done to 'b' will affect parent array 'arr2d.flatten'
# e.g: - 
b[0] = -1
print (arr2d)


# sequence, repetation and random numbers
np.arange(1,5)
np.arange(1,5, dtype = float)
np.arange(1,5, dtype = int)
np.arange(1,5,2)
#np.linspace(1,50,50) # divide 1-50 numbers into 50 parts
#np.logspace(1,50,10)

np.zeros([2,2])
np.ones([2,2])

# repetation
a = [1,2,3]
np.tile(a, 3)   # it will repeat entire array thrice
np.repeat (a,3) # it will every word in an array thrice
np.repeat (arr2d,3)

# Random number
np.random.rand(1,3)     # (1*3) it will create an array of it, between (0-1) always
np.random.rand(3,3)
np.random.randint(1,3, [3,3])

np.random.seed(0)   # fixed due to seed parameter
np.random.randint(1,3, [3,3])

uniques, counts = np.unique(arr2d, return_counts = True)
print (uniques)
print (counts)  # count of unique values

# More about Numpy
arr = np.array([5,7,2,4,6,8,2])
print (arr)

val = np.where(arr>5) # Will show index of values greater than 5
print (val)
print (arr[val])
arr > 5  # Boolean for arr
np.where(arr>5, 'greater than five', 'smaller than five')
arr.max()
arr.argmax()    # it will show index of max value
arr.argmin()    # it will show index of min value

# ============== read and write into a CSV file===========================
# np.genfromtxt(fname)    
# it will read a txt file, which contains different types of datasets
# np.loadtxt(fname)
#it will read a txt file, which contains same types of values

# file is at 'C:\Users\sshar127\Desktop\Learnings\Python Bootcamp'
# first way, with Nan values
np.genfromtxt('Numpy.csv', delimiter = ',', skip_header=1)

#to replace Nan values
data = np.genfromtxt('Numpy.csv', delimiter = ',', skip_header=1, filling_values= 100, dtype = int)
print (data)

data.ndim
data.shape

np.set_printoptions(suppress = True)    # To remove sceintific notations
data[:3] # to pull first 3 rows data

# === When we need to pull text and numbers both - Second way
data1 = np.genfromtxt('Numpy.csv', delimiter = ',', skip_header=1, dtype = None)
print (data1)

# to save file
np.savetxt('Data.csv', data, delimiter = ',')

# to save a numpy error
np.save('data.npy', data)
x = np.load('data.npy')
print (x)

# when we need to add both first and second way
np.savez('data3.npz', data, data1)
y = np.load('data3.npz')
print (y)

y.files # to check files

y['arr_0']
y['arr_1']

# ===== Concate rows n columns wise
arr1 = np.zeros([4,4])
arr2 = np.ones([4,4])
print (arr1)
print (arr2)

# axis = 0 means rows and aixs = 1 is columns
np.concatenate([arr1, arr2], axis = 0)
np.concatenate([arr1, arr2], axis = 1)

# for verticle and horizontal stack
np.vstack([arr1, arr2])
np.hstack([arr1, arr2])

# r_ = row wise concate, c_ = columns wise concate
np.r_[arr1, arr2]
np.c_[arr1, arr2]

# === sorting
arr1 = np.random.randint(1,10, size = [10, 5])
print (arr1)

np.sort(arr1)
np.sort(arr1, axis = 0)
arr1[:, 0] # will pull entire single column
sorted_index = arr1[:, 0].argsort() # sort by index
# arr1 [sorted_index]

# Working with dates
a = np.datetime64('2020-03-26 20:46:00')
print (a)
a+10    #adding seconds here

# Inside a function
def func1(x):
    if x%2 == 1:
        return x**2
    else:
        return x/2

func1(5)

# to use an array in function, we vectorize it
func1_v = np.vectorize(func1, otypes=[float])
func1_v(arr1)





















