import requests
import configparser

cfg = configparser.ConfigParser()
cfg.read('/home/pi/dashboard/tools/config.txt')

base_url = cfg['base']['url']


def get_solar_data():
    resp = requests.get(base_url + '/solar/current', timeout=4)
    if resp.status_code != 200:
        return None
    else:
        return resp.json()  # returns a python dictionary
