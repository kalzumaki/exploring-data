import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('../data/wilcoxon_test.csv')

# data exploration

mean = df.mean()
print("Mean:", mean ,"\n")
(df['post']- df['pre']).mean()
fig, axes = plt.subplots(nrows = 1, ncols= 2)
df['pre'].plot.box(grid=False, ax=axes[0])
plt.ylim([60, 100])
df['post'].plot.box(grid=False, ax=axes[1])
plt.show()

# wilcoxon signed rank test

w = stats.wilcoxon (df['pre'], df['post'])
print("Wilcoxon Result:", "\n", w)

