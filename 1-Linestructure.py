# In python, lines can be seen described as seen logically and physically

#Physically and logically the code below is three lines
x =1
y = 1
z = 1

#This below is the same as the one above but physically seen as a line
x =1 ; y= 1; z = 1


#Consider the example below
a = 1 + 2
# is the same as
b = 1 \
    + 2
# We use the \ to add two physical lines into one single line. We usually do that when a line is to \
# scroll left.

#the output gives the same value which is 3
print(a)
print(b)