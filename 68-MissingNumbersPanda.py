#Dealing with missing data
#Data Cleaning
"""
-Data cleaning is a very important step in data analysis
-Missing values in Pandas are stored as Nan
-You can detect missing values easily using many functions
    *isnull - ensure you dont have missing values
    *dropna - will drop every missing value  in dataset
    *fillna - if you don't want to drop any missing values but you populate missing values
    *interpolate -similar to fillna but works automatically
"""

#usage
import pandas as pd
df = pd.read_csv("69-pokemon.csv")
print(df.head())
print(df.shape) #gives the shape of the dataset

#is null
print(df.isnull())
#for places with values the output is False whilst places without values have boolean True


# ##dropna
# print(df.dropna(inplace=True))
# #comparing to df.shape, the shape of the dataset has reduced. some have been dropped.

# ##fillna
# print(df.fillna(2, inplace=True))
# print(df.isnull()) #there wont be any null values

##interpolate -it has many methods you can use to deal with missing values.
print(df.interpolate('linear'))