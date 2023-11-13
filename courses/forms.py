from django import forms
from .models import Course, Testimonials


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'forms-styling rounded-0'


class TestimonialsForm(forms.ModelForm):
    class Meta:
        model = Testimonials
        fields = ('name', 'review')
        labels = {
            'name': 'Name',
            'review': 'What did you think of the course?',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'forms-styling rounded-0'
