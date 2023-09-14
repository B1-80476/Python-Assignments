
def translate():

    dict1 = "this is fun"
    str = ""
    list1 = list(dict1)
    list2 = ['a','e','i','o','u',' ']


    for word in list1:

          if word not in list2:
              str = str+word+'o'+word
          else:
              str=str+word
    print(str)

translate()




