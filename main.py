# main.py

import time
import json
from datetime import datetime
from pytz import timezone, UnknownTimeZoneError
from weather import get_weather, get_forecast, is_valid_location
from news import get_news
from utils import load_config, get_user_location, get_timezone

def main():
    config = load_config()
    output_number = 1
    shown_news_titles = set()
    
    while True:
        location = get_user_location()
        formatted_location = location.title()  # Capitalize the first letter of each word
        if is_valid_location(location, config['api_keys']['openweathermap']):
            break
        else:
            print("Invalid location. Please try again.")
    
    try:
        while True:
            if output_number > 1:
                # Add a few blank lines before each update
                print("\n" * 3)
            
            print(f"Output: {output_number}")
            print("------------------------------------------------")
            print(f"Location: {formatted_location}")
            
            # Fetch timezone info for the location
            try:
                tz_name = get_timezone(location)
                if tz_name:
                    tz = timezone(tz_name)
                    location_time = datetime.now(tz)
                else:
                    location_time = None
            except UnknownTimeZoneError:
                location_time = None
            
            print("------------------------------------------------")
            
            if config['weather']['enabled']:
                weather = get_weather(location, config['api_keys']['openweathermap'], config['weather'])
                print("Weather:")
                if config['weather']['show_time']:
                    if location_time:
                        print(f"{formatted_location} Local Time: {location_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")
                    else:
                        print(f"{formatted_location} Local Time: N/A (Timezone information not available)")
                if config['weather']['show_temperature']:
                    print(f"Temperature: {weather['temperature']}°C")
                if config['weather']['show_description']:
                    print(f"Description: {weather['description']}")
                if config['weather']['show_humidity']:
                    print(f"Humidity: {weather['humidity']}%")
                if config['weather']['show_wind_speed']:
                    print(f"Wind Speed: {weather['wind_speed']} m/s")
                
                if config['weather']['show_forecast']:
                    forecast = get_forecast(location, config['api_keys']['openweathermap'], config['weather']['forecast_days'])
                    print("Forecast:")
                    for date, info in forecast.items():
                        print(f"{date}: {info['temperature']}°C, {info['description']}")
                
                print("------------------------------------------------")
            
            news_categories = [category for category, enabled in config['news'].items() if enabled and category != "show_links"]
            for category in news_categories:
                news = get_news(location, category, config['api_keys']['newsapi'], shown_news_titles)
                print(f"{category.capitalize()} News:")
                if news:
                    for article in news:
                        title = article['title']
                        if title not in shown_news_titles:
                            if config['news']['show_links']:
                                print(f"{title}: {article['url']}")
                            else:
                                print(f"{title}")
                            shown_news_titles.add(title)
                else:
                    print("No news available.")
                print("------------------------------------------------")
            
            output_number += 1
            time.sleep(config['update_interval'] * 60)
    except KeyboardInterrupt:
        print("\nExiting the application. Goodbye!")

if __name__ == "__main__":
    main()
