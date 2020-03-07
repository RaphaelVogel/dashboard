from omxplayer.player import OMXPlayer  # pylint: disable=import-error
from threading import Lock
from access_modules import cfg, chromium


g_player = None
lock = Lock()


def display_rtsp_stream(number):
    camera_url = cfg['cam' + str(number)]['url']
    lock.acquire()
    global g_player
    if not g_player:
        # first call - for parameters see https://github.com/popcornmix/omxplayer#synopsis
        g_player = OMXPlayer(camera_url, ['--no-osd', '--no-keys', '--live'])
    else:
        if g_player.get_source() != camera_url:
            g_player.load(camera_url)  # play new stream

    lock.release()


def display_mjpeg_stream(number):
    camera_url = cfg['cam' + str(number)]['url']
    chromium.open_url(camera_url)


def quit_rtsp_stream():
    lock.acquire()
    global g_player
    if g_player:
        g_player.quit()
        g_player = None
    lock.release()
