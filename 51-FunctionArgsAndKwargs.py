#Function Args and Kwargs
#Args
#Sometimes, we don't know beforehand how many inputes a function should take.
#We wouldn't need to define a list. This is done by using the args as an argument.
#The asterisk is called the unpacking operator.
#The inputs in this case are passed as positional arguments - tuple - and not list.

#Kwargs
#if you have keywords or named arguments, then you can use kwargs, which is short for keyword arguments.
#We define it by using double asterisk, which is also an unpacking operator.
#Notice that pass the inputs as a dictionary.

#Function input ordering
"""def func_example(x, y, z = 3, *args, **kwargs)
-Standard inputs can be required like x and y in this case,
-Standard inputs can be Optional like z
 -Positional inputs is *args
 -Keyword input is **kwargs"""

#usage
def print_input(*args): #it can take as many inputs, inputs are tuple data types
    for i in args:
        print(i)
print_input(1,5,1)

def print_input2(**kwargs):
    for key, value in zip(kwargs.keys(), kwargs.values()):
        print(key, value)
print_input2(x = "Phil", y = "M")

def print_input3(*z, y, x =1):
    print(x)
    print(y)
    print(z)

print_input3(1,2,3,4, y =1, x =5)
#the *z prints 1,2,3,4. notice the order that y comes first(standard required input)
#before x which is a standard required input then *z which is the positional input.