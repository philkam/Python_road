#Iterators
#From the for-loop lesson, we said that we iterate over iterables, which are python objects that return one or more
#of its elements per iteration.
#Iterators are the python object that contain the data stream, and we can traverse through their elements.
#We can construct an iterator from an iterables using iter keyword.
#IT can be any kind of built-in iterables in python like lists, tuples etc.
#We can iterate over the iterator element by element using next keyword.
#used mostly for big data sets

#usage
my_list = [1,2,3,4,6]
iterator = iter(my_list) #converted iterable to iterator
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator)) #Error:StopIteration error,there are no elements in the list.