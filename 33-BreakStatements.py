#Break Statement
"""
-We use break statement to break from a for/while loop if some condition happens.

"""
#USAGE
my_list = [1, 2, 3, "stop", 5, "stop", 4.5]

for i in my_list:
    print(i)
    if i == "stop":
        print("The code will stop!")
        break
print("this is outside the loop")
print("********************************")

index = 0
while index < len(my_list):
    current_element = my_list[index]
    print(current_element)
    if current_element == "stop":
        print("The loop will stop")
        break
    index +=1
