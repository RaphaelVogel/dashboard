import requests


def get_solar_data():
    resp = requests.get('http://ha:8080/solar/current')
    if resp.status_code != 200:
        return None
    else:
        return resp.json()  # returns a python dictionary
