import requests
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('/home/pi/dashboard/tools/config.txt')
base_url = config.get('base', 'url')


def play_radio():
    requests.get(base_url + '/playRadio', timeout=3)


def stop_radio():
    requests.get(base_url + '/stopRadio', timeout=3)


def increase_volume():
    requests.get(base_url + '/increaseVolume', timeout=3)


def decrease_volume():
    requests.get(base_url + '/decreaseVolume', timeout=3)
