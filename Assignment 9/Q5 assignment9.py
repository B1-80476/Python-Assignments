# Q5. Write a function in python to count the number of lines from a text file
# "story.txt" which is not starting with an alphabet "C".
# Example: If the file "test.txt" contains the following lines:
# Connecting DB’s with Python.
# Working with DB’s using Python.
# Accessing and Manipulating DB’s.
# Creation of Python virtual Environment.
# Working with beautiful soup.
# Working with matplotlib, seaborn.
# The function should display the output as 4

def new():
    c = ("Connecting DB’s with Python."
         "\nWorking with DB’s using Python."
         "\nAccessing and Manipulating DB’s."
         "\nCreation of Python virtual Environment."
         "\nWorking with beautiful soup."
         "\nWorking with matplotlib, seaborn.")

    f = open("story.txt", 'w')
    f.write(c)
    f = open("story.txt", 'r')

    count = 0
    for line in f:

         if line[0] == 'C' or line[0] == 'c':
            continue
         else:
            count += 1

    print(count)

    f.close()

new()