from django.shortcuts import render
from .models import Course, Coach

# Create your views here.


def course_contents(request):
    """a view to return courses page"""
    courses = Course.objects.all()

    context = {
        'courses': courses
    }
    return render(request, 'courses/course_contents.html', context)


def course_detail(request):
    """a view to return course detail page"""

    return render(request, 'courses/course_detail.html')
