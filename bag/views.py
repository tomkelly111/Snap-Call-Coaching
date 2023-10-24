from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from courses.models import Course

# Create your views here.


def view_bag(request):
    """a view to return shopping bag"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, course_id):
    """ Add a course of the to the shopping bag """

    course = get_object_or_404(Course, pk=course_id)
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    if course_id in bag:
        messages.info(
            request, f'The {course.name} course is already in your cart')
    else:
        bag[course_id] = quantity
        messages.success(
            request, f'The {course.name} course has been added to your cart')

    request.session['bag'] = bag
    return redirect(redirect_url)


def remove_from_bag(request, course_id):
    """ remove item from shopping bag """
    course = get_object_or_404(Course, pk=course_id)
    try:
        bag = request.session.get('bag', {})
        bag.pop(course_id)
        messages.success(
            request, f'The {course.name} course has been removed from your cart')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing course: {e}')
        return HttpResponse(status=500)
