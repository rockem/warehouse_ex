import json

from bottle import run, get, post, response


@get('/health')
def health():
    return json.dumps({'status': 'UP'})


@post('/orders')
def create_order():
    response.status = 400


run(host='localhost', port=8080, debug=True)
