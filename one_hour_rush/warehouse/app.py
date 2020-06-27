import json

import bottle
from bottle import run, post, request, get, put, response

from warehouse import tasks, stock
from warehouse.layout import get_item_location
from warehouse.tasks import Task, MOVE, DROP, PICK


@post('/orders')
def new_order():
    tasks.add_tasks(create_tasks_for_order(json.loads(request.body.read())))
    response.status = 201


def create_tasks_for_order(order_items):
    tasks = []
    for oi in order_items:
        tasks.append(Task(MOVE, destination=get_item_location(oi)))
        tasks.append(Task(PICK, product=oi))
    tasks.append(Task(MOVE, destination=(0, 0)))
    tasks.append(Task(DROP))
    return tasks


# ========================
@get('/tasks')
def get_pending_tasks():
    return json.dumps([t.to_json() for t in tasks.all()])


@put('/tasks/<id>/complete')
def task_completed(id):
    task = tasks.get_by_id(id)
    if task.action is PICK and task.product:
        stock.dec(task.product)
    elif task.action is DROP and task.product:
        stock.inc(task.product)
    tasks.remove(id)


# ========================
@get('/stock')
def get_stock():
    return json.dumps(stock.all())


# ========================
@post('/supply')
def new_order():
    tasks.add_tasks(create_tasks_for_supply_order(json.loads(request.body.read())))


def create_tasks_for_supply_order(order_items):
    tasks = []
    for oi in order_items:
        tasks.append(Task(PICK))
        tasks.append(Task(MOVE, get_item_location(oi)))
        tasks.append(Task(DROP, product=oi))
        tasks.append(Task(MOVE, (0, 0)))
    return tasks


bottle.response.default_content_type = 'application/json'
run(host='localhost', port=8080, debug=True)
