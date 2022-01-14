#Logical Operators
"""
Negate condition = not. If a is true. The (neagation)not will make a false.
Either condition = or. If a is true and b is false. The result is true
Both condition = and. If a and b are both true. The result is true

The following are false in python - zero numerical value(0, 0.0, 0.0+0) , empty string, empty objects, none keyword
Anything apart from these values are true.

Comparison can only be done to ensure true if they are of the same datatype.

"""

#USage
x = 3
y = 5
z = 10

print("1.", x>2)
print("2.", y<1)

#3. for or if one is true, the result is true
print("3.", x>2 or y <1)

#4. for and if one is false, the result is false
print("4.", x>2 and y <1 and z<1)

#5. x>2 is true but the not preceding will make the result false
print("5.", not x>2)

#6. bool of empty string is false
print("6.", bool(""))

#7. bool of 0 is false
print("7.", bool(0))

#8. bool of 2 is true
print("8.", bool(2))

#9. These will give you false because we cannot compare data with different data type.
#Here, we compare a string and a boolean which is false in every way
print("9." )
print("" == False)
print("" == True, "\n")

#10. However, we can compare float to integer and get true.
print("10." )
print(1 == 1.0)


