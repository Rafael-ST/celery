from django.shortcuts import render
from .tasks import simple_task
from django.http import JsonResponse

def trigger_task(request):
    simple_task.delay("Hello from Celery!")
    return JsonResponse({"message": "Task triggered!"})
