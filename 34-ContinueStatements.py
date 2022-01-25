#Continue Statements
#We use the continue statements if we want to skip some iterations from a for/while loop if some condition happens.

#Usage
my_list = [1, 3.4, 'stop', 5, 'stop', 2]
for i in my_list:
    if i == 'stop':
        #break
        continue   #the 'stop'  will be skipped
    print(i)
