0. Run RabbitMq in docker
#
docker run -d \
--hostname my-rabbit \
--name some-rabbit \
-e RABBITMQ_DEFAULT_USER=bob \
-e RABBITMQ_DEFAULT_PASS=bob \
-p 5672:5672 \
-p 15672:15672 \
rabbitmq:3-management

------------------------------------------------------------------------------
1. Define Your code
# 
from celery import Celery

app = Celery(
    main='tasks',
    broker='pyamqp://bob:bob@localhost//'
)

@app.task
def add(x, y):
    return x + y

------------------------------------------------------------------------------
2. Testing Your code
You can test your setup by calling a task from a Python shell or script:
#
from one import add

result = add.delay(4, 6)
print(result.get(timeout=10))  # Should print 10 if everything works correctly

------------------------------------------------------------------------------
3. Handling Warnings
To address the warnings about connection retries, you can update your Celery configuration:
#
from celery import Celery

app = Celery(
    main='tasks',
    broker='pyamqp://bob:bob@localhost//'
)

app.conf.broker_connection_retry_on_startup = True

@app.task
def add(x, y):
    return x + y

------------------------------------------------------------------------------
4. Monitoring Tasks
If you want to monitor tasks, you can enable task events by adding the -E flag when starting the worker:
#
terminal :
celery -A one.app worker
# or
celery -A one.app worker -E
# or
celery -A one.app worker --loglevel=INFO -E

------------------------------------------------------------------------------
5. Create a module to use file one
run_one.py
#
from one import add

add.apply_async(args=[5, 8])

------------------------------------------------------------------------------
6. run it in terminal
#
python3 run_one.py