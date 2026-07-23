from bottle import run, route, template, view, static_file

@route('/')
def h():
    return template('home.tpl')

@route('/about')
def ab():
    return template('about.tpl')

@route('/contact')
def c():
    return template('contact.tpl')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

run(host='localhost', port=8080, debug=True, reloader=True)