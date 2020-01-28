import sys
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

TEMPLATE_PATH.insert(0, './web/views')


# --- Base routes ----------------------------------------------------------------------------------------------------
@route('/')
def index():
    return static_file('index.html', root='./web')


@route('/lib/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./web/lib')


# ---------------------------------------------------------------------------------------------------------
# --- Public routes ---
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
def set_url(url):
    status = monitor.status()
    if status == monitor.Status.OFF:
        monitor.switch_on()
    chromium.open_url(url)
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/soccerTable/<liga>')
def show_soccer_table(liga):
    status = monitor.status()
    if status == monitor.Status.OFF:
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_soccerTable/" + liga)
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/currentWeather')
def show_current_weather():
    status = monitor.status()
    if status == monitor.Status.OFF:
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_currentWeather")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/currentSolar')
def show_current_solar():
    status = monitor.status()
    if status == monitor.Status.OFF:
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_currentSolar")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/currentTime')
def show_current_time():
    status = monitor.status()
    if status == monitor.Status.OFF:
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_currentTime")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/soccerMatches/<liga>')
def show_soccer_matches(liga):
    status = monitor.status()
    if status == monitor.Status.OFF:
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_soccerMatches/" + liga)
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/picOfTheDay')
def show_pic_of_the_day():
    status = monitor.status()
    if status == monitor.Status.OFF:
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_picOfTheDay")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/displayCamera/<cam>')
def display_camera(cam):
    status = monitor.status()
    if status == monitor.Status.OFF:
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_display_camera/" + cam)
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/alarmMessage/<sensor_type>/<alarm_location>')
def alarm_message(sensor_type, alarm_location):
    status = monitor.status()
    if status == monitor.Status.OFF:
        monitor.switch_on()
    chromium.open_url("localhost:8080/i_alarmMessage/" + sensor_type + "/" + alarm_location)
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


# ---------------------------------------------------------------------------------------------------------
# --- Button pressed routes / private routes ---
# ---------------------------------------------------------------------------------------------------------
@route('/i_soccerTable/<liga>')
@view('soccer_ranking')
def i_show_soccer_table(liga):
    try:
        data = soccer_table.get_table_data(liga)  # a list of dictionaries (each club one dictionary)
        return dict(liga=liga, table=data)
    except Exception as e:
        logger.error(str(e))


@route('/i_currentSolar')
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
def i_show_current_time():
    return None


@route('/i_soccerMatches/<liga>')
@view('soccer_matches')
def i_show_soccer_matches(liga):
    try:
        data = soccer_table.get_match_data(liga)  # a list of dictionaries (each match one dictionary)
        return dict(liga=liga, matches=data)
    except Exception as e:
        logger.error(str(e))


@route('/i_picOfTheDay')
@view('pic_of_the_day')
def i_show_pic_of_the_day():
    try:
        ret_data = pic_of_the_day.get_pic_url()  # returns a dictionary with picture url and text
        return dict(data=ret_data)
    except Exception as e:
        logger.error(str(e))


@route('/i_display_camera/<cam>')
@view('display_camera')
def i_display_camera(cam):
    try:
        ret_data = camera.get_camera_data(cam)
        return dict(data=ret_data)
    except Exception as e:
        logger.error(str(e))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'devmode':
        run(host='localhost', port=8080, debug=True, reloader=True)
    else:
        run(host='0.0.0.0', port=8080, debug=False, reloader=False)
