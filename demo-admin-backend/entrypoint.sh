#!/bin/sh

echo "Waiting for database..."

while ! nc -z $DB_HOST $DB_PORT; do
  sleep 0.1
done

echo "database started"

gunicorn --workers=2 --threads=4 --worker-class=gthread -b \
  $API_SERVER_HOST:$API_SERVER_PORT wsgi:flask_app

