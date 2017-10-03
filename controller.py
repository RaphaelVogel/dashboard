#!/usr/bin/python3
from access_modules import chromium, monitor
import sys
import time
import atexit
import logging
from logging.handlers import RotatingFileHandler

import Adafruit_MPR121.MPR121 as MPR121
import RPi.GPIO as GPIO

logger = logging.getLogger("controller_logger")
logger.setLevel(logging.WARN)
filehandler = RotatingFileHandler('./dashboard/log_controller.txt', maxBytes=100000, backupCount=3)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s', datefmt='%d-%m-%Y %H:%M:%S')
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)


# Define mapping of capacitive touch pin to method calls
PIN_METHOD_MAPPING = {
    0: "display_soccer_table1()",
    1: "display_soccer_table2()",
    2: "display_current_weather()",
    3: "display_current_solar()",
    4: "display_current_time()",
    5: "display_soccer_matches1()",
    6: "display_soccer_matches2()",
    7: "display_pic_of_the_day()",
    8: "display_camera()",
    9: "",
    10: "meckesheim_liga()",
    11: "alarm_status()"
}

IRQ_PIN = 26
EVENT_WAIT_SLEEP_SECONDS = 0.15


# --- Define functions to call if button is touched ------------------------------------------------------------------
def display_soccer_table1():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_soccerTable/1")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()


def display_soccer_table2():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_soccerTable/2")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()


def display_soccer_matches1():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_soccerMatches/1")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()


def display_soccer_matches2():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_soccerMatches/2")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()


def display_current_weather():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_currentWeather")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()


def display_current_solar():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_currentSolar")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()


def display_current_time():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_currentTime")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()


def display_pic_of_the_day():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_picOfTheDay")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()


def display_camera():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_display_camera/1")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()


def meckesheim_liga():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    chromium.open_url("www.fussball.de/mannschaft/fc-germ-meckesheim-moenchzell-fc-germ-meckesheim-moenchzell-baden/-/saison/1617/team-id/01L785U8VS000000VV0AG80NVT9OCUEA#!/section/teamFixturesMatchdayLeagueTable")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()


def alarm_status():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_alarm_status")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()


# --- Setup the MPR121 device ------------------------------------------------------------------------------------
def setup_touch_loop():
    cap = MPR121.MPR121()
    if not cap.begin():
        print('Failed to initialize MPR121, check your wiring!')
        sys.exit(1)

    # Configure GPIO library to listen on IRQ pin for changes.
    # Be sure to configure pin with a pull-up because it is open collector when not
    # enabled.
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(IRQ_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(IRQ_PIN, GPIO.FALLING)
    atexit.register(GPIO.cleanup)

    # Clear any pending interrupts by reading touch state.
    cap.touched()

    while True:
        # Wait for the IRQ pin to drop
        while not GPIO.event_detected(IRQ_PIN):
            time.sleep(EVENT_WAIT_SLEEP_SECONDS)
        # Read touch state.
        touched = cap.touched()
        # Check which key presses for any touched keys.
        for pin, function_to_call in PIN_METHOD_MAPPING.iteritems():
            pin_bit = 1 << pin
            if touched & pin_bit:
                if function_to_call:
                    eval(function_to_call)
                    break


if __name__ == '__main__':
    setup_touch_loop()
