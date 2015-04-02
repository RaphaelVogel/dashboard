from bottle import route, static_file, request, HTTPResponse, view
from access_modules import iceweasel, monitor, soccer_table


# --- Base routes ----------------------------------------------------------------------------------------------------
@route('/')
def index():
    return static_file('index.html', root='./web')


@route('/lib/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./web/lib')


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
