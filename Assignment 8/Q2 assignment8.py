# 2)Define a Circle class allowing to create a circleC (O, r) with center O(a, b) and radius r
# using the
# constructor:
# def init (self,a,b,r):
# self.a = a
# self.b = b
# self.r = r
# A:- Define a Area() method of the class which calculates the area of the circle.
# B:-Define a Perimeter() method of the class which allows you to calculate the perimeter of
# the circle.

PI = 3.14

class Circle():

    def __init__(self,r):
        self.r = r


    def cal_Area(self):
        self.Area = PI * self.r ** 2
        print(f"Area of circle is = {self.Area}")

    def cal_perimeter(self):
        self.perimeter = 2 * PI * self.r
        print(f"Perimeter of circle is = {self.perimeter}")


radius = Circle(10)
radius.cal_Area()
radius.cal_perimeter()


