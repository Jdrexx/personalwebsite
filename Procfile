web: python manage.py collectstatic --noinput && gunicorn personalwebsite.wsgi --bind 0.0.0.0:$PORT --workers 2 --timeout 120 --access-logfile - --error-logfile - --capture-output --max-requests 1000 --max-requests-jitter 100
release: python manage.py migrate --noinput
