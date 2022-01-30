#Defining Functions
#Function header
"""
Python uses the keyword def to define the function.
Functions can have multiple inputs and/or outputs.
Eg def multiply(x,y):
You can have optional input by assigning the value of the variable in the function header.
Eg def multiply(x, y, z =1):
The code will throw an error if you don't provide x or y, but not z
"""

#Function Body
"""
The function body is indented in a code block, like loops and conditional statements.
We can return one or more outputs using return.
Eg.
def multiply(x,y):
    result= x*y
    return results
"""

#Function Naming
"""
Can't use spaces or special characters.
Can't use python keywords or built-in functions' names.
Use descriptive names for function name, inputs, and outputs. 
"""

#Function Argument and Parameter
""""
The terms parameter and argument can be used for the same thing: information that are passed into a function. 
From a function's perspective: A parameter is the variable listed inside the parentheses in the function definition. 
An argument is the value that are sent to the function when it is called.
"""

#Usage
def multiply(first_num, second_num): #This is the function header
    result = first_num * second_num #Function body
    return result                   #Function body

#Calling the function - THe function is being called and used.
res = multiply(8,6)
print(res)

#You can override the assigned value of a function parameter.
def addition(first_num, second_num=4): #This is the function header
    result = first_num + second_num #Function body
    return result                   #Function body

#Even though second number has been assigned a value, the 6 will override it.
add_ans = addition(8,6)
print(add_ans)