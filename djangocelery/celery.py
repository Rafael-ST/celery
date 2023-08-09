import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangocelery.settings')
app = Celery("djangocelery")
# app = Celery('djangoceleray', broker="redis://localhost:6379", backend="redis://localhost:6379")
app.config_from_object("django.conf:settings")

@app.task
def add_numbers():
    return

app.autodiscover_tasks()
