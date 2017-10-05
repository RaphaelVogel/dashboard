#!/usr/bin/python
import subprocess
from threading import Timer

TIMER_RUNNING = False
TIMER_START = 210.0


def switch_off():
    subprocess.call("/opt/vc/bin/tvservice -o", shell=True)


def switch_on():
    subprocess.call("/opt/vc/bin/tvservice -p; sudo chvt 6; sudo chvt 7", shell=True)


def status():
    out = subprocess.check_output("/opt/vc/bin/tvservice -s", universal_newlines=True, shell=True)
    if "TV is off" in out:
        return "OFF"
    else:
        return "ON"


# --- Start thread to turn off monitor ------------------------------------------------------------------------------
def turn_monitor_off():
    switch_off()
    global TIMER_RUNNING
    TIMER_RUNNING = False


def start_timer():
    timer = Timer(TIMER_START, turn_monitor_off)
    timer.start()
    global TIMER_RUNNING
    TIMER_RUNNING = True
