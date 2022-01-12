#String Slice
#When you want more than one index in a string you can slice it.
#We use : to specify the slice start and end
#The end index is not included. It is zero index.

#String Slide
#It means step.
#If we want to change it, we use another :
#It would be [start:end:stride/step]. End is always -1

#Useful functions
#String.count("a") - counts the occurrences in a string.
#String.find("a") - return the index of the first occurrence.

#Usage
first_string = "Hello my name is Phil"
print(first_string)
print(first_string[0:5]) #[start:end]
print(first_string[0:5:2]) #[start:end:step] -jumps 2 steps
print(first_string[-4:-1]) #starts from the bottom stops at -1 which is the last character
print(first_string.count('l')) #counts the number of l in the string
print(first_string.find('l')) #returns the first occurrence of l

