import random

MOVE = 'move'
PICK = 'pick'
DROP = 'drop'

PENDING = 'pending'
IN_PROGRESS = 'IN_PROGRESS'

tasks = []


def add_tasks(new_tasks):
    for t in new_tasks:
        tasks.append(t)


class Task:
    def __init__(self, action, product=None, destination=None):
        self.id = str(random.getrandbits(128))
        self.action = action
        self.destination = destination
        self.product = product
        self.status = PENDING

    def to_json(self):
        return self.__dict__


def all():
    pending_tasks = [t for t in tasks if t.status is PENDING]
    _activate_tasks([t for t in pending_tasks])
    return pending_tasks


def _activate_tasks(tasks):
    for t in tasks:
        t.status = IN_PROGRESS


def remove(id):
    tasks.remove(get_by_id(id))


def get_by_id(id):
    return next((t for t in tasks if t.id == id), None)
