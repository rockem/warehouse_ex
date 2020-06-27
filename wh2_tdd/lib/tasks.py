import random

_tasks_repository = []


class Task:
    DROP = 'drop'
    PICK = 'pick'
    MOVE = 'move'

    PENDING = 'status'
    IN_PROGRESS = 'in_progress'

    def __init__(self, action, product=None, destination=None):
        self.id = str(random.getrandbits(64))
        self.action = action
        self.product = product
        self.destination = destination
        self.status = Task.PENDING


def add_all(tasks):
    _tasks_repository.extend(tasks)


def next_tasks():
    pending_tasks = [t for t in _tasks_repository if t.status == Task.PENDING]
    for t in pending_tasks:
        t.status = Task.IN_PROGRESS
    return pending_tasks


def get(id):
    return next(t for t in _tasks_repository if t.id == id)
