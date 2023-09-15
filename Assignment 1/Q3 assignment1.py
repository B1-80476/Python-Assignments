# 3] Write a program to accept a 4 digit number and
# a. Display face value of each decimal digit
# b. Display place value of each decimal digit
# c. Display no in reverse order by changing decimal place values If
# user
# enters a 4 digit number 9361 output should be
# a. 9 3 6 1
# b. 9361 = 9 000 + 300 + 60 + 9
# c. 1639

def function():

    print("Please enter 4 digit number")
    print()
    Num_str = input(f"Please enter number:")


    if len(Num_str) == 4:

        Num = int(Num_str)



        digit1 = Num % 10
        Num = Num//10
        digit1_str = str(digit1)
        digit2 = Num % 10
        Num = Num // 10
        digit2_str = str(digit2)
        digit3 = Num % 10
        Num = Num // 10
        digit3_str = str(digit3)
        digit4 = Num % 10
        Num = Num // 10
        digit4_str = str(digit4)

        str1 = digit1_str+digit2_str+digit3_str+digit4_str

        print(f"Face value of each decimal digit: {digit4} {digit3} {digit2} {digit1}")
        print()
        print(f"Place value of each decimal digit: {digit4*1000} {digit3 * 100} {digit2 * 10} {digit1 * 1}")
        print()
        print(f"No. in reverse order by changing decimal place values: {str1}")

    else:
        print("invalid entry")



function()