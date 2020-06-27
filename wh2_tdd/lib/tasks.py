import random

_tasks_repository = []


class Task:
    DROP = 'drop'
    PICK = 'pick'
    MOVE = 'move'

    def __init__(self, action, product=None, destination=None):
        self.id = str(random.getrandbits(64))
        self.action = action
        self.product = product
        self.destination = destination


def add_all(tasks):
    _tasks_repository.extend(tasks)


def next_tasks():
    return _tasks_repository


def get(id):
    return next(t for t in _tasks_repository if t.id == id)
