string_1 = input("Enter the string : ")
string_2 = ""
for index in string_1:
    if index.isalnum() == True:
        string_2 = string_2 + index

string_2 = string_2.lower()

i = -1
flag = True

for index in range(len(string_2)//2):
    if string_2[index] == string_2[i]:
        i = i - 1
    else:
        flag = False
        break
if flag == True:
    print("string is palindrome")
else:
    print("Sting is not palindrome")