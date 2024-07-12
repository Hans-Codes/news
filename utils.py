# utils.py

import json
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

def get_user_location():
    location = input("Enter the city/town/country you want to see updates for: ")
    return location

def get_timezone(location):
    geolocator = Nominatim(user_agent="weather_app")
    location = geolocator.geocode(location)
    
    if location:
        tf = TimezoneFinder()
        timezone_str = tf.timezone_at(lng=location.longitude, lat=location.latitude)
        return timezone_str
    else:
        return None

def is_valid_location(location, api_key):
    geolocator = Nominatim(user_agent="weather_app")
    location_data = geolocator.geocode(location, language='en')
    
    if location_data:
        return True
    else:
        return False
