import requests


def get_solar_data():
    resp = requests.get('http://ha:8080/solar/current')
    return resp.json()
