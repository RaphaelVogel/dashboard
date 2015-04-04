from bottle import route, static_file, request, HTTPResponse, view
from access_modules import iceweasel, monitor, soccer_table, current_weather


# --- Base routes ----------------------------------------------------------------------------------------------------
@route('/')
def index():
    return static_file('index.html', root='./dashboard/web')


@route('/lib/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./dashboard/web/lib')


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
    iceweasel.open_url(url)
    return dict(status="OK")


# --- Button pressed routes ------------------------------------------------------------------------------------------
@route('/soccerTable/<liga>')
@view('soccer_ranking')
def show_soccer_table(liga):
    data = soccer_table.get_table_data(liga)  # a list of dictionaries (each club one dictionary)
    return dict(liga=liga, table=data)


@route('/currentWeather')
@view('current_weather')
def show_current_weather():
    data = current_weather.get_weather_data()  # a dictionary of weather data
    return dict(weather=data)