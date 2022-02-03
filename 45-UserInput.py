#User Input
#Many applications work by accepting input from the user.
# In many cases, you can't prevent the user from using your application incorrectly.
#So, you need to handle the expected incorrect inputs.
#We can read the keyboard input using input built-in function.
#It will wait until the user inserts the input and submit it by clicking enter
#You can provide a help message for the user.
#The output of the input function is always a string

#usage
x = input() #Enter  a name in the prompt
print(x)

z = input("Please enter a number")
print(type(z)) #This is a string

p = int(input("PLease enter a number"))
print(type(p)) #this will be an int, it has been casted.
