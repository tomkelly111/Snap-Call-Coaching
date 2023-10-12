from django.shortcuts import render

# Create your views here.


def course_contents(request):
    """a view to return courses page"""
    return render(request, 'courses/course_contents.html')
