import subprocess
import logging
from enum import Enum
from subprocess import CalledProcessError
from threading import Timer

logger = logging.getLogger("dashboard_logger")

TIMER_RUNNING = False
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


# --- Start thread to turn off monitor ------------------------------------------------------------------------------
def _turn_monitor_off():
    switch_off()
    global TIMER_RUNNING
    TIMER_RUNNING = False


def start_timer():
    timer = Timer(MONITOR_ON_TIME, _turn_monitor_off)
    timer.start()
    global TIMER_RUNNING
    TIMER_RUNNING = True
