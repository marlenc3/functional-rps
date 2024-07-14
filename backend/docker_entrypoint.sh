#!/bin/bash
set -e

export APP_MODULE=main:app
export GUNICORN_CONF=./gunicorn_conf.py
export WORKER_CLASS=uvicorn.workers.UvicornWorker


if [ "$1" = 'gunicorn' ]; then
    ${command_prefix} gunicorn -k "$WORKER_CLASS" -c "$GUNICORN_CONF" "$APP_MODULE"
elif [ "$1" = 'uvicorn' ]; then
    ${command_prefix} uvicorn --host 0.0.0.0 --port 8002 --workers ${UVICORN_WORKERS:-2} --reload "$APP_MODULE"
else
    exec "$@"
fi

