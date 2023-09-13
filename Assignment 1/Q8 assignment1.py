No_of_calls=int(input("please enter number of call:"))

if No_of_calls<=100:
    print("Your telephone monthly bill is 200")
elif No_of_calls>100 and No_of_calls<=150:
    bill= No_of_calls-100
    extra= bill*0.6 + 200
    print(f"Your telephone monthly bill is {extra}")
elif No_of_calls>150 and No_of_calls<=200:
    bill= No_of_calls-150
    extra= bill*0.5 + 230
    print(f"Your telephone monthly bill is {extra}")
else:
    bill = No_of_calls - 200
    extra = bill * 0.4 + 255
    print(f"Your telephone monthly bill is {extra}")
