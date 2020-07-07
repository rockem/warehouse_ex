from invoke import task


@task
def test(c):
    c.run('PYTHONPATH=. pytest tests', pty=True)


@task
def start(c):
    c.run('PYTHONPATH=. python lib/app.py', pty=True)
