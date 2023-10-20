from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """a view to return shopping bag"""
    return render(request, 'bag/bag.html')


def add_to_bag(request, course_id):
    """ Add a course of the to the shopping bag """

    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    bag[course_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
