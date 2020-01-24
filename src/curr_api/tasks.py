from __future__ import absolute_import, unicode_literals

from celery.task import periodic_task
from celery.schedules import crontab

from curr_api.utils import fixer_request


@periodic_task(run_every=(crontab(minute=0, hour=0)), name="fixer_request_task")
def fixer_request_task():
    fixer_request()
