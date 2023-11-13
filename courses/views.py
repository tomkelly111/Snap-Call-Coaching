from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Course, Testimonials
from django.contrib.auth.decorators import login_required
from .forms import CourseForm, TestimonialsForm
from profiles.models import UserProfile
from django.contrib import messages

# Create your views here.


def course_contents(request):
    """a view to return courses page"""
    courses = Course.objects.order_by('order')

    context = {
        'courses': courses
    }
    return render(request, 'courses/course_contents.html', context)


def course_detail(request, course):
    """a view to return course detail page"""
    course = get_object_or_404(Course, name=course)
    testimonials = Testimonials.objects.filter(
        course=course).filter(approved=True)
    has_purchased = False
    has_reviewed = False

    if request.user.is_authenticated:
        user_profile = UserProfile.objects.get(user=request.user)
        if course in user_profile.purchased_courses.all():
            has_purchased = True
            if course in user_profile.reviewed_courses.all():
                has_reviewed = True
            else:
                if request.method == 'POST':
                    form = TestimonialsForm(request.POST)
                    if form.is_valid():
                        testimonial = form.save(commit=False)
                        testimonial.course = course
                        testimonial.save()
                        user_profile.reviewed_courses.add(course)
                        messages.success(
                            request, 'Your review is awaiting approval!')
                        return redirect(reverse('course_detail',
                                                args=[course.name]))
                    else:
                        messages.error(
                            request, 'Failed to submit. Please \
                            ensure the form is valid.')
                else:
                    form = TestimonialsForm()
    form = TestimonialsForm()
    context = {
        'course': course,
        'testimonials': testimonials,
        'form': form,
        'has_purchased': has_purchased,
        'has_reviewed': has_reviewed,
    }
    return render(request, 'courses/course_detail.html', context)


@login_required
def add_course(request):
    """add new courses to site"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can do that')
        return redirect(reverse('home'))
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save()
            messages.success(request, 'Successfully added new course!')
            return redirect(reverse('course_detail', args=[course.name]))
        else:
            messages.error(
                request, 'Failed to add new course, please \
                ensure form is validly completed')
    else:
        form = CourseForm()
    form = CourseForm()
    template = 'courses/add_course.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_course(request, course_id):
    """ Edit a course """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can do that')
        return redirect(reverse('home'))

    course = get_object_or_404(Course, pk=course_id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated course!')
            return redirect(reverse('course_detail', args=[course.name]))
        else:
            messages.error(
                request, 'Failed to update course. \
                Please ensure the form is valid.')
    else:
        form = CourseForm(instance=course)
        messages.info(request, f'You are editing {course.name}')

    template = 'courses/edit_course.html'
    context = {
        'form': form,
        'course': course,
    }

    return render(request, template, context)


@login_required
def delete_confirmation(request, course_id):
    """ delete a course """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can do that')
        return redirect(reverse('home'))

    course = get_object_or_404(Course, pk=course_id)
    template = 'courses/delete_confirmation.html'
    context = {
        'course': course,
    }

    return render(request, template, context)


@login_required
def delete_course(request, course_id):
    """ delete a course """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can do that')
        return redirect(reverse('home'))

    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    messages.success(request, 'Successfully deleted course!')
    return redirect(reverse('course_contents'))
