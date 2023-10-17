from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_contents, name="course_contents"),
    path('course-detail/<str:course>/',
         views.course_detail, name="course_detail"),
]
