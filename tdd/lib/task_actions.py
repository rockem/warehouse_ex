from lib import stock
from lib.tasks import Task


def on_task_complete(task):
    if task.product:
        if task.action == Task.PICK:
            stock.dec(task.product)
        else:
            stock.inc(task.product)
