from omxplayer.player import OMXPlayer  # pylint: disable=import-error
from threading import Timer, Lock
from access_modules import cfg, monitor


g_player = None
g_timer = None
CAMERA_ON_TIME = 100.0
lock = Lock()


def display_camera_data(number):
    camera_url = cfg['cam' + str(number)]['url']
    global g_player, g_timer
    lock.acquire()
    if not g_player:
        # first call
        g_player = OMXPlayer(camera_url)
        g_timer = Timer(CAMERA_ON_TIME, quit_camera)
        g_timer.start()
        monitor.reset_timer()
    else:
        if g_player.get_source() != camera_url:
            # play new stream
            g_player.load(camera_url)

        # reset camera and monitor timer
        g_timer.cancel()
        g_timer = Timer(CAMERA_ON_TIME, quit_camera)
        g_timer.start()
        monitor.reset_timer()
    lock.release()


def quit_camera():
    global g_player, g_timer
    if g_player:
        g_player.quit()
        g_player = None
    if g_timer:
        g_timer.cancel()
        g_timer = None


def camera_active():
    global g_player
    return g_player is not None
