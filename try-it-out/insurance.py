import pandas as pd

sales = pd.Series([781, 650, 705, 406, 580,450, 550, 640], 
                  index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])

print("Print the series: ")
print(sales)
print()
print("Print the Length:")
print(len(sales))

print("Second team:")
print(sales.iloc[1])

print("Team F:")
print(sales.iloc[5])

print("3rd to 5th team:")
print(sales.iloc[2:5])

print("Teams A, B, D:")
print(sales[['A', 'B', 'D']])

print("Sales Team who has sales < 500 or > 700:")
print(sales[(sales < 500) | (sales > 700)])

print("Print the names and sales of the teams with more sales than Team B:")
print(sales[sales > sales['B']])

print("Print the names of teams whose sales < 600")
print(sales[sales < 600])

print("Sum, mean, standard deviation of sales for the eight teams:")
print("Sum: ", sales.sum(), "\n",
      "Mean: ", sales.mean(), "\n",
      "Standard Deviation: ", sales.std()
      )

print("12.")
newTeamsSales = sales.loc[['A', 'C']] = 820
newTeamsSales = sales
print(newTeamsSales)

print("Add new Team J:")
sales.loc['J'] = 400
print(sales)

print("delete team J:")
sales_mod = sales.drop('J')

print(sales_mod)
print()
print("15.")
sales1= sales.copy()
sales2 = sales + 500
print(sales)
print(sales2)