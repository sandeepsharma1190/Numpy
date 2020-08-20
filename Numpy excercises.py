'''100 Numpy excercises'''

import numpy as np
print(np.__version__)
print(np.show_config)

Z = np.zeros(10)
print (Z)
Z[4] = 1


'''Create a vector with values ranging from 10 to 49'''
Z = np.arange(10,49)
print(Z)

'''Reverse a vector (first element becomes last)'''
a = np.arange(50)
print(a[::-1])

'''Create a 3x3 matrix with values ranging from 0 to 8'''
a = np.arange(9).reshape(3,3)
print(a)

'''Find indices of nonzero elements from [1,2,0,0,4,0]'''
nz = np.nonzero ([1,2,0,0,4,0])
print (nz)

'''Create a 3x3 identity matrix'''
idm = np.eye(3)
print(idm)

'''Create a 3x3x3 array with random values'''
rand = np.random.random((3,3,3))
print(rand)

'''Create a 10x10 array with random values and find the minimum and maximum values'''
a = np.random.random((10,10))
amin, amax = a.min(), a.max()
print (amin, amax)

'''Create a random vector of size 30 and find the mean value'''
a = np.random.random(30)
m = a.mean()
print(m)

'''Create a 2d array with 1 on the border and 0 inside'''
z = np.ones((10,10))
z[1: -1, 1: -1] = 0
print(z)

'''Booleans in Numpy'''
0 * np.nan
np.nan == np.nan
np.inf > np.nan
np.nan - np.nan
0.3 == 3 * 0.1

'''Create a 5x5 matrix with values 1,2,3,4 just below the diagonal'''
a = np.diag(1+np.arange(4), k = -1)
print (a)

'''Create a 8x8 matrix and fill it with a checkerboard pattern'''
Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)

'''Consider a (6,7,8) shape array, what is the index (x,y,z) of the 100th element'''
print(np.unravel_index(100,(6,7,8)))

'''Create a checkerboard 8x8 matrix using the tile function'''
Z = np.tile(np.array([[0,1],[1,0]]), (4,4))
print(Z)

'''Normalize a 5x5 random matrix'''
Z = np.random.random((5,5))
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)

'''Create a custom dtype that describes a color as four unisgned bytes (RGBA)'''
color = np.dtype([("r", np.ubyte, 1),
                  ("g", np.ubyte, 1),
                  ("b", np.ubyte, 1),
                  ("a", np.ubyte, 1)])

'''Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)'''
Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)

'''Given a 1D array, negate all elements which are between 3 and 8, in place.'''
Z = np.arange(11)
Z[(3 < Z) & (Z <= 8)] *= -1
print (Z)

print(sum(range(5),-1))
from numpy import *
print(sum(range(5),-1))





Z = np.random.uniform(-10,+10,10)
print (np.trunc(Z + np.copysign(0.5, Z)))



















