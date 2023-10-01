# Q4.Write a program that display following output:
# SHIFT
# HIFTS
# IFTSH
# FTSHI
# TSHIF
# SHIFT

def rotate():

    s = "SHIFT"
    print(s)
    for index in range(len(s)):
        s = s[1] + s[2:] + s[0]
        print(s)

rotate()



