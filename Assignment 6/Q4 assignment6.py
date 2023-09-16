# 4)- Write a definition of a method count_now(places) to find and display those
# # place names, in
# # which there are more than 5 characters.
# # For example :
# # If the list places contains
# # ["DELHI","LONDON","PARIS","NEW YORK","DUBAI"]
# # The following should get displayed :
# # LONDON
# # NEW YORK

def count_now():

    list1 = ["DELHI","LONDON","PARIS","NEW YORK","DUBAI"]

    for index in list1:

          size =  len(index)
          if size > 5:
            print(index)



count_now()