def factorial():


    for index in range(1,11):
        fact = 1
        for index1 in range(1,index+1):

            fact = fact * index1

        print(f"factorial of {index1} = {fact}")

factorial()