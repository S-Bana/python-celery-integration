from time import sleep
from celery import Celery
from celery import signature


# Configure the Celery app to use RabbitMQ
app = Celery(
    main='name_app',
    backend='rpc://',
    broker='pyamqp://bob:bob@localhost//'
)

# Set the broker_connection_retry_on_startup to True
app.conf.broker_connection_retry_on_startup = True

@app.task
def add(x, y):
    sleep(5)
    return (x+y)


result = add.signature(args=(3, 4))
print(result.delay())