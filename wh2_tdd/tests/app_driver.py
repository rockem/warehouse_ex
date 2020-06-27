import subprocess

import requests
from busypie import wait, ConditionTimeoutError


class AppError(Exception):
    BAD_REQUEST = 400

    def __init__(self, error_code):
        self.reason = error_code


class AppDriver:

    def __init__(self, domain):
        self._domain = domain
        self._app_p = None

    def start(self):
        self._app_p = subprocess.Popen(['python', 'lib/app.py'])
        try:
            wait().ignore_exceptions().until(self._app_is_up)
        except ConditionTimeoutError as e:
            self.stop()
            raise e

    def _app_is_up(self):
        return requests.get(f'{self._domain}/health').status_code == 200

    def create_order_for(self, items):
        resp = requests.post(f'{self._domain}/orders', json=items)
        self._assert_response_status(resp, 201)

    def _assert_response_status(self, resp, expected_status):
        if resp.status_code != expected_status:
            raise AppError(resp.status_code)

    def next_tasks_contains(self, *expected_tasks):
        for idx, task in enumerate(self._get_next_tasks()):
            assert expected_tasks[idx].items() <= task.items()

    def _get_next_tasks(self):
        resp = requests.get(f'{self._domain}/next-tasks')
        self._assert_response_status(resp, 200)
        return resp.json()

    def quantity_of(self, product):
        resp = requests.get(f'{self._domain}/stock')
        self._assert_response_status(resp, 200)
        return resp.json()[product]

    def complete_all_tasks(self):
        tasks = self._get_next_tasks()
        for t in tasks:
            resp = requests.put(f'{self._domain}/tasks/{t["id"]}/complete')
            self._assert_response_status(resp, 200)

    def create_supply_order_for(self, items):
        resp = requests.post(f'{self._domain}/supply', json=items)
        self._assert_response_status(resp, 201)

    def stop(self):
        self._app_p.kill()
