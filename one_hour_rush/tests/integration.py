import subprocess
import sys
from time import sleep

import pytest
import requests

DOMAIN = 'http://localhost:8080'


@pytest.fixture
def app():
    p = subprocess.Popen([sys.executable, 'warehouse/app.py'])
    sleep(1)
    yield
    p.kill()


def test_integration(app):
    _add_order(['Milk', 'Bread'])
    _get_tasks()
    _show_stock()
    _supply(['Milk', 'Milk'])
    _get_tasks()
    _show_stock()


def _add_order(items):
    r = requests.post(f"{DOMAIN}/orders", json=items)
    assert r.status_code == 201


def _get_tasks():
    print('Tasks ===============>')
    r = requests.get(f"{DOMAIN}/tasks")
    assert r.status_code == 200
    for t in r.json():
        print(t)
        print('--')
        _complete_tasks(t)


def _complete_tasks(t):
    r = requests.put(f"{DOMAIN}/tasks/{t['id']}/complete")
    assert r.status_code == 200


def _show_stock():
    print('Stock ===============>')
    r = requests.get(f"{DOMAIN}/stock")
    assert r.status_code == 200
    print(r.json())


def _supply(items):
    r = requests.post(f"{DOMAIN}/supply", json=items)
