
Checking_Leap_year=int(input("Please enter year:"))

year=Checking_Leap_year


if year%4==0:
    if year%100==0:
      if year%400==0:
       print("It is a leap year")
      else:
        print("It is not a leap year")
    else:
        print("It is a leap year")
else:
    print("It is not a leap year")



