import pandas as pd

# table
temp_stats = [
        [-0.1, 0.0, -0.1, -0.2],
        [1.8, 2.0, 1.6, 1.6],
        [6.4, 6.8, 5.8, 5.9],
        [12.3, 12.9, 11.5, 11.5],
        [17.9, 18.5, 17.1, 17.1],
        [22.2, 22.8, 21.6, 21.5]
    ]

stats = pd.DataFrame(temp_stats)
stats.index = ['january', 'febuary','march','april','may','june']
stats.columns = ['City1','City2', 'City3', 'City4']

# average temp. in march for city2
averageTemp2 = stats.loc['march', 'City2']

# average temp. in april for city4

averageTemp3 = stats.loc['april', 'City4']

# average temp. in january for city3

averageTemp4 = stats.loc['january', 'City3']

# average temp. in june for city1

averageTemp5 = stats.loc['june', 'City1']



print()
print("Monthly Average Temperature Statistics Table")
print()
print(stats)
print()
print("Average Temperature in March for City2")
print(averageTemp2)
print()
print("Average Temperature in April for City4")
print(averageTemp3)
print()
print("Average Temperature in January for City3")
print(averageTemp4)
print()
print("Average Temperature in June for City1")
print(averageTemp5)
