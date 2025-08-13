import pandas as pd
import numpy as np

temp = pd.Series([-0.1, 0.0, -0.1, -0.2, 1.8, 2.0, 1.6, 1.6, 2.5, 18.5, 14.5, 7.6])

temp.index = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']

len(temp)


temp.iloc[2]


print(temp.iloc[5:8])

print(temp.loc['apr':'sep'])
print(temp.iloc[:4])
print(temp.iloc[9:])
print(temp[:])

print()

print(temp.loc[temp >= 15])
print(temp.loc[(temp >= 15) & (temp < 20)])
print(temp.loc[(temp < 5) | (temp >= 20)])

print()
march = temp.loc['mar']
print(march)

print(temp.where(temp >=10).dropna())

print(temp.loc[temp >= 10].index)

print(temp + 1)

print(2 * temp + 0.1)

print(temp + temp)

print(temp.loc[temp >= 15] + 1)

print("Mean: ",temp.mean())

print("Sum: ", temp.sum())
print("Median: ",temp.median())
print("Max: ", temp.max())
print("Min: ", temp.min())
print("Standard Deviation: ", temp.std())
print("Standard Variation: ", temp.var())
print("\nAbsolute Value:\n", temp.abs())
print("\nSummary:\n", temp.describe())



