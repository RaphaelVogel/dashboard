import requests


def get_weather_data():
    resp = requests.get('http://ha:8080/weather/current')
    return resp.json()
