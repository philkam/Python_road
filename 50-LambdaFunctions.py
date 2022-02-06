#Lambda Function
"""
-The division function we discussed earlier can be simplified into one line.

        def div(x,y):
           return x/y
        print(div(x,y)

-We can do so by using lambda keyword
        div = lambda x, y: x/y
        print(div(3,2))

Lambda Syntax
--We first use the lambda keyword, followed by the function variables.
--Then we use the colon, followed by the function body.
--Lambda functions are mainly used for small simple functions.
--It can be used as arguments for higher-order functions.
--Higher order functions take functions as arguments. Ex-filter and map functions are higher-order
"""

#Usage
def mul(x,y):
    return  x*y
print(mul(3,4))

#Using lambda
mul_lambda = lambda x, y: x*y
print(mul_lambda(3,4))

#both give 12, therefore they are the same.
