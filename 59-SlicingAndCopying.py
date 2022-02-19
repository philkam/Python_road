#Slicing and copying
"""
##[rows, columns]
## [start:end, start:end]
-The copy function is used if you want to work on a subarray without manipulating the original one.
"""

import numpy as np

#the seed function allows us to have the same random number irrespective of the number of times the code is run
np.random.seed((0))
np_rand = np.random.random((3,3))
print(np_rand)

#we want to slice rows 0 and 1 and column 0 and 1
print(np_rand[0:2, 0:2])

#we want first three rows and only first column
print(np_rand[0:3,0])

#storing in sliced numbers in new variable
#np_sub_rand = np.copy(np_rand[0:3,0]) #comment  out this to understand comment #NB
np_sub_rand =  np_rand[0:3,0]   #comment  this to understand #NB
print(np_sub_rand)

#modifying the first value in the array
np_sub_rand[0] = 1000
print(np_sub_rand)

#NB
# #we can see that if we modify a value in the array it affects the even the original array so we need to copy
print(np_rand)  #original array has been affected



