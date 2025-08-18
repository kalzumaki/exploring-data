import folium
import os
os.chdir('../chp09/')
import displayMap as dm

loc = [9.31181237379359, 123.30731152220616]


map = folium.Map(location=loc, zoom_start=16)
dm.showMap(map)