import requests
from datetime import datetime

def get_weather(location, api_key, weather_config):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"
    response = requests.get(url)
    try:
        response.raise_for_status()
        data = response.json()
        weather = {}
        if weather_config['show_time']:
            weather['time'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if weather_config['show_temperature']:
            weather['temperature'] = data['main']['temp']
        if weather_config['show_description']:
            weather['description'] = data['weather'][0]['description']
        if weather_config['show_humidity']:
            weather['humidity'] = data['main']['humidity']
        if weather_config['show_wind_speed']:
            weather['wind_speed'] = data['wind']['speed']
        return weather
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except Exception as err:
        return f"Other error occurred: {err}"

def get_forecast(location, api_key, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={location}&cnt={days*8}&appid={api_key}&units=metric"
    response = requests.get(url)
    try:
        response.raise_for_status()
        data = response.json()
        forecast = {}
        for item in data['list']:
            date = datetime.fromtimestamp(item['dt']).strftime('%Y-%m-%d')
            if date not in forecast:
                forecast[date] = {
                    "temperature": item['main']['temp'],
                    "description": item['weather'][0]['description']
                }
        return forecast
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP error occurred: {http_err} - {response.text}"
    except Exception as err:
        return f"Other error occurred: {err}"

def is_valid_location(location, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        print(f"API response for location validation: {response.status_code} - {response.text}")
        return False
