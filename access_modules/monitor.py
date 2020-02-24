import subprocess
from enum import Enum
from threading import Timer
from access_modules import camera

MONITOR_ON_TIME = 80.0
g_timer = None


class Status(Enum):
    ON = "ON"
    OFF = "OFF"


def switch_off():
    global g_timer
    camera.quit_camera()
    subprocess.call("vcgencmd display_power 0", shell=True)
    g_timer = None


def switch_on():
    global g_timer
    subprocess.call("vcgencmd display_power 1", shell=True)
    g_timer = Timer(MONITOR_ON_TIME, switch_off)
    g_timer.start()


def status():
    out = subprocess.check_output("vcgencmd display_power", universal_newlines=True, shell=True)
    if "display_power=0" in out:
        return Status.OFF
    else:
        return Status.ON


def reset_timer():
    global g_timer
    if g_timer:
        g_timer.cancel()
        g_timer = Timer(MONITOR_ON_TIME, switch_off)
        g_timer.start()
