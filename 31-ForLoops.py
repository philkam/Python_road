#FOR LOOPS
#For loops runs for specific pre-defined number of iterations.
#We iterate over iterables, which are python objects that return one or more of its elements per iterations.
#iterables include Files, Dictionaries, Lists, Sets, Tuples, Strings.
#Range function can set the start, end and step for the range function.

#Usage
my_list = [1, 2, 3, "King", 4.8]

for element in my_list:
    print(element)
print("DOne")
print("*************************************")
for element in range(1, 10, 2):
    print(element)
print("Done")