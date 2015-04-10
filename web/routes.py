from bottle import route, static_file, request, HTTPResponse, view, template
from access_modules import iceweasel, monitor, soccer_table, current_weather, current_solar, pic_of_the_day, ebay


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


@route('/currentSolar')
def show_current_solar():
    data = current_solar.get_solar_data()  # a dictionary of solar data
    if data:
        return template('current_solar', solar=data)
    else:
        return template('error_solar')


@route('/currentTime')
@view('current_time')
def show_current_time():
    return None


@route('/soccerMatches/<liga>')
@view('soccer_matches')
def show_soccer_matches(liga):
    data = soccer_table.get_match_data(liga)  # a list of dictionaries (each match one dictionary)
    return dict(liga=liga, matches=data)


@route('/picOfTheDay')
@view('pic_of_the_day')
def show_pic_of_the_day():
    ret_data = pic_of_the_day.get_pic_url()  # returns a dictionary with picture url and text
    return dict(data=ret_data)


@route('/ebay')
@view('ebay')
def show_ebay():
    ret_data = ebay.get_data()  # returns a list of dictionaries
    return dict(offers=ret_data)