from weather import Weather
from pprint import pprint
import json


if __name__ == "__main__":
    with open("config.json", "r") as file:
        config = json.load(file)

    weather = Weather("Liepāja", config["API_KEY"])
    print(weather)