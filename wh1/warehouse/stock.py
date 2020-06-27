ITEMS = {
    'Milk': 10,
    'Bread': 10,
    'Salt': 10,
    'Soap': 10,
    'Pasta': 10,
}


def dec(product):
    ITEMS[product] = ITEMS[product] - 1


def inc(product):
    ITEMS[product] = ITEMS[product] + 1


def all():
    return [{'name': key, 'amount': value} for key, value in ITEMS.items()]
