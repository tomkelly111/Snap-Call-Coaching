from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    content = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name


class Coach(models.Model):
    name = models.CharField(max_length=80)
    courses = models.ManyToManyField(Course)
    biography = models.TextField(max_length=500)
    accolades = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Coaches"
