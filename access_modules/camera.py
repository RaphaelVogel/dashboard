import ConfigParser
import requests

config = ConfigParser.RawConfigParser()
config.read('/home/pi/dashboard/tools/config.txt')


def get_camera_data(number):
    camera_name = config.get('cam' + number, 'name')
    camera_url = config.get('cam' + number, 'url')
    return {name: camera_name, url: camera_url}
