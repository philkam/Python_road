#Pandas DataFrame Manipulation
"""
Accessing Data:
            - Access elements, rows or columns using labels
            - The labels can be single or multiple
            - The labels cn be numerical or with their name
            - Add rows using the append method
            - Add columns using the insert method.
            - Remove specific element using the pop and drop methods.
            - Rename columns and rows using the rename method.
            - We can change the row index name using the set_index method
"""

#usage
import pandas as pd
pd_csv = pd.read_csv("67-covid19_tweets.csv")

print(pd_csv.head())

#Access elements
print(pd_csv.iloc[0,0]) #iloc deals with index whilst loc deals with location that's the difference
print(pd_csv.loc[0,'user_name'])

#Add rows
x = pd.Series([1], name= 'anything')
pd_csv = pd_csv.append(x)
print(pd_csv.head())

##Adding columns
pd_csv.insert(loc= 0, column = "anyone", value= 5)
print(pd_csv.head())
print(pd_csv)

##Remove (pop- drop)
print(pd_csv.drop(labels= 0))

##Rename
print(pd_csv.rename(columns={"anyone":"Anything"}))

##set index
print(pd_csv.set_index("user_name"))