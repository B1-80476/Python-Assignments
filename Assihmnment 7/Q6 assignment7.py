def function6():

    string = " The quick brown fox umps over the lazy dog"
    string1= string.lower()
    list1 = list(string1)
    sp=['!','?'," "]
    dict1 = {}
    for ch in list1:
        if ch not in sp:
            if dict1.get(ch) is None:
                dict1[ch]=1
        else:
            pass

    length = len(dict1)

    if length == 26:
        print("pangram")

    else:
        print("Not pangram")


function6()
