# 8) Find number of occurrences of each character in the string (irrespective of its case).

str1 = "rahul  acfjwjffpwnfjwfoyqweubfwkhgfphbwh fhoqwyufhwfbkwhgfwhfn qwkfgwufbjqwfykqwovbfhw fkqwfgwqgbf g"
new = str1.upper()
list1 = list(new)
dict = {}

for index in list1:
    if index not in dict:
        dict[index] = 1
    else:
        dict[index] += 1

print(dict)



