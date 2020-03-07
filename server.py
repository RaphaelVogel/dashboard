import sys
from pathlib import Path
from threading import Timer
from bottle import (
    run,
    route,
    static_file,
    HTTPResponse,
    view,
    TEMPLATE_PATH,
    template,
)
from access_modules import (
    chromium,
    monitor,
    soccer_table,
    pic_of_the_day,
    camera,
    solar,
    cfg,
)


current_dir = Path(__file__).resolve().parent
# bottle initialization
TEMPLATE_PATH.append(Path(current_dir, 'web/views'))


# decorator to control monitor
def monitor_handling(func):
    def wrapper(*args, **kwargs):
        status = monitor.status()
        if status is monitor.Status.OFF:
            monitor.switch_on()
        else:
            monitor.reset_timer()
        return func(*args, **kwargs)

    return wrapper


# decorator to quit camera if running
def quit_rtsp_stream(func):
    def wrapper(*args, **kwargs):
        camera.quit_rtsp_stream()
        return func(*args, **kwargs)

    return wrapper


# --- Base routes ----------------------------------------------------------------------------------------------------
@route('/')
def index():
    return static_file('index.html', root=Path(current_dir, 'web'))


@route('/lib/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root=Path(current_dir, 'web/lib'))


# ---------------------------------------------------------------------------------------------------------
# --- Command/public routes ---
# ---------------------------------------------------------------------------------------------------------
@route('/monitor/<status>')
def switch_monitor(status):
    if status == monitor.Status.ON.value:
        monitor.switch_on()
    elif status == monitor.Status.OFF.value:
        monitor.switch_off()
    else:
        return HTTPResponse(dict(error="Wrong url to switch monitor, use ON or OFF"), status=500)

    return dict(status="OK")


@route('/soccerTable/<liga>')
def show_soccer_table(liga):
    chromium.open_url("localhost:8080/i_soccerTable/" + liga)
    return dict(status="OK")


@route('/currentWeather')
def show_current_weather():
    chromium.open_url("localhost:8080/i_currentWeather")
    return dict(status="OK")


@route('/currentSolar')
def show_current_solar():
    chromium.open_url("localhost:8080/i_currentSolar")
    return dict(status="OK")


@route('/currentTime')
def show_current_time():
    chromium.open_url("localhost:8080/i_currentTime")
    return dict(status="OK")


@route('/soccerMatches/<liga>')
def show_soccer_matches(liga):
    chromium.open_url("localhost:8080/i_soccerMatches/" + liga)
    return dict(status="OK")


@route('/picOfTheDay')
def show_pic_of_the_day():
    chromium.open_url("localhost:8080/i_picOfTheDay")
    return dict(status="OK")


@route('/displayCamera/<cam>')
def display_camera(cam):
    if cam == 2:
        # mjpeg stream camera
        chromium.open_url("localhost:8080/i_display_mjpeg_camera/" + cam)
    else:
        # rtsp stream camera
        chromium.open_url("localhost:8080/i_display_rtsp_camera/" + cam)
    return dict(status="OK")


@route('/showURL/<url_id>')
def showURL(url_id):
    chromium.open_url("localhost:8080/i_show_url/" + url_id)
    return dict(status="OK")


# ---------------------------------------------------------------------------------------------------------
# --- Web/Button pressed routes ---
# ---------------------------------------------------------------------------------------------------------
@route('/i_soccerTable/<liga>')
@view('soccer_ranking')
@monitor_handling
@quit_rtsp_stream
def i_show_soccer_table(liga):
    data = soccer_table.get_table_data(liga)  # a list of dictionaries (each club one dictionary)
    return dict(liga=liga, table=data)


@route('/i_currentSolar')
@view('current_solar')
@monitor_handling
@quit_rtsp_stream
def i_show_current_solar():
    data = solar.read_data()  # a dictionary of solar data
    if data:
        return template('current_solar', solar=data)
    else:
        return template('error_solar')


@route('/i_currentTime')
@view('current_time')
@monitor_handling
@quit_rtsp_stream
def i_show_current_time():
    return None


@route('/i_soccerMatches/<liga>')
@view('soccer_matches')
@monitor_handling
@quit_rtsp_stream
def i_show_soccer_matches(liga):
    data = soccer_table.get_match_data(liga)  # a list of dictionaries (each match one dictionary)
    return dict(liga=liga, matches=data)


@route('/i_picOfTheDay')
@view('pic_of_the_day')
@monitor_handling
@quit_rtsp_stream
def i_show_pic_of_the_day():
    ret_data = pic_of_the_day.get_pic_url()  # returns a dictionary with picture url and text
    return dict(data=ret_data)


@route('/i_display_rtsp_camera/<cam>')
@monitor_handling
def i_display_rtsp_camera(cam):
    camera.display_rtsp_stream(cam)


@route('/i_display_mjpeg_camera/<cam>')
@monitor_handling
@quit_rtsp_stream
def i_display_mjpeg_camera(cam):
    camera.display_mjpeg_stream(cam)


@route('/i_show_url/<url_id>')
@monitor_handling
@quit_rtsp_stream
def i_show_url(url_id):
    url_to_open = cfg['show_url'][url_id]
    chromium.open_url(url_to_open)


if __name__ == '__main__':
    Timer(15.0, switch_monitor(monitor.Status.OFF.value)).start()  # initially switch off monitor
    if len(sys.argv) > 1 and sys.argv[1] == 'devmode':
        run(server='cheroot', host='localhost', port=8080, debug=True, reloader=True)
    else:
        run(server='cheroot', host='0.0.0.0', port=8080, debug=False, reloader=False)
