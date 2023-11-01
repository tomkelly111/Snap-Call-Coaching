from django.shortcuts import render, get_object_or_404
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib import messages
from courses.models import Course

@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your billing details have been saved')
        else:
            messages.error(
                request, 'Update failed, please ensure form is validly completed')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.purchased_courses.all()
    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


def course_subscriptions(request, course):
    """a view to return course detail page"""
    queryset = Course.objects
    detail = get_object_or_404(queryset, name=course)
    context = {
        'course': detail
    }
    return render(request, 'courses/course_detail.html', context)
