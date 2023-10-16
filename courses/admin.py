from django.contrib import admin
from .models import Course, Coach
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Course)
class CourseAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)


@admin.register(Coach)
class CoachAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)
