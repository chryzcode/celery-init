# Run on WSL or Linux(Ubuntu)

- Update and install redis
  sudo apt-get update
  sudo apt-get install redis

- Start redis server
sudo service redis-server start

- Connect to redis
redis-cli 

- Install in project
pip install celery[redis]
pip install django-celery-results

### Create a celery.py and tasks.py file and make config in settings.py file

- check the __init__.py file of the project folder
- Don't forget to migrate

To run Celery and process tasks, you need to start a Celery worker process.
celery -A your_project worker --loglevel=info
celery -A celery_init worker --loglevel=info

- For Celery Beat
celery -A celery_init beat --loglevel=debug --scheduler django_celery_beat.schedulers:DatabaseScheduler




- for configuration
https://docs.celeryq.dev/en/latest/django/first-steps-with-django.html#using-celery-with-django

