import time
import json
from weather import get_weather, get_forecast, is_valid_location
from news import get_news
from utils import load_config, get_user_location

def main():
    config = load_config()
    
    while True:
        location = get_user_location()
        if is_valid_location(location, config['api_keys']['openweathermap']):
            break
        else:
            print("Invalid location. Please try again.")
    
    try:
        while True:
            print(f"Location: {location}")
            print("------------------------------------------------")
            
            if config['weather']['enabled']:
                weather = get_weather(location, config['api_keys']['openweathermap'], config['weather'])
                print("Weather:")
                if config['weather']['show_time']:
                    print(f"Time: {weather['time']}")
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
                news = get_news(location, category, config['api_keys']['newsapi'])
                print(f"{category.capitalize()} News:")
                if news:
                    for article in news:
                        if config['news']['show_links']:
                            print(f"{article['title']}: {article['url']}")
                        else:
                            print(f"{article['title']}")
                else:
                    print("No news available.")
                print("------------------------------------------------")
            
            time.sleep(config['update_interval'] * 60)
    except KeyboardInterrupt:
        print("\nExiting the application. Goodbye!")

if __name__ == "__main__":
    main()
