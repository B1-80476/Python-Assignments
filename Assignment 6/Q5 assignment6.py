# 5)Calculate the sum and average of the digits present in a string
# Str1="Python83737@#8496"

def function5():
    Str1 = "Python83737@#8496"
    str2 = list(Str1)
    avg = 0
    str3 = []
    for index in str2:
        if index.isdigit() is True:
            str3.append(index)
    print(str3)

    count = 0
    for index_2 in str3:
        count = count + int(index_2)

    num = len(str3)
    print(num)

    print(f"Avg is:{count//num}")


function5()



