import requests
from datetime import datetime

class Weather:
    def __init__(self, city_name, API_KEY): # Finds a city by name and gets its weather
        self.API_KEY = API_KEY
        self.city = self.find_city(city_name)

        self.temperature = None
        self.max_temperature = None
        self.min_temperature = None
        self.humidity = None
        self.pressure = None

        self.sunrise_timestamp = None
        self.sunset_timestamp = None

        self.timezone = None
        self.visibility = None

        self.wind_speed = None
        self.wind_degree = None
        
        self.update()

    def find_city(self, city_name) -> dict: # Gets information about a city by its name
        with requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},&appid={self.API_KEY}") as response:
            try:
                return response.json()[0]
            except KeyError:
                raise Exception("Invalid API key was provided.")
            except IndexError:
                raise Exception("The city was not found.")
            
    def update(self) -> None: # Gets weather information by coordinates (we got the coordinates of the city in find_city)
        with requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={self.city["lat"]}&lon={self.city["lon"]}&appid={self.API_KEY}&units=metric") as response:
            if response.status_code != 200:
                raise Exception(f"Unexpected statuscode received from openweather API ({response.status_code}).")
            weather_json = response.json()

        self.temperature = weather_json["main"]["temp"]
        self.max_temperature = weather_json["main"]["temp_max"]
        self.min_temperature = weather_json["main"]["temp_min"]
        self.humidity = weather_json["main"]["humidity"]
        self.pressure = weather_json["main"]["pressure"]

        self.sunrise_timestamp = weather_json["sys"]["sunrise"]
        self.sunset_timestamp = weather_json["sys"]["sunset"]

        self.timezone = weather_json["timezone"]
        self.visibility = weather_json["visibility"]

        self.wind_speed = weather_json["wind"]["speed"]
        self.wind_degree = weather_json["wind"]["deg"]

    def __str__(self):
        return f"""
Weather in {self.city["name"]}:
    Temperature: {self.temperature}
    Temperature amplitude: {self.max_temperature - self.min_temperature:.2f}
    Humidity: {self.humidity}
    Wind speed: {self.wind_speed}
    Pressure: {self.pressure}
    Sunrise at {datetime.fromtimestamp(self.sunrise_timestamp).strftime("%H:%M")}
    Sunset at {datetime.fromtimestamp(self.sunset_timestamp).strftime("%H:%M")}
"""