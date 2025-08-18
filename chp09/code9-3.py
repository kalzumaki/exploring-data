import folium
import os
os.chdir('/home/kalzumaki/bigdata/chp09')
import displayMap as dm

loc = [9.31181237379359, 123.30731152220616]
loc

map = folium.Map(location=loc, zoom_start=13)
folium.Marker(location=loc, icon=folium.Icon(color='red', icon='star')).add_to(map)

dm.showMap(map)