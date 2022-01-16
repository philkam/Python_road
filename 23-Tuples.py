#Tuples
"""
Special case of list where the elements can not change.
Tuple is immutable.
We create tuples using circular brackets ()
Indexing and slicing are the same as lists.
"""

#Usage
my_tuple = (1, 2, 5.3)
print(type(my_tuple))

print(my_tuple[1])

#The code below will be an error because it doesn't support item assignment
#my_tuple[1] = 4