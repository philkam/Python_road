#Higher Order FUnction
#Higher order function take function as argument.
"""Map function is as follows
            map(func, *iterables)
The asterisk means that there can be more than one iterables.
It applies function on the iterables."""

#Map function
"""
-THe function must have number of inputs equal to the number of iterables.
-Maps returns a generator that can be applied by using the list built-in function.
-The function can be a normal or a lambda one. 
-It is better to use lambda with map as it is a more pythonic way to write the code."""

#Usage
def add_five(my_list):
    output_list = []
    for element in my_list:
        element = element + 5
        output_list.append(element)
    return output_list

my_list = [5,1,20]
print(add_five(my_list))

def add_five_map(element):
    return element +5
output = map(add_five, my_list)

output = map(lambda element: element +5 , my_list)
print(list(output))
