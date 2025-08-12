import pandas as pd

age = pd.Series([25, 30, 35, 40, 45])
age.index = ['Benjie', 'Kevin', 'Van Kirk', 'Rex', 'Christan']

age.iloc[2]
age.loc['Van Kirk']

print(age
      )

score = pd.DataFrame([
    [77,88,99,55],
    [0,1,2,3],
    [55,66,33,23]
    ])

score.index = ['Math', 'Science', 'English']
score.columns = ['Q1', 'Q2', 'Q3', 'Q4']

print(score)

tom = score.loc['Science','Q2']

print(tom)