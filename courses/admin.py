from django.contrib import admin
from .models import Course
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    list_display = ('name', 'description', 'price')
    summernote_fields = ('content',)


