#Conditional Statements with Advanced Data Types
#Lists and membership operators can be used in conditional statements.

#Usage
my_list = ["2", 3, 5, 4.3]
if 3 in my_list:
    print(my_list)

z = 10
x = 2
y = 5

if x > y and z > y: ##False and true ---> False
    print("hello")
elif x > y or z > y: ##False OR true ---> True
    print("Hi")