import sys
from db import Db
from weather import WeatherRequest

if __name__ == '__main__':
    while True:
        user_input = input("Input city name to get current weather or q to exit")
        if user_input == 'q':
            break
        weather = WeatherRequest(Db())
        data = weather.request(user_input)
        print(data)
        print(weather.parse(data))