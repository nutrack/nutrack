release: sh -c 'python manage.py migrate --run-syncdb && python manage.py collectstatic --noinput --clear' && ./manage.py migrate
web: gunicorn nutrack.wsgi --log-file -
