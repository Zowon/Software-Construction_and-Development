import requests

# API Endpoint and Key (Replace with your own API key if available)
API_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "your_api_key_here"  # Replace with an actual OpenWeatherMap API key

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        print(f"City: {data['name']}")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Weather: {data['weather'][0]['description']}")
    else:
        print("Error: Unable to fetch weather data.")

# Get weather for a specific city
city_name = input("Enter city name: ")
get_weather(city_name)
