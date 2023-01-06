#!/bin/bash

cat .env

docker-compose up -d --build wkhtmltopdf
docker-compose up -d --build redis
docker-compose up -d --build db

cd JrachkaTop && python -m celery -A JrachkaTop worker
