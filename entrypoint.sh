#!/usr/bin/env bash
set -e

PYTHON_INTERPRETER=$(which python3)
APPLICATION_ADDRESS=0.0.0.0
APPLICATION_PORT=8000


function waiting_for_database {
    echo "Waiting for database."
    until PGPASSWORD=$POSTGRES_PASSWORD psql -h "$POSTGRES_HOST_NAME" -U "$POSTGRES_USER" -c '\q'; do
      >&2 echo "Postgres is unavailable - sleeping."
      sleep 1
    done
    >&2 echo "Postgres is up - executing command."

}
function run_migrations {
    echo "Running database migrations."
    $PYTHON_INTERPRETER manage.py migrate --noinput
}

function collect_static {
    echo "Collecting application static files."
    $PYTHON_INTERPRETER manage.py collectstatic --noinput
}
function run_tests {
    echo "Running tests."
    $PYTHON_INTERPRETER manage.py test
}
function run_dev_server {
    echo "Running application server. ($APPLICATION_ADDRESS:$APPLICATION_PORT)"
    $PYTHON_INTERPRETER manage.py runserver --nothreading $APPLICATION_ADDRESS:$APPLICATION_PORT
}

function main() {
    waiting_for_database
    run_migrations
    collect_static
    run_tests
    run_dev_server
}

main