import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('../data/ind_ttest.csv')

# data exploration

df.head() # check if it reads

df.groupby('group').count() # count all group column
df.groupby('group').mean() # the mean of the group column
df.groupby('group').boxplot(grid =True) # create a boxplot for group column on b
plt.show()


group1 = df.loc[df.group == 'A', 'height']
group2 = df.loc[df.group == 'B', 'height']
group1
group2

#normality test (not required btw since the sample is > 30 (45))

stats.shapiro(group1) 
stats.shapiro(group2)


stats.levene(group1, group2)

result = stats.ttest_ind(group1, group2, equal_var = True)
result


