from invoke import task


@task
def test(c):
    c.run('PYTHONPATH=. python tests/integration.py')


@task
def start(c):
    c.run('PYTHONPATH=. python warehouse/app.py', pty=True)
