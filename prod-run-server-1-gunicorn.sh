#bin/bash

cd /code && \
gunicorn -b 0.0.0.0:81 otmp.wsgi:application --daemon