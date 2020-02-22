from omxplayer.player import OMXPlayer  # pylint: disable=import-error
from threading import Timer
from access_modules import cfg


g_player = None
CAMERA_ON_TIME = 40.0


def display_camera_data(number):
    camera_url = cfg['cam' + str(number)]['url']
    global g_player
    if not g_player:
        # first call
        g_player = OMXPlayer(camera_url)
        Timer(CAMERA_ON_TIME, quit_camera).start()
    else:
        if g_player.get_source() != camera_url:
            # play new stream
            g_player.load(camera_url)
        else:
            # already playing requested stream, do nothing
            pass


def quit_camera():
    global g_player
    g_player.quit()
    g_player = None


def camera_active():
    global g_player
    return g_player is not None
