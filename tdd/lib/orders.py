import queue
from queue import Empty

_orders = queue.Queue(maxsize=20)


class Order:
    SUPPLY = 'supply'
    ORDER = 'order'

    def __init__(self, type, items):
        self.type = type
        self.items = items


def add_order(order_items):
    _orders.put(Order(Order.ORDER, order_items))


def get_next_order():
    try:
        return _orders.get(block=False)
    except Empty:
        return None


def add_supply(order_items):
    _orders.put(Order(Order.SUPPLY, order_items))
