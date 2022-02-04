#Handling Exceptions
#Any exception will break the code and any lines after the exception won't be executed.
#HEnce we need to catch and handle the errors.
#We handle exceptions using a block of try and except.
#Inside the try body, we write the code that we want to execute, but we suspect it may throw an error.
#Inside the except body, we write the code that should be executed if an exception occurs.

#usage
def divide(x, y):
    try:
        result = x/y
    except:
        result = "Cannot divide by 0"
    return result

print(divide(5,3))
print(divide(2,3))
print(divide(3,0))
print("Hello")