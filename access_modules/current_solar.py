import requests
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('/home/pi/dashboard/tools/config.txt')
base_url = config.get('base', 'url')


def get_solar_data():
    resp = requests.get(base_url + '/solar/current', timeout=4)
    if resp.status_code != 200:
        return None
    else:
        return resp.json()  # returns a python dictionary
