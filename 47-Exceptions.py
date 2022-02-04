#Exceptions
"""
Also known as runtime errors. It happens when there is no syntax errors in the code, but the code failed
in some cases.
Example: if we have a function that divides tow numbers, if the denominator is zero, then the code will fail and stop.
A user can define the message that prints in case there is an exception, the raise Exception() is used in this case.
We can use another keyword -assert- for detecting bugs more clearly in our code.
The raise is used to raise an exception.
THe assert is also used to raise an exception but if a condition is not met.

"""
#Usage

#Exception 1
x = 1
y = 0
#z = x/y
#print("hello")
#>> error division by 0

#Exception 2
#print(a)

#>> a is not defined exception

#Exception 3
#2 + "a"

#>> unsupported operands types for +: 'int' and 'str'


#Exception 4
x = 10
y = 20
# if x < y:       #Exception
#     raise Exception("THis is incorrect")
# print("Hello")


#Exception 5
a = 30
b = 20
# assert a < b
# print("hello")

