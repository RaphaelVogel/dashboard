import configparser
from pathlib import Path
from omxplayer.player import OMXPlayer
from threading import Timer

root_dir = Path(__file__).resolve().parent.parent
cfg = configparser.ConfigParser()
cfg.read(Path(root_dir, 'tools/config.txt'))


g_camera_url = None
g_timer_running = False
CAMERA_ON_TIME = 45.0


def display_camera_data(number):
    camera_url = cfg['cam' + str(number)]['url']
    global g_timer_running, g_camera_url
    if camera_url == g_camera_url and g_timer_running:
        return
    player = OMXPlayer(camera_url)
    g_camera_url = camera_url
    g_timer_running = True
    timer = Timer(CAMERA_ON_TIME, _quit_camera, args=(player,))
    timer.start()


def _quit_camera(player):
    player.quit()
    global g_timer_running
    g_timer_running = False
