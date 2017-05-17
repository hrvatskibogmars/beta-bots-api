web: newrelic-admin run-program gunicorn --pythonpath="$PWD/betabots" wsgi:application
worker: python betabots/manage.py rqworker default