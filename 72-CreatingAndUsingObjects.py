# Create and use objects in Python
"""
Accessing the object attributes
We use the dot operator . to access the attributes/methods

"""


# usage

class Car:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = price

    number_of_wheels = 4


first_car = Car('Nissan', 2014, 10000)
second_car = Car('BMW', 2009, 20000)

#print(first_car == second_car)  # they are stored in different memory addresses because of keyword self


print(first_car.price)
print(second_car.number_of_wheels)
