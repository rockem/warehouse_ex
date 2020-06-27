_orders = []


class Order:
    SUPPLY = 'supply'
    ORDER = 'order'

    def __init__(self, type, items):
        self.type = type
        self.items = items


def add_order(order_items):
    _orders.append(Order(Order.ORDER, order_items))


def get_orders():
    return _orders


def add_supply(order_items):
    _orders.append(Order(Order.SUPPLY, order_items))
