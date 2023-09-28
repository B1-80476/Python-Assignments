# Q1. Write a Python program to create a Vehicle class with max_speed and
# mileage instance attributes. Write a python program to Create a child class Bus
# that will inherit all of the variables and methods of the Vehicle class

class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_specs(self):
        print(f"MAX SPEED = {self.max_speed}")
        print(f"MILEAGE = {self.mileage}")


class Bus(Vehicle):


    def print_specs(self):
        Vehicle.print_specs(self)



p1 = Bus(55, 10)
p1.print_specs()
