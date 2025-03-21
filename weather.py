import requests
from pprint import pprint


class Weather:
    def __init__(self, city_name, API_KEY):
        self.API_KEY = API_KEY
        self.city = self.find_city(city_name)

        self.temperature = None
        self.max_temperature = None
        self.min_temperature = None
        self.humidity = None
        self.pressure = None

        self.sunrise_datetime = None
        self.sunset_datetime = None

        self.timezone = None
        self.visibility = None

        self.wind_speed = None
        self.wind_degree = None

        self.update()

    def find_city(self, city_name) -> dict:
        with requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},&appid={self.API_KEY}") as response:
            return response.json()[0]

    def update(self) -> None:
        with requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={self.city["lat"]}&lon={self.city["lon"]}&appid={self.API_KEY}&units=metric") as response:
            weather_json = response.json()

        self.temperature = weather_json["main"]["temp"]
        self.max_temperature = weather_json["main"]["temp_max"]
        self.min_temperature = weather_json["main"]["temp_min"]
        self.humidity = weather_json["main"]["humidity"]
        self.pressure = weather_json["main"]["pressure"]

        self.sunrise_datetime = weather_json["sys"]["sunrise"]
        self.sunset_datetime = weather_json["sys"]["sunset"]

        self.timezone = weather_json["timezone"]
        self.visibility = weather_json["visibility"]

        self.wind_speed = weather_json["wind"]["speed"]
        self.wind_degree = weather_json["wind"]["deg"]

    def __str__(self):
        return f"Current temperature is {self.temperature}°C, wind speed - {self.wind_speed} and humidity is {self.humidity}"