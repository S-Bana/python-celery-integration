from time import sleep
from celery import Celery

app = Celery(
    main='name_app',
    backend='rpc://',
    broker='pyamqp://bob:bob@localhost//',
)

# Configure the Celery app to use RabbitMQ

# in one line for each config
# app.conf.broker_connection_retry_on_startup = True
# app.conf.timezone = 'Asia/Tehran'

# or in multi line for some config
# app.conf.update(
#     broker_connection_retry_on_startup = True,
#     timezone = 'Asia/Tehran',
# )

# or read config from files
app.config_from_object('conf_three')

@app.task
def add(x, y):
    sleep(5)
    return (x+y)
