from scipy import stats

men = [10,10]
women = [15,65]

# chi-square

stats.chi2_contingency([men, women])