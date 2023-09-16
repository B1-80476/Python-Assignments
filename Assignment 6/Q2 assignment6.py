# 2)Display following menu and write required function for it
# A. Display characters from even position
# B. Display characters from odd position
# C. Display length of a string
# D. Add a at the end of string length times


def function():

    def odd_position(list1):
        for word in range(0, len(list1), 2):
            print(f"odd place= {list1[word]}")

    def even_position(list1):
        for word in range(1, len(list1), 2):
            print(f"even place= {list1[word]}")

    def length_of_string(list1):
        length = len(list1)
        print(f" length of string = {length}")

    def a_n_times(list1,str1):
        length = len(list1)
        Add = "a" * length
        str1 = str1 + Add
        print(str1)

    while True:

     print("*" * 80)

     input1= int(input("Please select your choice 1. for odd position, 2. for even position,3. for length of string, 4. for print a with string, 5. for quit:"))

     if input1 == 1:
        str1 = input("please enter a string:")
        list1 = list(str1)

        odd_position(list1)

     elif input1 == 2:
         str1 = input("please enter a string:")
         list1 = list(str1)

         even_position(list1)

     elif input1 == 3:
         str1 = input("please enter a string:")
         list1 = list(str1)

         length_of_string(list1)

     elif input1 == 4:
         str1 = input("please enter a string:")
         list1 = list(str1)

         a_n_times(list1,str1)

     elif input1 == 5:
         print("QUIT")
         break

     else:
         print("invalid entry:")

function()