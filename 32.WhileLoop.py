#While Loops
#While loops runs until a condition is no longer satisfied.
#Stop condition needs to be met at some point, otherwise there will be an infinite loop.
#We prefer while loops over for loops when we don't know how many iterations we have.


#Usage
"""
for i in range(10):
    print(i)
"""

i = 0
while i < 10:
    print(i)
    i+=1
print("*************************************")
#we want to add till we get to 70
my_list = [ 10, 20, 30, 5, 5, 20, 40]
result_addition = 0
index = 0
while result_addition < 70:
    result_addition = result_addition + my_list[index]
    index +=1
    print(result_addition)
print("Iterations needed to 70:" , index) #the number of iterations it took to get to 70
