def find_longest_word():

   list1= []

   no_of_input=int(input("please enter total numbers you want to enter:"))

   if no_of_input == 0:
       print("invalid entry")

   elif no_of_input>=1:
       print(f"Enter {no_of_input}:")

       for l1 in range(no_of_input):
           a = input(f"Enter word {l1+1} :")
           list1.append(a)

   print(list1)

   max = list1[0]

   for l1 in range(len(list1)):
       if len(max) < len(list1[l1]):
           max = list1[l1]

   print(f"maximum length= {max}")


find_longest_word()