from django.urls import path
from . import views

urlpatterns = [
    path('trigger/', views.trigger_task, name='trigger_task'),
]