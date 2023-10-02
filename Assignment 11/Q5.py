# Q5 Write a Python program to sort a list of tuples using Lambda.
# Original list of tuples:
# [('Python', 88), ('ML', 90), ('Rprograming', 97), ('DBMS', 82)]
# Sorting the List of Tuples:
# [('DBMS', 82), ('Python', 88), ('ML', 90), ('Rprograming', 97)]

l = [('Python', 88), ('ML', 90), ('Rprograming', 97), ('DBMS', 82)]

for index in l:
    a = sorted(l, key = lambda y:y[1])
print(a)