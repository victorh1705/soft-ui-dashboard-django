#!/bin/bash
# exit on error
set -o errexit

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py collectstatic --no-input
python manage.py migrate

chown python:python build.sh

gunicorn --config gunicorn-cfg.py core.wsgi