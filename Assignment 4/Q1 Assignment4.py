list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

list3= []

for l1 in range(2):
    for l2 in range(2):
        print(f"{list1[l1] + list2[l2]}")
        list3.append(list1[l1] + list2[l2])

print(list3)



