from django.contrib import admin
from .models import Course, Testimonials
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    list_display = ('name', 'description', 'price')
    summernote_fields = ('content',)


@admin.register(Testimonials)
class testimonialAdmin(admin.ModelAdmin):
    list_display = ('course', 'name', 'created_on', 'approved')
