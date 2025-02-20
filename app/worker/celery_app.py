import os

from celery import Celery

celery_app = None


if os.getenv('DOCKER') is not None: # if running example without docker
    celery_app = Celery(
        "worker",
        backend="redis://:password@localhost:6379/0",
        broker="amqp://user:bitnami@localhost:5672//"
    )
    celery_app.conf.task_routes = {
        "app.worker.celery_worker.test_celery": "test-queue"}
else:  # running example with docker
    celery_app = Celery(
        "worker",
        backend="redis://:password@127.0.0.1:6379/0",
        broker="amqp://guest:guest@127.0.0.1:5672//"
    )
    celery_app.conf.task_routes = {
        "app.worker.celery_worker.test_celery": "test-queue"}

celery_app.conf.update(task_track_started=True)
