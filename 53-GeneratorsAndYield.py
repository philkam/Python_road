#Generators And Yield
"""
-We can construct python iterators using functions
-These functions are called generators
-The key difference between regular functions and generators is the yield keyword.
-Yield makes the generators returns values one at a time. yield replaces the return keyword.
-Whenever the generator is called, it starts from where it left.

"""

#usage
def reverse_normal(data):
    reverse_list = []
    for i in range(len(data)-1, -1, -1):
        reverse_list.append(my_list[i])
    return reverse_list

my_list = [1,2,5]
reverse_list_normal = reverse_normal(my_list)

print(reverse_list_normal)

def reverse_generator(data):
    for i in range(len(data)-1, -1, -1):
        yield my_list[i]

reverse_list_generator = reverse_generator(my_list)
# print(next(reverse_list_generator))
# print(next(reverse_list_generator))
# print(next(reverse_list_generator))

for i in reverse_list_generator:
    print(i)

