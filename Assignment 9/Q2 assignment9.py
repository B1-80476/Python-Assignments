# Q2. Write a Rectangle class in Python language, allowing you to build a
# rectangle with length and width attributes . Create a Perimeter() method to
# calculate the perimeter of the rectangle and a Area() method to calculate the
# area of the rectangle . Create a method display() that display the length, width,
# perimeter and area of an object created using an instantiation on rectangle class.
# Create a Parallelepiped child class inheriting from the Rectangle class and with
# a height attribute and another Volume() method to calculate the volume of the
# Parallelepiped

class Rectangle:

    def __init__(self,length,breath):
        self.length = length
        self.breath = breath

    def perimeter(self):
        return 2 * (self.length + self.breath)

    def area(self):
        return self.length * self.breath

    def display(self):
        print(f"Length is: {self.length}")
        print(f"Breath is: {self.breath}")
        print(f"Perimeter is: {Rectangle.perimeter(self)}")
        print(f"Area is: {Rectangle.area(self)}")

class Parallelepiped(Rectangle):

    def __init__(self,length,breath,height):
        Rectangle.__init__(self,length,breath)
        self.heigth = height

    def volume(self):
        return self.length * self.breath * self.heigth

    def display_volume(self):
        Rectangle.display(self)
        print(f"volume of Parallelepiped:{Parallelepiped.volume(self)}")


p = Parallelepiped(2,3,4)
p.display_volume()