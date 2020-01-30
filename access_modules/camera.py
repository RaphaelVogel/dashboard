import configparser
import time
from omxplayer.player import OMXPlayer


cfg = configparser.ConfigParser()
cfg.read('./tools/config.txt')


def display_camera_data(number):
    camera_url = cfg['cam' + str(number)]['url']
    player = OMXPlayer(camera_url)
    time.sleep(15)
    player.quit()
