import pytest
from pytest import fail

from lib import stock, task_actions
from lib.stock import StockAllocationError
from lib.tasks import Task


def test_fail_on_unknown_product():
    with pytest.raises(StockAllocationError):
        stock.allocate_items(['kuku'])


def test_decreasing_stock_clear_allocations():
    stock.allocate_items(['Salt'] * 10)
    stock.dec('Salt')
    stock.inc('Salt')
    try:
        stock.allocate_items(['Salt'] * 1)
    except StockAllocationError:
        fail()


def test_increase_stock_on_product_insert():
    task_actions.on_task_complete(Task(action=Task.DROP, product='Salt'))
    assert stock.all()['Salt'] == 11
