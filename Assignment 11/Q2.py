# Q2. Refer the dataset "Salaries.csv" and perform following tasks.
# i) Read the dataset in dataframe.
# ii) display first five records.
# iii) display first ten records.
# iv) display last five records.
# v) display last ten records.
# vi) display the columns inside the dataset.
# vii) display shape of data.
# viii) describe the dataset.
# ix) display the information about the dataset and analyse the data.
# x) display types of each columns.

import pandas as pd

df = pd.read_csv("Salaries.csv")
de = pd.DataFrame(df)
print(f"first five records:\n {de.iloc[:5]}")
print("-"*80)
print(f"first 10 records:\n {de.iloc[:10]}")
print("-"*80)
print(f"Last five records:\n {de.iloc[-6:-1]}")
print("-"*80)
print(f"Last 10 records:\n {de.iloc[-11:-1]}")
print("-"*80)
print(f"column:\n {de.columns}")
print("-"*80)
print(f"Shape:\n {de.shape}")
print("-"*80)
print(f"Describe:\n {de.describe}")
print("-"*80)
print(f"information about the dataset and analyse the data:\n {de.info}")
print("-"*80)
print(f"display types of each columns:\n {de.dtypes}")
