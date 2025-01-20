import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="weatherApp") #this is a geocoding service that is part of OpenStreetMap
city = input("Please enter your city: ")
url = "https://www.google.com/search?q="+city+" nelongitude and latitude"
html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')



def get_lat_lon(city):
    location = geolocator.geocode(city)
    if location:
        return location.latitude, location.longitude
    else:
        return None, None


latitude, longitude = get_lat_lon(city)
print(f"{longitude}, {latitude}")

# def get_temperature():
    
