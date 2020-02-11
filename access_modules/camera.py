from omxplayer.player import OMXPlayer  # pylint: disable=import-error
from threading import Timer
from access_modules import cfg


g_camera_url = None
CAMERA_ON_TIME = 40.0


def display_camera_data(number):
    camera_url = cfg['cam' + str(number)]['url']
    global g_camera_url
    if camera_url == g_camera_url:
        return
    player = OMXPlayer(camera_url)
    g_camera_url = camera_url
    timer = Timer(CAMERA_ON_TIME, _quit_camera, args=(player,))
    timer.start()


def _quit_camera(player):
    player.quit()
    global g_camera_url
    g_camera_url = None
