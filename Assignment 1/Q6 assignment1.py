str_age=input("Please enter your age:")
Age=int(str_age)

if Age<18:
    print("Not eligible for voting")
elif Age>110:
    print("Invalid entry")
else:
    print("eligible for voting")



