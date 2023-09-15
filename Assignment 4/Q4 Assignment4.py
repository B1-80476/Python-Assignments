def function4():

    mylist = [41,"DROND","Sunbeam", 13,"ZARA"]

    list1 = []

    for l1 in mylist:
       if type(l1) is str:
          list1.append("#")
          continue

       elif type(l1) is int:
          for l2 in range(0,3):
            list1.append(l1)

    print(list1)

function4()