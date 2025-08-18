import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import association_rules, apriori
from mlxtend.preprocessing import TransactionEncoder

# data prep

df = pd.read_csv('../data/chipotle.csv')

df.info()
df.head()


#data exploration
len(df['Item'].unique())
temp = df[ df.item_price == df.item_price.max()]

temp
temp = df[ df.item_price == df.item_price.min()]
temp = temp[['Item','item_price']].drop_duplicates()

temp

len(df['Transaction'].unique())

# best selling food

sales_quantity = df.groupby('Item').count()
sales_quantity = sales_quantity.sort_values('Transaction', ascending = False)
sales_quantity['Transaction']


#top 10 best selling products

top_ten = sales_quantity.sort_values('Transaction').tail(10)
top_ten = top_ten['Transaction']
top_ten.plot.barh(xlabel = 'Transaction',
                  ylabel = '',
                  title= 'Top 10 Items',
                  figsize = (9,5))
plt.subplots_adjust(left=0.2)
plt.show()

# association analysis


#preprocessing

temp = df[['Transaction', 'Item']].drop_duplicates()
temp = temp.groupby('Transaction')['Item'].apply(list)
temp

te = TransactionEncoder()
trans_matrix = te.fit(temp).transform(temp)
trans_matrix

basket = pd.DataFrame(trans_matrix, columns = te.columns_)

basket.head()

#association rule exploration

freq_item = apriori (df=basket, min_support= 0.01, use_colnames=True)
freq_item

# find association rules using the association_rules() method
rules = association_rules (df= freq_item, metric = 'lift', min_threshold = 1, num_itemsets = len(basket))

rules.sort_values ('confidence', ascending=False , inplace = True)

# display 10
rules.head(10)
rules.iloc[0,:].transpose()
