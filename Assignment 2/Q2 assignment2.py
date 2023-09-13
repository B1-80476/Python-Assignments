
Sub1=int(input("Please enter marks of three subject:"))
Sub2=int(input())
Sub3=int(input())

Avg=(Sub1+Sub2+Sub3)/3

if Avg<=100 and Avg>=90:
    print("Grade A")
elif Avg <= 89 and Avg >= 80:
        print("Grade B")
elif Avg <= 79 and Avg >= 70:
        print("Grade C")
elif Avg <= 69 and Avg >= 60:
        print("Grade D")
elif Avg <= 59:
        print("Grade F")
else:
    print("invalid entry")

