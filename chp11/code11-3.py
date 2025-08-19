import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('../data/mw_test.csv')

# data exploratory

df.head()
count = df.groupby('group').count()
mean = df.groupby('group').mean()
df.groupby('group').boxplot(grid=False)
plt.show()

print("count: ", '\n',count , "\n")
print("mean: ", '\n', mean, "\n")

print()

group1 = df.loc[df.group == 'A', 'score']
group2 = df.loc[df.group == 'B', 'score']


# man whitney black

mwb = stats.mannwhitneyu(group1, group2)

print("Man Whiteny Black Result: \n", mwb)