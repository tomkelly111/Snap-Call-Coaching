from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('course-detail/<str:course>/',
         views.course_subscriptions, name="course_subscriptions"),
]
