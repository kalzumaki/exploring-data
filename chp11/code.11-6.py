from scipy import stats 
groupA = [7,3]
groupB = [2,9]

# expected frequency

exp = stats.chi2_contingency([groupA, groupB])[3]


# fisher

fish = stats.fisher_exact([groupA, groupB])

print("Expected Frequency: " , "\n", exp, "\n",
      "Fisher Exact Result: ", "\n", fish
      )