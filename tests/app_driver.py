import subprocess

import requests
from busypie import wait


class AppError(Exception):
    BAD_REQUEST = 400

    def __init__(self, error_code):
        self.reason = error_code


class AppDriver:

    def __init__(self):
        self.app_p = None

    def start(self):
        self.app_p = subprocess.Popen(['python', 'lib/app.py'])
        wait().ignore_exceptions().until(self._app_is_up)

    def _app_is_up(self):
        return requests.get('http://localhost:8080/health').status_code == 200

    def create_order_with(self, items):
        resp = requests.post('http://localhost:8080/orders', json=items)
        self.assert_response_status(resp, 201)

    def assert_response_status(self, resp, expected_status):
        if resp.status_code != expected_status:
            raise AppError(resp.status_code)

    def stop(self):
        self.app_p.kill()
