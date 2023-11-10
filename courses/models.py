from django.db import models



class Course(models.Model):
    name = models.CharField(max_length=80)
    description = models.CharField(max_length=250)
    content = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    order = models.PositiveIntegerField(default=0)
    featured_image = models.ImageField('image', default='placeholder')

    def __str__(self):
        return self.name


class Testimonials(models.Model):
    course = models.ForeignKey(Course,
                             on_delete=models.CASCADE,
                             related_name='testimonial')
    name = models.CharField(max_length=80)
    review = models.CharField(max_length=250)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Testimonials"
        ordering = ['-created_on']
    

    def __str__(self):
        return self.review

