import requests
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('/home/pi/dashboard/tools/config.txt')
base_url = config.get('base', 'url')


def get_weather_data():
    resp = requests.get(base_url + '/weather/current', timeout=3)
    return resp.json()  # returns a python dictionary
