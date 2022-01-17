#Dictionary
#It is a key-value pair structure.
#IT can be indexed but with its key. Keys are unique.
#IT can be created using curly brackets {} and colon :
#The keys that are not unique will overwrite the latest key value.
#The in keyword is used to check if the key exist.
#The get function is used to get the values of the key without the syntax error.
#You can use a list in a dictionary.

#Usage
my_dict = {1:"Phil", "kay": 4.3, 35: 8, "kenzy": [13, 53, 88, "kofi"]}
print(type(my_dict))

#my_dict[0] #key error: this value cannot be returned
print(my_dict[1]) #this prints the value of the key

#if you are not sure a key exists, use get function to prevent the code from stopping in the middle.
print("hello")
#print(my_dict[0]) #code stops if this is used but
print(my_dict.get(0)) #code checks if there is a 0 key and still runs. This is safer if you are not sure key exists.
print("hi")

