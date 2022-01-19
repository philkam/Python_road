#Compound Data Types
#Python is very flexible in the values of any advanced data type, other than the set.
#We can have anything in the list, dictionary and tuples from strings to integers to float to boolean even
#tuples, dictionary and others.
"""
Examples
my_dict = {1:{1:[1,2,3,"Phil"], 3.2: (1,2,3)}}
my_tuple = (1,2,{1:["tuple",6]})
my_list = [1,(5,1,"a"), 6.6]
"""

#Usage
my_list = [{1: ["ahk", "ca", "bh"]},[2,(3,4,8),4 ], "King"]
print(my_list[0]) #gets the first element from the list
print(my_list[0][1]) #prints the values in the dictionary
print(my_list[0][1][0]) #prints the first value in the dictionary

print(my_list[1]) #prints the second value in the list
print(my_list[1][1][1]) #prints the second value in the tuple of the second list


print(my_list[2]) #prints the last value in the list