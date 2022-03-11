#Property Decorator
"""
-We have many built-in decorators we can use for python classes, which can make our life much easier.

-@property: We can get the same results of property function using the property decorator.
For the getters and setters, we can have two methods with the same name if you notice they have different number
 of parameters.

-@classmethod
-@staticmethod
"""

class Car:
    def __init__(self, model):
        self.__model = model

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

car1 = Car("BMW")
print(car1.model)

car1.model = "Kea"
print(car1.model)