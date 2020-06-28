from lib.orders import Order
from lib.tasks import Task

_stock_layout = {
    'Bread': (5, 6),
    'Milk': (1, 5),
    'Salt': (6, 5),
    'Soap': (8, 9),
    'Pasta': (9, 2)
}


def _create_order_tasks(items):
    tasks = []
    for i in items:
        tasks.append(Task(action=Task.MOVE, destination=_stock_layout[i]))
        tasks.append(Task(action=Task.PICK, product=i))
    tasks.append(Task(action=Task.MOVE, destination=(0, 0)))
    tasks.append(Task(action=Task.DROP))
    return tasks


def _create_supply_order_tasks(items):
    tasks = []
    for item in items:
        tasks.append(Task(action=Task.MOVE, destination=(0, 0)))
        tasks.append(Task(action=Task.PICK, product=item))
        tasks.append(Task(action=Task.MOVE, destination=_stock_layout[item]))
        tasks.append(Task(action=Task.DROP, product=item))
    return tasks


_tasks_steps = {
    Order.ORDER: _create_order_tasks,
    Order.SUPPLY: _create_supply_order_tasks
}


def create_tasks_for(order):
    return _tasks_steps[order.type](order.items)
