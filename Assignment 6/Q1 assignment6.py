# 1)Write a menu Driven Program To Calculate the Parameter and Area of
# different Shapes(Circle,Square,Rectangle) using functions


def function1():

    def circle(r):
        parameter = 2 * 3.14 * r
        area = 3.14 * r ** 2
        print(f"Area of circle: {area}, parameter: {parameter}")

    def square(s):
        area = s ** 2
        parameter = 4 * s
        print(f"Area of square: {area}, parameter: {parameter}")

    def rectangle(l,b):
        area = l * b
        parameter = 2 * (l + b)
        print(f"Area of rectangle: {area}, parameter: {parameter}")

    while True:

      print("-" * 80)

      print("select: 1 of circle, 2 for square, 3 for rectangle, 4 for EXIT")

      choice = int(input("please enter a number:"))

      if choice == 1:
        rad = int(input("please enter a radius:"))
        circle(rad)

      elif choice == 2:
        sid = int(input("please enter a side:"))
        square(sid)

      elif choice == 3:
        len = int(input("please enter a length:"))
        bre = int(input("please enter a breath:"))
        rectangle(len,bre)

      elif choice == 4:
          print("terminate")
          break

      else:
        print("Invalid entry")

function1()