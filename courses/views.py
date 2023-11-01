from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Course, Testimonials
from django.contrib.auth.decorators import login_required
from .forms import CourseForm
from django.contrib import messages

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
    detail = get_object_or_404(Course, name=course)
    testimonials = Testimonials.objects.filter(course=detail)
    print(detail)  # Check the value of 'detail'
    for testimonial in testimonials:
        # Check the values of testimonials
        print(testimonial.name, testimonial.review, testimonial.created_on)
    context = {
        'course': detail,
        'testimonials': testimonials
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
            messages.error(request, 'Failed to add new course, please ensure form is validly completed')
    else:
        form = CourseForm()
    form = CourseForm()
    template = 'courses/add_course.html'
    context = {
        'form': form,
    }
    return render (request, template, context)


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
                request, 'Failed to update course. Please ensure the form is valid.')
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
def delete_course(request, course_id):
    """ delete a course """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admins can do that')
        return redirect(reverse('home'))

    course = get_object_or_404(Course, pk=course_id)
    course.delete()
    messages.success(request, 'Successfully deleted course!')
    return redirect(reverse('course_contents'))
