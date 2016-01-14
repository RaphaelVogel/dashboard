import requests


def start_speech_recognition():
    resp = requests.get('http://192.168.1.15/recognize')

