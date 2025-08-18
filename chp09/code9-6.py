import folium
import os
import displayMap as dm
import pandas as pd


df = pd.read_csv('../data/wind.csv')

df = df.sample(50, random_state=123)