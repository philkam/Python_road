#Bitwise Operators
#Bit level is 0s and 1s. Everything in the computer is zeros and ones.
"""
Bitwise and - &
Bitwise or - |
Bitwise negate - ~
Bitwise XOR - ^
Shift right - >>
Shift left <<
"""

#Usage
x = 3
print(bin(x)) #bin converts to binary

y = 4
print(bin(y))

#Bitwise OR
z = y | x
print(z)

""""
x:  011
y: 0100
------- Using bitwise OR.  z becomess
z: 0111
"""
print(bin(z))