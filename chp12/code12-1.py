import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

# data prep
df = pd.read_csv('../data/iris.csv')
df = df.drop('Species', axis=1)

df.head()


# data standardization

scaler = StandardScaler()
result = scaler.fit_transform(df)
df_scaled = pd.DataFrame(result, columns= df.columns)
df_scaled.head()

# dimension
pca = PCA(n_components=2)
transform = pca.fit_transform(df_scaled)
transform = pd.DataFrame(transform)
transform.head()


# visualization

transform.plot.scatter(x=0, y=1, title='PCA plot')
plt.show()