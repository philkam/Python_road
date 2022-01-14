#Identity Operators
#is and is not
#The equality operator checks the values are the same
#The identity operator checks if the variables(objects) are the same. USe when you want to check if memory addresses
#are the same.

#Usage
x = 1000
y = 1000

print(x == y ) #Equality operator compares values


#Checking the memory address of x and y
print(id(x))
print(id(y))

print(x is y) # Identity operator, compares variables (memory address)
#returns true if memory addresses are the same