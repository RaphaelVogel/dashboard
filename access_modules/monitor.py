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
        subprocess.call("/opt/vc/bin/tvservice -o", shell=True)
    except CalledProcessError:
        logger.warning('Cannot switch off monitor')


def switch_on():
    try:
        subprocess.call("/opt/vc/bin/tvservice -p; sudo chvt 6; sudo chvt 7", shell=True)
        timer = Timer(MONITOR_ON_TIME, switch_off)
        timer.start()
    except CalledProcessError:
        logger.warning('Cannot switch on monitor')


def status():
    out = ""
    try:
        out = subprocess.check_output("/opt/vc/bin/tvservice -s", universal_newlines=True, shell=True)
    except CalledProcessError:
        logger.warning('Cannot get monitor status')
        return None

    if "TV is off" in out:
        return Status.OFF
    else:
        return Status.ON
