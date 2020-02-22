import subprocess
import logging
from enum import Enum
from subprocess import CalledProcessError
from threading import Timer

logger = logging.getLogger("dashboard_logger")
MONITOR_ON_TIME = 180.0
g_timer = None


class Status(Enum):
    ON = "ON"
    OFF = "OFF"


def switch_off():
    global g_timer
    try:
        subprocess.call("vcgencmd display_power 0", shell=True)
        g_timer = None
    except CalledProcessError:
        logger.warning('Cannot switch off monitor')


def switch_on():
    global g_timer
    try:
        subprocess.call("vcgencmd display_power 1", shell=True)
        g_timer = Timer(MONITOR_ON_TIME, switch_off)
        g_timer.start()
    except CalledProcessError:
        logger.warning('Cannot switch on monitor')


def reset_timer():
    global g_timer
    if g_timer:
        g_timer.cancel()
        g_timer = Timer(MONITOR_ON_TIME, switch_off)
        g_timer.start()


def status():
    out = ""
    try:
        out = subprocess.check_output("vcgencmd display_power", universal_newlines=True, shell=True)
    except CalledProcessError:
        logger.warning('Cannot get monitor status')
        return None

    if "display_power=0" in out:
        return Status.OFF
    else:
        return Status.ON
