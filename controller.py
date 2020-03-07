#!/usr/bin/python
import time
import board
import busio
import adafruit_mpr121
from access_modules import chromium


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
    11: "display_maps_meckesheim_heilbronn"
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


def display_camera_hof():
    chromium.open_url("localhost:8080/i_display_rtsp_camera/1")


def display_maps_meckesheim_heilbronn():
    chromium.open_url("localhost:8080/i_show_url/meckesheim-heilbronn")


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

        time.sleep(0.10)


if __name__ == '__main__':
    setup_touch_loop()
