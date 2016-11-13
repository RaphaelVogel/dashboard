import requests
import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('/home/pi/dashboard/tools/config.txt')
base_url = config.get('base', 'url')


def get_alarm_logs():
    resp = requests.get(base_url + '/alarmLog', timeout=3)
    if resp.status_code != 200:
        return None
    else:
        return resp.json()  # returns a python dictionary


def get_alarm_status():
    resp = requests.get(base_url + '/alarmStatus', timeout=3)
    if resp.status_code != 200:
        return None
    else:
        return resp.json()  # returns a python dictionary