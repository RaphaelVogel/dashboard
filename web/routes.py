from bottle import route, static_file, request, HTTPResponse
from access_modules import iceweasel, monitor

fake = False

@route('/')
def index():
    return static_file('index.html', root='./ha2/web')

@route('/haui/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./ha2/web/haui')


@route('/ui5lib/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./ha2/web/ui5lib')


@route('/pages/<filepath:path>')
def serve_static(filepath):
    return static_file(filepath, root='./ha2/web/pages')


# Solar inverter API
# -------------------------------------------------------------------
@route('/solar/current')
def current_solarproduction():
    current_data = ""
    if current_data:
        return current_data
    else:
        return HTTPResponse(dict(error="Could not read solar production values"), status=500)
