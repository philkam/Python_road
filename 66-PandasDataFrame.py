#Panda DataFrame
"""
-Two-dimensional data structure(consist of rows and columns).
-Can be imagined as a dictionary for series objects.
-Each column of the DataFrame is a Series object.
-We can create a dataframe by reading a CSV file.
-Basic attributes: shape, ndim, size, values, index, columns
"""

import pandas as pd
import numpy as np

##Dict of series/dict
di = { "tweet": [1,2,3], "user_name":["ahmed","mohamed","john"], "verified":[True, False, False]}
df_di = pd.DataFrame(di)
print(df_di)

##from dictionary of series
di_series = {"tweet": pd.Series([1,2,3]), "user_name": pd.Series(["ahmed","mohamed","john"]), "verified":pd.Series([True, False, False])}

df_di_series = pd.DataFrame(di_series)
print(df_di_series)

#from dictionary of ndarrays/lists
my_list = [1, 5, 2]
df_list = pd.DataFrame(my_list, columns=["list"])
print(df_list)

#from a list of dicts
list_dicts = [{"a":2, "c":4.5}, {"b": 4, "g":1}]
df_list_dict = pd.DataFrame(list_dicts)
print(df_list_dict)

##2-D numpy array
np_arr = 4.5*np.ones((3,3))
df_np = pd.DataFrame(np_arr)
print(df_np)

#a series
ser = pd.Series([1,2,6])
df_ser = pd.DataFrame(ser)
print(df_ser)

#Another Dataframe
df_ser2 = pd.DataFrame(df_ser)
print(df_ser2)

##from csv file
# pd_csv = pd.read_csv("covid19_tweets.csv")
# print(pd_csv.head())