fahrenheit = (celsius * 1.8) + 32

choose=input("Please Enter your temp input in celsius (c) or fahrenheit (f): ")

if choose=="c":
    cel=int(input("Please enter temp in celsius:"))
    fah= cel*1.8+32
    print(f"Your temp in fahrenheit is: {fah}")

elif choose=="f":
    fah = int(input("Please enter temp in fahrenheit:"))
    cel = (fah-32)/1.8
    print(f"Your temp in celsius is: {cel}")

else:
    print("invalid entry")



