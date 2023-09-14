def function1():
    people={'Arham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
    people_copy = people.copy()

# A. Find out how many students are in the list
# B. Change Lisa’s favourite colour
# C. Remove 'Jenny' and her favourite colour
# D. Sort and print students and their favourite colours alphabetically by name
    def fun_1():

       count = len(people)

       print(f"numbers of students in list is: {count}")

       colour_change = input("please enter a color name to change lisa color: ")

       for key in people:
           if key == "Lisa":
            people["Lisa"] = colour_change

       print(people)

       if key == "Jenny":
           people.pop('Jenny')

       print(people)

    fun_1()


    list2= []
    for key in people_copy:
      list2.append(key)

    list2.sort()
    print(list2)

function1()



