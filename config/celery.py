import os

import configurations
from celery import Celery
from celery.schedules import crontab
from decouple import config

# from layouts.tasks import create_instances_according_date
# set the default Django settings_old module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      config('DJANGO_SETTINGS_MODULE', cast=str))
os.environ.setdefault('DJANGO_CONFIGURATION',
                      config('DJANGO_CONFIGURATION', cast=str))
configurations.setup()

app = Celery('config')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
