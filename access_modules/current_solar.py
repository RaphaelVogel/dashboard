import requests
import configparser
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
cfg = configparser.ConfigParser()
cfg.read(Path(root_dir, 'tools/config.txt'))

base_url = cfg['base']['url']


def get_solar_data():
    resp = requests.get(base_url + '/solar/current', timeout=4)
    if resp.status_code != 200:
        return None
    else:
        return resp.json()  # returns a python dictionary
