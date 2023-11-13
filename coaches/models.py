from django.db import models
from courses.models import Course


class Coach(models.Model):
    name = models.CharField(max_length=80)
    courses = models.ManyToManyField(
        Course, blank=True, related_name='coached_courses')
    biography = models.TextField(max_length=500)
    accolades = models.TextField(max_length=500)
    featured_image = models.ImageField('image', default='placeholder')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Coaches"
