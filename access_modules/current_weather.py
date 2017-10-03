import requests
import configparser

cfg = configparser.ConfigParser()
cfg.read('/home/pi/dashboard/tools/config.txt')

base_url = cfg['base']['url']


def get_weather_data():
    resp = requests.get(base_url + '/weather/current', timeout=3)
    return resp.json()  # returns a python dictionary
