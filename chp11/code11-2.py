import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

df = pd.read_csv('../data/paired_ttest.csv')

df.head()
df[['before', 'after']].mean()
(df['after']-df['before']).mean()