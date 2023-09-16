
import numpy as np
import pandas as pd

def function2():

    a2 = pd.Series([1, 3, 5, 7, 9])
    a1 = pd.Series([2, 4, 6, 8, 10])

    print(f"Addition of series = {a1 + a2}")
    print()
    print(f"Subtract of series = {a1 - a2}")
    print()
    print(f"Multiple of series = {a1 * a2}")
    print()
    print(f"Divide of series = {a1 / a2}")


function2()
