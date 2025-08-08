from __future__ import absolute_import, unicode_literals

import os
from django.conf import settings
from celery.schedules import crontab

from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{cookiecutter.project_name}}.settings')
app = Celery('{{cookiecutter.project_name}}')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)



app.conf.timezone = 'America/Recife'
