#!/usr/bin/python
import subprocess


def switch_off():
    subprocess.call("sudo /opt/vc/bin/tvservice -o", shell=True)


def switch_on():
    subprocess.call("sudo /opt/vc/bin/tvservice -p; sudo chvt 6; sudo chvt 7", shell=True)


def status():
    out = subprocess.check_output("sudo /opt/vc/bin/tvservice -s", shell=True)
    if "TV is off" in out:
        return "OFF"
    else:
        return "ON"