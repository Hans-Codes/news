# Console-based Weather and News App

## Overview
This is a console-based application that provides weather updates and news about a user-chosen location. The app updates every few minutes based on user configuration.

## Features
- Displays current weather information (time, temperature, description, humidity, wind speed)
- Provides weather forecast for up to 7 days
- Shows news articles based on user-selected categories
- Customizable configuration through a JSON file
- Supports any valid location
- Clean and organized console output
- Uses [OpenWeatherMap](https://openweathermap.org) and [News API](https://newsapi.org/), which are both free to use.

## Requirements
- Python 3.x
- Requests library

## Setup
1. Clone or download the repository.
2. Navigate to the project directory.
3. Install the required dependencies:
    ```
    pip install requests
    ```
4. Run the app
    ```
    python main.py
    ```
    
## Configuration
You can setup your API keys and preferences such as what category of news to check, how many days of weather forecasts, what to show in the weather update, update interval inside the config.json file.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, you can do so in the following ways:

- Fork the repository and create your branch from main.
- Make your changes and test thoroughly.
- Ensure your code follows the existing style and conventions.
- Submit a pull request detailing your changes and any relevant information.

## License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License
