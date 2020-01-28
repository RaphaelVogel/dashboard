import configparser

cfg = configparser.ConfigParser()
cfg.read('./tools/config.txt')


def get_camera_data(number):
    camera_name = cfg['cam' + str(number)]['name']
    camera_url = cfg['cam' + str(number)]['url']
    return {'name': camera_name, 'url': camera_url}
