# # 2. API Interaction (Weather Data Fetching)  
# 📌 **Task:** Write a Python script that fetches weather data from an API and processes the response.  
# ✅ **Instructions:**  
# - Sign up at [OpenWeatherMap](https://home.openweathermap.org/users/sign_up) and get a free API key.  
# - Fetch weather details (temperature, weather condition, humidity) for a given city.  
# - Example output:  
# Weather in Lagos: 
# Temperature: 30°C 
# Condition: Clear sky 
# Humidity: 75%

import requests

def get_weather(city_name, api_key):
    # Base URL for OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Parameters for the API request
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"  # to get temperature in Celsius
    }
    
    # Sending the GET request
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        # Parsing the JSON response
        data = response.json()
        temperature = data['main']['temp']
        condition = data['weather'][0]['description']
        humidity = data['main']['humidity']
        
        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition.capitalize()}")
        print(f"Humidity: {humidity}%")
    else:
        print("Error fetching data. Please check the city name or API key.")

# Replace 'your_api_key' with your actual API key from OpenWeatherMap
api_key = "fd9708a7c7664e2462c6e347d484e65c"  
city_name = "Lagos"  # Example city
get_weather(city_name, api_key)