from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_init.settings')

app = Celery('celery_init',)
app.conf.enable_utc = False
app.config_from_object('django.conf:settings')



app.conf.beat_schedule = {
    'every-10-seconds': {
        'task': 'init_app.tasks.test',
        # 'schedule': 10, every 10 seconds
        'schedule': crontab(minute="*/1"),  # Adjust the time as per your requirement
        'args': ('Damn', ),
    },
}


app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')