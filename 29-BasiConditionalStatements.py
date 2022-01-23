#IF, ELSE IF, ELSE CONDITION
"""
-Python syntax is similar to any language. If we want to execute something provided something else happens, we use  keyword if.
-We use keyword if else statement provided we want another thing to happen if the 'if condition' is not true.
-The 'elif' keyword gives up more options to choose from.
-Only one statement will be executed  which is the first one to be true.
-In usage1, y is printed even though the elif condition is also true.
"""
#Usage
x = 10
y = 20
z = 30
if y > x: #condition is if y is greater than x. The colon is important for python to know where the condition ended
    print(y) #indentation is expected.  #true
elif z > y:
    print(z) # true
else:
    print(x)
print("This is printed either way")

print("*********************************************")

#usage2
if y >x:
    print("This is the first block")
    if z > y:
        print(z)
    elif x >y:
        print(x)
        print("this is the first block also")
print("this is block zero")
