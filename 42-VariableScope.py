#Variable Scope
"""
Not all variables cn be accessed all the time.
There is a scope for each variable, either local or global.
Global variables can be accessed and modified from anywhere in the code.
"""

#Local Variables
#If a variable is defined inside a function, then it cannot be called outside the function


#Global Variable
#We can force a variable inside a function to be global using global keyword.

#Usage
def multiply(x, y):
    global result
    result = x*y
    print(result) #Local variable
    return result
print(multiply(4,2))

print(result) #this can be printed because result has been made global

