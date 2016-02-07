import requests


def start_radio():
    requests.get('http://192.168.1.15:8080/playRadio')


def stop_radio():
    requests.get('http://192.168.1.15:8080/stopRadio')
