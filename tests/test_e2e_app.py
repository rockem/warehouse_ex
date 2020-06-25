import pytest

from tests.app_driver import AppDriver, AppError


@pytest.fixture
def app():
    app = AppDriver()
    app.start()
    yield app
    app.stop()


def test_fail_to_create_order_due_to_stock_shortage(app):
    with pytest.raises(AppError) as e:
        app.create_order_with(['Bread'] * 11)
    assert e.value.reason == AppError.BAD_REQUEST
