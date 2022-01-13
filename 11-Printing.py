#Print Function
#The syntax of the print function is
#       print(object(s), sep, end, file, flush)

#Format Function
#Makes printing variables much easier and readable. It is a string function.
#Syntax : string.format(value1, value2...)
#Variables must be in curly brackets.

#Usage
print("I am a male")
x = 8
print(f"The current value of X is {x}") #f is placed to make the x variable print in case it is dynamic
print("The current value of x is ",x) #another way of printing dynamically

string_intro = "{first_name} Ansah is teaching programming"
print(string_intro.format(first_name="any name"))
print("The value of x is {}". format(x))