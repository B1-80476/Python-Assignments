# 7) Write a function filter_long_words() that takes a list of words and
# an integer len and returns the list of words that are longer than len.

def filter_long_words():
    no_of_input=int(input("please enter Number of input:"))

    list1= []
    list2= []
    for num in range(no_of_input):
        c = input("please enter item:")
        list1.append(c)

    len1 = int(input("please enter a input length to check string length:"))

    for element in list1:
        if len(element) > len1:
            list2.append(element)

    print(list2)

filter_long_words()