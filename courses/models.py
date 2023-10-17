from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    content = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
