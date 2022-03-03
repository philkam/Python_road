#MOdifying Attributes
"""
-We can modify any attribute
-However, by doing so, we expose the code for anyone to change
-In other programming language,we can prevent this by setting the attributes as private
-In order to keep the attributes private from the user, we use getters and setters methods.
-The object attributes start with __
-Calling the getters and setters each time you want to get the value or set the value for one attribute is a bi of hassle.
-There is a more pythonic way to hide/encapsulate the attribute from the user. That is the property function.

"""

#Usage
class Car:
    def __init__(self, model, year, price):
        self.__model = model
        self.year = year
        self.price = price

    def setmodel(self, model):
        self.__model = model

    def getmodel(self):
        return self.__model

    model = property(getmodel, setmodel)
    number_of_wheels = 4

car1 = Car('BMW', 2000, 10000)


# print(car1.setmodel("AAA"))
# print(car1.getmodel())

car1.model = "AAA"
print(car1.model)
print(car1.year)