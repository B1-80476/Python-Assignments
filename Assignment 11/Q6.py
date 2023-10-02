# Q6. Consider engine.csv file and plot the following graphs between any 2 columns.
# i) Line plot
# ii) Bar Graph
# iii) Scatter Plot

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Engine.csv.csv")
print(df)

def bar_plot():

    engine = np.array(df["ENGINESIZE"])
    co2 = np.array(df["CO2EMISSIONS"])

    plt.bar(engine,co2)



    plt.xlabel("CO2 emiss")
    plt.ylabel("Size engine")

    plt.title("E size vs Co2 E")

    plt.show()

def scatter_plot():
    cyl = np.array(df["CYLINDERS"])
    fuel = np.array(df["FUELCONSUMPTION_COMB"])

    plt.scatter(cyl, fuel, color= "green")


    plt.xlabel("CYLINDERS")
    plt.ylabel("FUELCONSUMPTION_COMB")

    plt.title("CYLINDERS vs FUELCONSUMPTION_COMB")

    plt.show()

def line_plot():
    eng = np.array(df["ENGINESIZE"])
    cy = np.array(df["CYLINDERS"])

    plt.plot(eng ,cy, color= "Black")


    plt.xlabel(eng)
    plt.ylabel(cy)

    plt.title("ENGINESIZE vs CO2EMISSIONS")

    plt.show()

bar_plot()
scatter_plot()
line_plot()