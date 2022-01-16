#List slicing and indexing
"""
List Slicing
Zero-based, square brackets to define it, comma to separate the elements, colon to slice.
Lists are mutable and ordered.
"""

#Usage
List_example = [1, 2, 3]
List_example[1]= "Phil" #since list is zero-indexed. we changed the 2 to "Phil"
print(List_example)

string_example= "Python basics"
print(string_example[0]) #string index prints the letters in the string.

#This is an error because the string doesn't support assignment. it is immutable.
#string_example[0] = "Q"
