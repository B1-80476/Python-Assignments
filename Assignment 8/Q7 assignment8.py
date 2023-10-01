# 7) Write a code to check if given string is palindrome or not.


str1 = "so qwertyuiop pOiuytrewq os"


new = str1.upper()
list1 = list(new)

i = -1

for index1 in range(len(list1)//2):
    flag = False
    if list1[index1] == list1[i]:
        i -= 1
        flag = True

if flag:
    print("palindrome")
else:
    print("Not")