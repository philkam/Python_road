#Enumerate function
#We use it to iterate over one iterable and one counter at the same time.
#it is a zip function but with a counter.

#Usage
my_list = [1, 2, 's', 3.5]
#print(list(enumerate(my_list))) #becomes a zip function

for i, c in enumerate(my_list):
    print(i) #this is the counter
    print(c) #this is the list item

