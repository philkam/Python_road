#Create your first Class in python
"""
Self Keyword
-When you initialize two or more objects of the same class, python needs a way to differentiate between them.
-Self is the way to do so.
-It is a pointer to the memory address where each object of the class is stored.

Class Keyword
-We define a class using class keyword.
-It is a convention to use CapitalName for the class.

Init Method
-It stores the initial values for all the instance attributes
-It must be created like this __init__()
-The first argument must be self
-The attributes are accessed using the dot.

Class Vs Instance Attributes
-The attributes inside the init method are specific for the instance. Called instance attributes
-Attributes that are shared between all instances are called class attributes and defined outside the init method

Function Vrs Method
-Uses the keyword def
-Has input and output.
-Functions are created outside a class whilst methods are created inside the class
-
"""


#usage
class Car:
    def __init__(self, model,year, price):
        self.model = model
        self.year = year
        self.price = price
    number_of_wheels = 4 #shared attribute/class attribute