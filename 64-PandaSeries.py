#Panda Series
"""
-One dimensional objects.
-Capable of holding any data type (integers, strings, floating point numbers, python objects)
-Can assign an index for each element in the series.
-It is a convention to import pandas as pd.
Series Basic Attributes: shape, ndim, size, values, index.
"""

import pandas as pd
import numpy as np

##from ndarray
np_arr = np.array([1, 2,3,7])
series_np= pd.Series(np_arr)
print(series_np) #the index and values are printed.

##from list
series_list = pd.Series([1, 10, 3])
print(series_list)

##from dictionary
di = {"First": 3, "Second": 2.1, "Apple": "Orange"}
series_dict = pd.Series(di)
print(series_dict)
#print(series_dict['First'])

##from scalar value
scalar_value = 10
series_scalar = pd.Series(scalar_value, index=[0,1,2,3,4])
print(series_scalar)
