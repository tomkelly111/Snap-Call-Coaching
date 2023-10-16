from django.contrib import admin
from .models import Course, Coach
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    list_display = ('name', 'description', 'price')
    summernote_fields = ('content',)


@admin.register(Coach)
class CoachAdmin(SummernoteModelAdmin):
    list_display = ('name', 'display_courses')
    summernote_fields = ('biography', 'accolades')

    def display_courses(self, obj):
        return ", ".join([course.name for course in obj.courses.all()])

    display_courses.short_description = 'Coaches the following courses:'
