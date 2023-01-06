#!/bin/bash

cat .env

docker-compose up -d --build wkhtmltopdf
docker-compose up -d --build redis
docker-compose up -d --build db

cd JrachkaTop && python3 manage.py migrate && python3 manage.py loaddata data
#gunicorn JrachkaTop.wsgi &
python -m celery -A JrachkaTop worker
