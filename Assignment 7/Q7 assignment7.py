# 7)Write a Python function student_data () which will print the id of a student
# (student_id). If the user
# passes an argument student_name or student_class(use **kwargs) the function
# will print the
# student name and class.

def student_data(student_id, **kwargs):

    print("Student Id:", student_id)

    if 'student_name' in kwargs:
        print("Student name:", kwargs['student_name'])

    if 'student_class' in kwargs:
        print("Student Class:", kwargs['student_class'])


student_data(101)
student_data(100, student_name= "Rahul", student_class= "A")
student_data(105, student_name= "shubham")