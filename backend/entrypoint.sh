#!/bin/bash
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser --noinput --email admin@example.com --surname Agasyan --name Artem --patronymic Armenovich

exec python manage.py runserver 0.0.0.0:8000
