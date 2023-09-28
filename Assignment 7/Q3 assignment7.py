# 3)Write a Pandas program to convert a dictionary to a Pandas series.
# Sample dictionary: d1 = {'a': 100, 'b': 200, 'c':300, 'd':400, 'e':800}
#

import pandas as pd

d1 = {
    'a': 100,
    'b': 200,
    'c': 300,
    'd': 400,
    'e': 800
}

def method1():

    a5 = pd.Series(d1)
    print(a5)



method1()
