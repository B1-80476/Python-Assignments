def histogram():

   list1= []

   no_of_input=int(input("please enter total numbers you want to enter:"))

   if no_of_input == 0:
       print("invalid entry")

   elif no_of_input>=1:
       print(f"Enter {no_of_input}:")

       for l1 in range(no_of_input):
           a = int(input(f"Enter {l1+1} value:"))
           list1.append(a)

   print(list1)

   for l2 in range(no_of_input):
       print('*'*list1[l2])

histogram()