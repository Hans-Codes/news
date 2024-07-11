import json

def load_config():
    with open('config.json', 'r') as f:
        config = json.load(f)
    return config

def get_user_location():
    location = input("Enter the city/town/country you want to see updates for: ").strip()
    return location
