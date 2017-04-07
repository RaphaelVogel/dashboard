from bottle import route, static_file, HTTPResponse, view, template
from access_modules import iceweasel, monitor, soccer_table, current_weather, current_solar, pic_of_the_day, alarmstatus, camera
import logging

logger = logging.getLogger("server_logger")


# --- Base routes ----------------------------------------------------------------------------------------------------
@route('/')
def index():
    return static_file('index.html', root='./dashboard/web')


@route('/lib/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./dashboard/web/lib')


# ---------------------------------------------------------------------------------------------------------
# --- Public routes ---
# ---------------------------------------------------------------------------------------------------------
@route('/monitor/<status>')
def switch_monitor(status):
    if status == "ON":
        monitor.switch_on()
    elif status == "OFF":
        monitor.switch_off()
    else:
        return HTTPResponse(dict(error="Wrong url to switch monitor, use ON or OFF"), status=500)

    return dict(status="OK")


@route('/setURL/<url>')
def set_url(url):
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url(url)
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/soccerTable/<liga>')
def show_soccer_table(liga):
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/i_soccerTable/" + liga)
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/currentWeather')
def show_current_weather():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/i_currentWeather")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/currentSolar')
def show_current_solar():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/i_currentSolar")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/currentTime')
def show_current_time():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/i_currentTime")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/soccerMatches/<liga>')
def show_soccer_matches(liga):
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/i_soccerMatches/" + liga)
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/picOfTheDay')
def show_pic_of_the_day():
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/i_picOfTheDay")
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/displayCamera/<cam>')
def display_camera(cam):
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/i_display_camera/" + cam)
    if not monitor.TIMER_RUNNING:
        monitor.start_timer()
    return dict(status="OK")


@route('/alarmMessage/<sensor_type>/<alarm_location>')
def alarm_message(sensor_type, alarm_location):
    status = monitor.status()
    if status == "OFF":
        monitor.switch_on()
    iceweasel.open_url("localhost:8080/i_alarmMessage/" + sensor_type + "/" + alarm_location)
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


@route('/i_currentWeather')
@view('current_weather')
def i_show_current_weather():
    try:
        data = current_weather.get_weather_data()  # a dictionary of weather data
        return dict(weather=data)
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


@route('/i_alarmMessage/<sensor_type>/<alarm_location>')
@view('alarm_message')
def i_alarm_message(sensor_type, alarm_location):
    try:
        return dict(sensor_type=sensor_type, alarm_location=alarm_location)
    except Exception as e:
        logger.error(str(e))


@route('/i_alarm_status')
@view('alarm_status')
def i_alarm_status():
    try:
        alarm_logs = alarmstatus.get_alarm_logs()  # returns a dictionary with alarm log messages
        message_list = alarm_logs['alarm_logs']
        alarm_status = alarmstatus.get_alarm_status()
        return dict(alarmlogs=message_list, alarmstatus=alarm_status['status'])
    except Exception as e:
        logger.error(str(e))