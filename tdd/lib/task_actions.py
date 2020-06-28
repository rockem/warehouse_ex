from lib import stock
from lib.tasks import Task

_current_location = None


def on_task_complete(task):
    _update_location_from(task)
    if _current_location != (0, 0) and task.product:
        if task.action == Task.PICK:
            stock.dec(task.product)
        else:
            stock.inc(task.product)


def _update_location_from(task):
    global _current_location
    if task.destination:
        _current_location = task.destination
