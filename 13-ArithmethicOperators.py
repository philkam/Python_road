#Arithmetic Operators
#They are addition(+) , subtraction(-) , multiplication(*) , Division(/), modulus (%), floor division (//) , exponent(**)

#Usage
a = 3
b = 5
result_add = a + b
print("The result for the addition is ", result_add)

result_sub = b - a
print("The result for the subtraction is ", result_sub)

result_mult = a * b
print("The result for the multiplication is ", result_mult)

result_div = 5/3
print("The result for the division is ", result_div)


result_mod = 5%3
print("The result for the modulus is ", result_mod)

#The modulus can be used to check for even and odd numbers.
if a % b == 0:
    print("The number is even")
else:
    print("The result is odd")

result_fdiv = 5//3
print("The result for the floor division is ", result_fdiv)

result_exponent = 5**3
print("The result for the exponent of is ", result_exponent)
