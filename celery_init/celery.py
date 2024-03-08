from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_init.settings')

app = Celery('celery_init')
app.conf.enable_utc = False
app.config_from_object(settings, namespace='CELERY')


app.conf.beat_scheduler = {
    'every-10-seconds': {
        'task': 'init_app.tasks.test',
        'schedule': crontab(minute=1),  # Adjust the time as per your requirement
        'args': (['Damn',]),
    },
}


app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')