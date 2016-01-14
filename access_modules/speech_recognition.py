import requests


def start_speech_recognition():
    requests.get('http://192.168.1.15:8080/recognize')

