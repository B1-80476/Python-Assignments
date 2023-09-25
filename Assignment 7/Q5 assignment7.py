
def function5():

    string = "sunbeaminfo.com"
    list1 = list(string)
    count = {}

    for ch in list1:
        if count.get(ch) is None:
           count[ch]=1

        else:
            count[ch] += 1

    print(count)

function5()
