#Class Method Decorator
"""
-It is a decorator that can be applied on any method in our class.
-It will allow us to call that method using also the class name and not only the object
"""


class Car:
    cars_count = 0
    def __init__(self, model):
        self.__model = model
        Car.cars_count = Car.cars_count + 1

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model):
        self.__model = model

    @classmethod
    def countcars(car_class):
        print("We have: ", car_class.cars_count, " cars")

car1 = Car("BMW")

car1.countcars()
car1.model = "Kea"
print(car1.model)

car2 = Car("Kea")
car2.countcars()