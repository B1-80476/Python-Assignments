# Q1. Refer the dataset "Advertising.csv" and perform following tasks.
# i) Read the dataset "Advertising.csv" in data frame
# ii) Print first five records of dataset
# iii) print last five records from dataset
# iv) display the columns inside the dataset
# v) display last three records from dataset
# vi) display the information about the dataset and analyse the data
# vii) display types of each columns.
# viii) check for null values in the dataset and display the sum of null values inside the column
# ix) drop a column 'radio' from a dataset and display first ten records
# x) increase the sales by 10% and add a new column "updated_sales" in dataframe
# xi) display shape of data
# xiii) describe the dataset.


import pandas as pd

df = pd.read_csv("Advertising.csv")
de = pd.DataFrame(df)
print(f"first five records:\n {de.iloc[:5]}")
print("-"*80)
print(f"last five records:\n {de.iloc[-6:-1]}")
print("-"*80)
print(f"the columns:\n {de.columns}")
print("-"*80)
print(f"last three records:\n {de.iloc[-4:-1]}")
print("-"*80)
print(f"Information about the dataset:\n {de.info}")
print("-"*80)
print("null values in the dataset:")
print(df.isna())
print("display the sum of null values inside the column")
print(df.isna().sum())
print("-"*80)
df.drop('radio',axis=1, inplace=True)
print(df.head(10))
print("-"*80)
df['update_sales'] = df['sales'] + (0.10*df['sales'])
print(df)
print("-"*80)
print("display shape of data:")
print(df.shape)
print("-"*80)
print("describe the dataset:")
print(df.describe)