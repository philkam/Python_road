#Integers and Float
"""We don't need to declare the type of variable. Python infer the data type. For example
when we type y = 4, pythong will create a variable called x which will have int as its datatype.
when we type x = 4.0, python will create a variable called x which will have float as its datatype.
The type() function tells which datatype it is.

Scientific notation can be used for float: x = .3e7 means 0.3 times 10 exponenent 7
Any number larger than 1.8x10^308 will be treated as infinity
Any number less than 5x10^-324  will be treated as a zero"""

#Usage
x = 1
print (x)

#tells you the datatype of x
print(type(x))

y = 3.4
print(type(y))

#Arithmetic operation of an integer and float will give a float datatype
print(type(x + y))