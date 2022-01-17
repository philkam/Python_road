#Sets
#Special case of a list where the elements can only be unique.
#Sets cannot be indexed, doesn't have order but mutable.
#Sets are created using the curly brackets {}
#For repeated objects it will only print the unique values.
#Elements can be added using the add function and removed using the pop function.

#Usage
my_set= {1, 25.3, 9, "p"}
print(my_set)
print(type(my_set))
#my_set[0] #error:sets  cannot be indexed

new_set = { 1, 2, 1, 3, 1, 3, 2} #only unique sets can be printed.
print(new_set)
new_set.add(6)
my_set.pop()

print(new_set) #6 has been added to the set
print(my_set) #"p" has been popped