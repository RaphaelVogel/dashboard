#!/usr/bin/python
from access_modules import iceweasel, monitor
import sys
import time
import atexit
from threading import Timer

import Adafruit_MPR121.MPR121 as MPR121
import RPi.GPIO as GPIO

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
    8: "display_ebay()",
    9: None,
    10: None,
    11: None,
}

IRQ_PIN = 26
EVENT_WAIT_SLEEP_SECONDS = 0.15

TIMER_RUNNING = False
TIMER_START = 300.0


# --- Start thread to turn off monitor ------------------------------------------------------------------------------
def turn_monitor_off():
    monitor.switch_off()
    global TIMER_RUNNING
    TIMER_RUNNING = False


def start_timer():
    timer = Timer(TIMER_START, turn_monitor_off)
    timer.start()
    global TIMER_RUNNING
    TIMER_RUNNING = True


# --- Define functions to call if button is touched ------------------------------------------------------------------
def display_soccer_table1():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/soccerTable/1")
    if not TIMER_RUNNING:
        start_timer()


def display_soccer_table2():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/soccerTable/2")
    if not TIMER_RUNNING:
        start_timer()


def display_soccer_matches1():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/soccerMatches/1")
    if not TIMER_RUNNING:
        start_timer()


def display_soccer_matches2():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/soccerMatches/2")
    if not TIMER_RUNNING:
        start_timer()


def display_current_weather():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/currentWeather")
    if not TIMER_RUNNING:
        start_timer()


def display_current_solar():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/currentSolar")
    if not TIMER_RUNNING:
        start_timer()


def display_current_time():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/currentTime")
    if not TIMER_RUNNING:
        start_timer()


def display_pic_of_the_day():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/picOfTheDay")
    if not TIMER_RUNNING:
        start_timer()


def display_ebay():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/ebay")
    if not TIMER_RUNNING:
        start_timer()


# --- Setup the MPR121 device ------------------------------------------------------------------------------------
def setup_touch_loop():
    cap = MPR121.MPR121()
    if not cap.begin():
        print 'Failed to initialize MPR121, check your wiring!'
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
        # Check which ey presses for any touched keys.
        for pin, function_to_call in PIN_METHOD_MAPPING.iteritems():
            pin_bit = 1 << pin
            if touched & pin_bit:
                if function_to_call:
                    eval(function_to_call)


if __name__ == '__main__':
    setup_touch_loop()
