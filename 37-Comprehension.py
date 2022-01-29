#Comprehension
#If you want to build a list faster, we use list comprehension.

#Usage

#Creating list the normal way
my_list_normal = []
for i in range(20):
    my_list_normal.append(i)
print(my_list_normal)


#Creating the same list using the list comprehension
my_list_comprehension = [i for i in range(20)]
print(my_list_comprehension)