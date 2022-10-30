release: sh -c 'python manage.py migrate && python manage.py collectstatic --noinput --clear'
web: gunicorn nutrack.wsgi --log-file -
