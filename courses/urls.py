from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_contents, name="course_contents"),
    path('course-detail/<str:course>/',
         views.course_detail, name="course_detail"),
    path('add/', views.add_course, name="add_course"),
]
