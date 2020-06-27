ITEMS = {
    'Bread': 10,
    'Milk': 10,
    'Salt': 10,
    'Soap': 10,
    'Pasta': 10
}

_allocated_items = {}


def allocate_items(items):
    for i in items:
        _validate_item_exists(i)
        _allocated_items[i] = _allocated_items.get(i, 0) + 1
        if ITEMS[i] - _allocated_items[i] < 0:
            raise StockAllocationError()


def _validate_item_exists(item):
    if not ITEMS.get(item, None):
        raise StockAllocationError('Item not exists')


def all():
    return ITEMS


def dec(item):
    ITEMS[item] -= 1
    _allocated_items[item] = - 1


class StockAllocationError(Exception):
    pass


def inc(item):
    ITEMS[item] += 1
