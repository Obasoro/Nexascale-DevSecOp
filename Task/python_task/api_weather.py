# Import the required libraries
import requests

# Enter the api key of openwaethermap here

api_key = "fd9708a7c7664e2462c6e347d484e65c"

# Base url for the open map api

root_url = "http://api.openweathermap.org/data/2.5/weather?"

# City namr for which we need weather data

city_name = input("Enter city name: ")

# Complete url for the api request

url = root_url + "appid=" + api_key + "&q=" + city_name

req = requests.get(url)

print(req.json())

data = req.json()

if data['cod'] == 200:
    pressure = data['main']['pressure']
    humidity = data['main']['humidity']
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    main = data['main']
    wind = data['wind']
    weather_desc = data['weather'][0]['description']
    

    print(f"City Name: + {city_name}")

    print(f"Weather conditions is {weather_desc}")
    print(f"Temperature is {temp} Celcius")
    print(f"Humidity is {humidity}%")
    print(f"Pressure is {pressure} hPa")
    print(f"Wind Speed is {wind_speed} m/s")
    print("Temperature: " + str(main['temp']))
    print("Humidity: " + str(main['humidity']))
    print("Wind Speed: " + str(wind['speed']))
    print("Description: " + str(weather_desc)) 

else:
    print("City not found")
