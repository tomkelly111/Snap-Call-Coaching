from django.shortcuts import render, get_object_or_404
from .models import Course

# Create your views here.


def course_contents(request):
    """a view to return courses page"""
    courses = Course.objects.all()

    context = {
        'courses': courses
    }
    return render(request, 'courses/course_contents.html', context)


def course_detail(request, course):
    """a view to return course detail page"""
    queryset = Course.objects
    detail = get_object_or_404(queryset, name=course)
    context = {
        'course': detail
    }
    return render(request, 'courses/course_detail.html', context)
