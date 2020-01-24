#!/bin/bash
set -e

exec gunicorn --chdir /code currency.wsgi --log-level debug --access-logfile /logs/gunicorn-access.log --error-logfile /logs/gunicorn-error.log -b 0.0.0.0:8000
# python manage.py runserver 0.0.0.0:8000