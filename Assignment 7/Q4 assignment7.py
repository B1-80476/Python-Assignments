# 4)Write a Pandas program to change the order of index of a given series. Go to
# the editor
# Sample Output:
# Original Data Series:
# A 1
# B 2
# C 3
# D 4
# E 5
# dtype: int64
# Data Series after changing the order of index:
# B 2
# A 1
# C 3
# D 4
# E 5
# dtype: int64

import pandas as pd

list1 = ["A", "B", "C", "D", "E"]
list2 = [1, 2, 3, 4, 5]

series1 = pd.Series(list2, index=list1)
print(series1)

new_order = ['B','A','C','D','E']
series2 = series1.reindex(new_order)
print(series2)


