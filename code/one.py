from time import sleep
from celery import Celery

# Configure the Celery app to use RabbitMQ
app = Celery(
    main='name_app',
    broker='pyamqp://bob:bob@localhost//'
)

# Set the broker_connection_retry_on_startup to True
app.conf.broker_connection_retry_on_startup = True

@app.task
def add(x, y):
    sleep(5)
    return (x+y)