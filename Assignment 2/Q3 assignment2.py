
def factorial_of_num(num):
    fact=1
    while num>=1:
        fact=num*fact
        num=num-1
    print(f"Factorial of number is:{fact}")

factorial_of_num(5)



