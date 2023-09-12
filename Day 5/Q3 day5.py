list1 = [10, 20, 30, (40, 50), 60]

count = 0
for l1 in list1:
    if type(l1) is tuple:
        print(count)
        break
    count=count+1

