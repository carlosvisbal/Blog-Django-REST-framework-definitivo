#!/bin/bash
# Make migrations and migrate
python manage.py makemigrations --no-input
mkmg_status=$?
if [ $mkmg_status -ne 0 ]
then
  exit $mkmg_status
fi
python manage.py migrate --no-input
# Collect static files
python manage.py collectstatic --no-input
# uWSGI server
# Daphne server
uwsgi -y server.yaml