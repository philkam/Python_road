#Zip Functions
#it maps iterables to iterators.
#It is used to iterate over multiple iterables at the same time.

#Usage
list1 = [1, 3, 2] #iterable
list2 = [5, 1, 4] #iterable
zip_list = zip(list1, list2) #iterator
#print(list(zip_list))

for i1, i2 in zip_list:
    print(i1,i2)