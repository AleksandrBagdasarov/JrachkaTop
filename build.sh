#!/bin/bash

cat .env

docker-compose up -d --build db
