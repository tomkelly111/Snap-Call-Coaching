from django.shortcuts import render
from .models import Course

# Create your views here.


def course_contents(request):
    """a view to return courses page"""
    courses = Course.objects.all()

    context = {
        'courses': courses
    }
    return render(request, 'courses/course_contents.html', context)
