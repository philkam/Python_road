#Static Methods Decorator
"""
-It is a built-in decorator that defines static methods.
-Static methods are class methods, rather than object methods. Just like class methods.
-Class methods work with the class, because one of their parameters is the class itself.
"""

#usage
class Car:
    car_count = 0
    def __init__(self, model):
        self.__model = model
        Car.car_count  +=1

    ##Setting & Getting ( setters and getters)
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    #Access to nothing
    @staticmethod
    def peep():
        print("PEEP!")

    ## Access to only the class
    @classmethod
    def countcars(car_class):
        print("We have: ", car_class.car_count, " Cars")

    ## Normal ( access to both the class and the objects)
    def print_car_model(self):
        print("Your car mode is : ", self.__model)
        print("We have : ", self.car_count, " cars")

car1 = Car("BMW")
print(car1.model)

car1.print_car_model()

car1.peep()
Car.peep()