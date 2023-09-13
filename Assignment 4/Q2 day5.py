def function_2():

    tuple = 5,4,8,4,5

    user_input=int(input("please enter a input to check if item is repeated in tuple or not:"))

    count = tuple.count(user_input)
    print(f"Your entered input is repeated {count} times")

function_2()