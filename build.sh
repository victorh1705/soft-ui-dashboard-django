#!/bin/bash
# exit on error
set -o errexit

#python -m pip install --upgrade pip
#
#pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

chown python:python .env
chown python:python /home/python/app/.env

gunicorn --config gunicorn-cfg.py core.wsgi