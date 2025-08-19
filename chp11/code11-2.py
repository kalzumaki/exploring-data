import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('../data/paired_ttest.csv')

df.head()
df[['before', 'after']].mean()
(df['after']-df['before']).mean()

fig, axes = plt.subplots(nrows = 1, ncols=2)

df['before'].plot.box(grid=False, ax=axes[0])
plt.ylim ([60, 100])
df['after'].plot.box(grid=False, ax=axes[1])
plt.show()

# normality test

norm = stats.shapiro(df['after']-df['before'])

print("normality test result: \n", norm, "\n")

# paired t-test

result = stats.ttest_rel(df['before'], df['after'])


print("paired t-test result: \n", result, "\n")