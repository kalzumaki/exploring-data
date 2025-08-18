import folium
from geopy.geocoders import Nominatim
import displayMap as dm 
import time

geolocator = Nominatim(user_agent="my_map_app")
address = '6201 Negros Oriental, Sibulan'
location = geolocator.geocode(address)
loc = [location.latitude, location.longitude]

map = folium.Map(location=loc, zoom_start=16)
dm.showMap(map)