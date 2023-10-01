# Q-1) Create a class 'Student' with rollno, studentName, course ,dictionary of
# marks(subjectName -
# marks [5]).
# Provide following functionalities
# A. initializer
# B. override __str__ method
# C. accept student data
# D. Print student data
# E. accept records of 5 students and Print it


class Student:

    def __init__(self):
        self.rollno = 0
        self.studentName = 0
        self.course = 0
        self.marks = 0

    def __str__(self):
        return f"{self.marks}, {self.rollno}, {self.studentName}, {self.course}"

    def accept(self, rollno, studentName, course, m1,m2,m3,m4,m5):
        self.rollno = rollno
        self.studentName = studentName
        self.course = course
        self.marks = {'maths': m1, 'eng': m2, 'sci': m3, 'phy': m4, 'bio': m5}

    def print_data(self):
        print(f"{self.rollno},\n{self.studentName},\n{self.course},\n{self.marks}")

s = Student()
print(s)
s.accept(101, "rahul", "dbda", 99,89,70,85,92)
s.print_data()
s.accept(101, "rohan", "dbda", 99,89,77,85,88)
s.print_data()
s.accept(101, "roman", "dbda", 99,89,80,80,92)
s.print_data()
s.accept(101, "rohit", "dbda", 95,89,67,85,91)
s.print_data()
s.accept(101, "ronak", "dbda", 91,89,75,85,92)
s.print_data()








