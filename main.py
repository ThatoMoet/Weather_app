import requests
from bs4 import BeautifulSoup
from geopy.geocoders import Nominatim
latitude=0
longitude=0
parameters={}

geolocator = Nominatim(user_agent="weatherApp") #this is a geocoding service that is part of OpenStreetMap
city = input("Please enter your city: ")
map_url = "https://www.google.com/search?q="+city+" longitude and latitude"
html = requests.get(map_url).content

soup = BeautifulSoup(html, 'html.parser')


def get_lat_long(city):
    location = geolocator.geocode(city)
    if location:
        return round(location.latitude,2), round(location.longitude,2)
    else:
        return None, None

def get_current_weather():
    url="https://api.open-meteo.com/v1/forecast"
    parameters={
        "latitude":latitude,
        "longitude": longitude,
        "hourly":"temperature_2m"
        
         }
    response=requests.get(url,params=parameters)
    return response.json()
    
    

latitude, longitude = get_lat_long(city)

weather=get_current_weather()
print(weather)

# def get_weather():
    
