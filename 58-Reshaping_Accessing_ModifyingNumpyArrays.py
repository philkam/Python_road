#Reshaping
#The shape of the array can be changed using reshape function.
#the new and original shape need to be compatible


#Accessing and Modifying
#You can access specific elements in a Numpy array the same way as with python lists in case of 1D arrays.
#However, higher dimensional arrays accessing and modifying is different from its list's counterparts.

#usage
import numpy as np

my_arr = np.arange(20)
print(my_arr)

#reshaping the way your array looks 5 rows and 4 columns, adding order brings the column first then row later
my_arr_reshaped = np.reshape(my_arr, (5, 4), order = "F")
print(my_arr_reshaped)

#convert 1-D array to 1-D list
my_list = list(my_arr)

#accessing and modifying value in list.
my_arr[1] = 5
my_list[1] =6
print(my_list[1])
print(my_arr[1])

#higher dimension array
my_list_reshaped = list(my_arr_reshaped)
print(my_arr_reshaped[0,1]) #prints 5 which is first row and first value
#print(my_list_reshaped[0,1]) #throws error, list can't be indexed this way
print(my_list_reshaped[0][1]) #prints 5




