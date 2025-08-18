import folium
import os
import displayMap as dm
import pandas as pd


df = pd.read_csv('../data/wind.csv')

df = df.sample(50, random_state=123)

center = (df.lat.mean(), df.lon.mean()) # lat first
map = folium.Map(location=center, zoom_start=5)
dm.showMap(map)

for i in range(len(df)):
    folium.Marker(location=[df.lat.iloc[i], df.lon.iloc[i]], icon=folium.Icon(color='blue',icon='flag')).add_to(map)
    
dm.showMap(map)


map = folium.Map(location=center, zoom_start=5)

for i in range(len(df)):
    folium.CircleMarker(location=[df.lat.iloc[i], df.lon.iloc[i]], 
                  radius=(df.spd.iloc[i]**0.5) * 2, color='red', stroke=False, fill=True, fill_opacity=0.5).add_to(map)
    
dm.showMap(map)

