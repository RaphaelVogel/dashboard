import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('/home/pi/dashboard/tools/config.txt')
base_url = config.get('cam1', 'url')


def get_camera_data(number):
    return {name: config.get('cam' + number, 'name'), url: config.get('cam' + number, 'url')}