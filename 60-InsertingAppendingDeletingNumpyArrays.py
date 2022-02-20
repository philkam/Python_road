#Inserting
#With the insert method, you can specify where you want to add new elements

#Appending
#The append method is for concatenation new elements, so they are added after the original array elements.
#If the axis parameter is not used, the output will be 1-D array.
#If not, the added elements must have the same shape as the original array.

#Deleting
#You can delete elements form a 1D Numpy array using delete function.
#You can delete elements from a higher NumPy array using delete function by specifying the axis parameter.

#NB obj is the index, axis refers to row or column 0 is row 1 is column

#Usage
import numpy as np

np_arr = np.array([[1,2], [6,8]])
print(np_arr)
print(np_arr.shape)

np_arr_insert = np.insert(arr = np_arr, obj = 1, values=[3,4], axis=1)
print(np_arr_insert)

np_arr_append = np.append(arr=np_arr, values=[[3,4], [1,2]], axis=0)
print(np_arr_append)


np_arr_delete = np.delete(arr=np_arr,obj = 1, axis = 0)
print(np_arr_delete)
