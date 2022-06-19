#!/bin/sh

# Wait for DB to be ready
function postgres_ready(){
python3 << END
import os
import sys
import psycopg2


db_host = os.environ.get("DJANGO_DB_HOST")
db_name = os.environ.get("POSTGRES_DB")
db_user = os.environ.get("POSTGRES_USER")
db_password = os.environ.get("POSTGRES_PASSWORD")

try:
    conn = psycopg2.connect(
        dbname=db_name, user=db_user, password=db_password, host=db_host
    )
except psycopg2.OperationalError:
    sys.exit(-1)
sys.exit(0)
END
}

until postgres_ready; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 5
done

# Performing migrations and static collection
echo "Performing DB migrations"
python3 manage.py migrate

if [ $ENVIRONMENT_NAME == "local" ]; then
  echo "Using development server"
  python3 manage.py runserver 0.0.0.0:8000
else
  if [ $ENVIRONMENT_NAME == "production" ]; then
    echo "Using Production Server"
    daphne -p 8001 currency_exchanger.asgi:application
  fi
fi