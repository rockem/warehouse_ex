from lib import tasks
from lib.tasks import Task


def test_should_not_retrieve_in_progress_tasks():
    tasks.add_all([Task(action=Task.MOVE, product='Milk')])
    assert len(tasks.next_tasks()) == 1
    assert len(tasks.next_tasks()) == 0


