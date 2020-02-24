from omxplayer.player import OMXPlayer  # pylint: disable=import-error
from threading import Lock
from access_modules import cfg, monitor


g_player = None
lock = Lock()


def display_camera_data(number):
    camera_url = cfg['cam' + str(number)]['url']
    lock.acquire()
    global g_player
    if not g_player:
        # first call - for parameters see https://github.com/popcornmix/omxplayer#synopsis
        g_player = OMXPlayer(camera_url, ['--no-osd', '--no-keys', '-b', '--live'])
        monitor.reset_timer()
    else:
        if g_player.get_source() != camera_url:
            g_player.load(camera_url)  # play new stream

        # reset monitor timer
        monitor.reset_timer()
    lock.release()


def quit_camera():
    lock.acquire()
    global g_player
    if g_player:
        g_player.quit()
        g_player = None
    lock.release()


def camera_active():
    lock.acquire()
    global g_player
    status = g_player is not None
    lock.release()
    return status
