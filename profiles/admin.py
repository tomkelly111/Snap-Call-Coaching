from django.contrib import admin
from .models import UserProfile

# Register your models here.


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'display_courses')

    def display_courses(self, obj):
        return ", ".join(
            [course.name for course in obj.purchased_courses.all()]
            )

    display_courses.short_description = 'Enrolled in the following courses:'
