#String manipulation
#We can add 2 string together.
#We can mulitply a string by an integer. The output is the string repeated.
#We can check if a string is within another string, using in operator.
""""Python has Built in functions. Check documentation for more. For example:
chr() -> from int to character
len() -> calculates the length of a string
str() -> converts to string
ord() -> converts to integer"""

#usage.
first = 'Ken'
second = 'Martin'

#Concatenation
res_string = first + second
print(res_string)

#multiply string with integer
res_string = first * 5
print(res_string)

#check if string is contained in another string
third = "What to do with your day?"
res_string = "What" in third
print(res_string)

#chr(i) function
#Return the string representing a character whose Unicode code point is the integer i.
print(chr(38))