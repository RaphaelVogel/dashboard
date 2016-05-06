import requests
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('/home/pi/dashboard/tools/config.txt')
base_url = config.get('base', 'url')


def play_radio():
    requests.get(base_url + '/playRadio')


def stop_radio():
    requests.get(base_url + '/stopRadio')


def increase_volume():
    requests.get(base_url + '/increaseVolume')


def decrease_volume():
    requests.get(base_url + '/decreaseVolume')
