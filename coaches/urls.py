from django.urls import path
from . import views

urlpatterns = [
    path('', views.coach_bios, name='coach_bios'),
]
