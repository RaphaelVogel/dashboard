import requests


def play_radio():
    requests.get('http://192.168.1.15:8080/playRadio')


def stop_radio():
    requests.get('http://192.168.1.15:8080/stopRadio')


def increase_volume():
    requests.get('http://192.168.1.15:8080/increaseVolume')


def decrease_volume():
    requests.get('http://192.168.1.15:8080/decreaseVolume')