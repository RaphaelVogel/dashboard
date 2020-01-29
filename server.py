import sys
import os
import logging
from logging.handlers import RotatingFileHandler
from bottle import (
    run,
    route,
    static_file,
    HTTPResponse,
    view,
    template,
    TEMPLATE_PATH,
)
from access_modules import (
    chromium,
    monitor,
    soccer_table,
    current_solar,
    pic_of_the_day,
    camera,
)


# logger configuration
logger = logging.getLogger("dashboard_logger")
logger.setLevel(logging.WARN)
filehandler = RotatingFileHandler('./log_dashboard.txt', maxBytes=100000, backupCount=3)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s', datefmt='%d-%m-%Y %H:%M:%S')
filehandler.setFormatter(formatter)
logger.addHandler(filehandler)

# bottle initialization
current_dir = os.path.abspath(os.path.dirname(__file__))
TEMPLATE_PATH.append(os.path.join(current_dir, 'web/views/'))


# decorator to controll monitor
def monitor_handling(func):
    def wrapper(*args, **kwargs):
        status = monitor.status()
        if status == monitor.Status.OFF:
            monitor.switch_on()
        func(*args, **kwargs)
        if not monitor.TIMER_RUNNING:
            monitor.start_timer()
    return wrapper


# --- Base routes ----------------------------------------------------------------------------------------------------
@route('/')
def index():
    return static_file('index.html', root='./web')


@route('/lib/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./web/lib')


# ---------------------------------------------------------------------------------------------------------
# --- Command/public routes ---
# ---------------------------------------------------------------------------------------------------------
@route('/monitor/<status>')
def switch_monitor(status):
    if status == monitor.Status.ON:
        monitor.switch_on()
    elif status == monitor.Status.OFF:
        monitor.switch_off()
    else:
        return HTTPResponse(dict(error="Wrong url to switch monitor, use ON or OFF"), status=500)

    return dict(status="OK")


@route('/setURL/<url>')
@monitor_handling
def set_url(url):
    chromium.open_url(url)
    return dict(status="OK")


@route('/soccerTable/<liga>')
@monitor_handling
def show_soccer_table(liga):
    chromium.open_url("localhost:8080/i_soccerTable/" + liga)
    return dict(status="OK")


@route('/currentWeather')
@monitor_handling
def show_current_weather():
    chromium.open_url("localhost:8080/i_currentWeather")
    return dict(status="OK")


@route('/currentSolar')
@monitor_handling
def show_current_solar():
    chromium.open_url("localhost:8080/i_currentSolar")
    return dict(status="OK")


@route('/currentTime')
@monitor_handling
def show_current_time():
    chromium.open_url("localhost:8080/i_currentTime")
    return dict(status="OK")


@route('/soccerMatches/<liga>')
@monitor_handling
def show_soccer_matches(liga):
    chromium.open_url("localhost:8080/i_soccerMatches/" + liga)
    return dict(status="OK")


@route('/picOfTheDay')
@monitor_handling
def show_pic_of_the_day():
    chromium.open_url("localhost:8080/i_picOfTheDay")
    return dict(status="OK")


@route('/displayCamera/<cam>')
@monitor_handling
def display_camera(cam):
    chromium.open_url("localhost:8080/i_display_camera/" + cam)
    return dict(status="OK")


@route('/alarmMessage/<sensor_type>/<alarm_location>')
@monitor_handling
def alarm_message(sensor_type, alarm_location):
    chromium.open_url("localhost:8080/i_alarmMessage/" + sensor_type + "/" + alarm_location)
    return dict(status="OK")


# ---------------------------------------------------------------------------------------------------------
# --- Web/Button pressed routes ---
# ---------------------------------------------------------------------------------------------------------
@route('/i_soccerTable/<liga>')
@view('soccer_ranking')
@monitor_handling
def i_show_soccer_table(liga):
    try:
        data = soccer_table.get_table_data(liga)  # a list of dictionaries (each club one dictionary)
        return dict(liga=liga, table=data)
    except Exception as e:
        logger.error(str(e))


@route('/i_currentSolar')
@monitor_handling
def i_show_current_solar():
    try:
        data = current_solar.get_solar_data()  # a dictionary of solar data
        if data:
            return template('current_solar', solar=data)
        else:
            return template('error_solar')
    except Exception as e:
        logger.error(str(e))


@route('/i_currentTime')
@view('current_time')
@monitor_handling
def i_show_current_time():
    return None


@route('/i_soccerMatches/<liga>')
@view('soccer_matches')
@monitor_handling
def i_show_soccer_matches(liga):
    try:
        data = soccer_table.get_match_data(liga)  # a list of dictionaries (each match one dictionary)
        return dict(liga=liga, matches=data)
    except Exception as e:
        logger.error(str(e))


@route('/i_picOfTheDay')
@view('pic_of_the_day')
@monitor_handling
def i_show_pic_of_the_day():
    try:
        ret_data = pic_of_the_day.get_pic_url()  # returns a dictionary with picture url and text
        return dict(data=ret_data)
    except Exception as e:
        logger.error(str(e))


@route('/i_display_camera/<cam>')
@view('display_camera')
@monitor_handling
def i_display_camera(cam):
    try:
        ret_data = camera.get_camera_data(cam)
        return dict(data=ret_data)
    except Exception as e:
        logger.error(str(e))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'devmode':
        run(server='cheroot', host='localhost', port=8080, debug=True, reloader=True)
    else:
        run(server='cheroot', host='0.0.0.0', port=8080, debug=False, reloader=False)
