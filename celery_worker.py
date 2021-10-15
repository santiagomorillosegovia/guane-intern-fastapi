import os
import time
from celery import Celery

celery = Celery(
    "worker",
    broker="amqp://user:bitnami@rabbitmq:5672//",
    backend="redis://:password123@redis:6379/0"
    
)


@celery.task(name="create_task")
def create_task(a):
    time.sleep(3)
    return "Perro Guardado"