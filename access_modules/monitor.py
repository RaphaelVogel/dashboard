import subprocess
import logging
from enum import Enum
from subprocess import CalledProcessError
from threading import Timer

logger = logging.getLogger("dashboard_logger")
MONITOR_ON_TIME = 180.0


class Status(Enum):
    ON = "ON"
    OFF = "OFF"


def switch_off():
    try:
        subprocess.call("vcgencmd display_power 0", shell=True)
    except CalledProcessError:
        logger.warning('Cannot switch off monitor')


def switch_on():
    try:
        subprocess.call("vcgencmd display_power 1", shell=True)
        timer = Timer(MONITOR_ON_TIME, switch_off)
        timer.start()
    except CalledProcessError:
        logger.warning('Cannot switch on monitor')


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
