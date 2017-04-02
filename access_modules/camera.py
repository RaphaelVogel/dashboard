import ConfigParser

config = ConfigParser.RawConfigParser()
config.read('/home/pi/dashboard/tools/config.txt')


def get_camera_data(number):
    camera_name = config.get('cam' + str(number), 'name')
    camera_url = config.get('cam' + str(number), 'url')
    return {'name': camera_name, 'url': camera_url}
