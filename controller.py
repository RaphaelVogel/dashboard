#!/usr/bin/python
import time
import board
import busio
import adafruit_mpr121
import logging
from pathlib import Path
from access_modules import chromium
from logging.handlers import RotatingFileHandler

current_dir = Path(__file__).resolve().parent
logger = logging.getLogger("dashboard_logger")
logger.setLevel(logging.WARN)
filehandler = RotatingFileHandler(Path(current_dir, 'log_controller.txt'), maxBytes=100000, backupCount=3)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s', datefmt='%d-%m-%Y %H:%M:%S')
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)


# Define mapping of capacitive touch pin to method calls
pin_method_mapping = {
    0: "display_soccer_table1",
    1: "display_soccer_table2",
    2: "",
    3: "display_current_solar",
    4: "display_current_time",
    5: "display_soccer_matches1",
    6: "display_soccer_matches2",
    7: "display_pic_of_the_day",
    8: "display_camera_hof",
    9: "",
    10: "",
    11: ""
}

IRQ_PIN = 26
EVENT_WAIT_SLEEP_SECONDS = 0.15


# --- Define functions to call if button is touched ------------------------------------------------------------------
def display_soccer_table1():
    chromium.open_url("localhost:8080/i_soccerTable/1")


def display_soccer_table2():
    chromium.open_url("localhost:8080/i_soccerTable/2")


def display_soccer_matches1():
    chromium.open_url("localhost:8080/i_soccerMatches/1")


def display_soccer_matches2():
    chromium.open_url("localhost:8080/i_soccerMatches/2")


def display_current_solar():
    chromium.open_url("localhost:8080/i_currentSolar")


def display_current_time():
    chromium.open_url("localhost:8080/i_currentTime")


def display_pic_of_the_day():
    chromium.open_url("localhost:8080/i_picOfTheDay")


def display_camera():
    chromium.open_url("localhost:8080/i_display_camera/1")


# --- Setup the MPR121 device ------------------------------------------------------------------------------------
def setup_touch_loop():
    i2c = busio.I2C(board.SCL, board.SDA)
    mpr121 = adafruit_mpr121.MPR121(i2c)
    while True:
        for i in range(12):
            if mpr121[i].value:
                function_name = pin_method_mapping[i]
                if function_name:
                    # call function
                    globals()[function_name]()

        time.sleep(0.15)  # Small delay to keep from spamming output messages.


if __name__ == '__main__':
    setup_touch_loop()
