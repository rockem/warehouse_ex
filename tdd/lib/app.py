import json

from bottle import run, get, post, request, abort, response, put

from lib import stock, orders, task_factory, tasks, task_actions
from lib.stock import StockAllocationError


@get('/health')
def health():
    return json.dumps({'status': 'UP'})


@post('/orders')
def create_order():
    order_items = _request_body()
    _allocate_stock_for(order_items)
    orders.add_order(order_items)
    response.status = 201


def _request_body():
    return json.loads(request.body.read())


def _allocate_stock_for(order_items):
    try:
        stock.allocate_items(order_items)
    except StockAllocationError:
        abort(code=400, text='stock allocation error')


@post('/supply')
def create_supply():
    order_items = _request_body()
    orders.add_supply(order_items)
    response.status = 201


@get('/next-tasks')
def get_next_tasks():
    while True:
        order = orders.get_next_order()
        if not order:
            break
        tasks.add_all(task_factory.create_tasks_for(order))
    response.content_type = 'application/json'
    return json.dumps([t.__dict__ for t in tasks.next_tasks()])


@put('/tasks/<id>/complete')
def complete_task(id):
    task_actions.on_task_complete(tasks.get(id))


@get('/stock')
def get_stock():
    response.content_type = 'application/json'
    return json.dumps(stock.all())


run(host='localhost', port=8080, debug=True)
