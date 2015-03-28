#!/usr/bin/python
import os


def switch_off():
    os.system('sudo /opt/vc/bin/tvservice -o')


def switch_on():
    os.system("sudo /opt/vc/bin/tvservice -p; sudo chvt 6; sudo chvt 7")
