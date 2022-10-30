release: sh -c 'python manage.py migrate && python manage.py collectstatic'
web: gunicorn nutrack.wsgi --log-file -
