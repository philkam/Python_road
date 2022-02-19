#Numpy Array
"""
-Fundamental unit of Numpy library.
-It is a multi-dimensional array where all the elements have the same data type.
-Can be created using NumPy functions or by converting Python lists to Numpy Arrays
-It is standard to import Numpy and give it an alias which is np which using the following line
        import numpy as np
-Convert a python list to numpy array using np.asarray function.
-We can get the shape and the data type of the array element using shape a nd dtype attributes.
-Numpy has its own data types which are different from the python ones.
"""

import numpy as np
my_list = [1, 2, 3]
#converting list to numpy array
my_arr = np.asarray(my_list)
print(my_arr) #prints the numpy array
print(my_arr.dtype) #prints the datatype of the array
print(my_arr.shape) #prints the shape of the array

#print numpy array of all zeros
np_zeros = np.zeros((5, 5), dtype=int)
print(np_zeros)

#print numpy array of all ones
np_ones = np.ones((5,5))
print(np_ones)

#prints range of values from start to finish
np_range = np.arange(start=2, step=2, stop=20)
print(np_range)

np_linspace = np.linspace(start=2, stop=20, num = 10)
print(np_linspace)

