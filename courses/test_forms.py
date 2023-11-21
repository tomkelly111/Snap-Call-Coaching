from django.test import TestCase
from .forms import CourseForm, TestimonialsForm


class TestCourseForm(TestCase):

    def test_fields_are_required(self):
        form = CourseForm({'name': '',
                           'description': '',
                           'content': '',
                           'price': '',
                           'order': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertIn('description', form.errors.keys())
        self.assertIn('content', form.errors.keys())
        self.assertIn('price', form.errors.keys())
        self.assertIn('order', form.errors.keys())
        self.assertEqual(form.errors['name']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['description']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['content']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['price']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['order']
                         [0], 'This field is required.')

    def test_fields_not_required(self):
        form = CourseForm({'name': 'test',
                           'description': 'test',
                           'content': 'test',
                           'price': '100',
                           'order': '1',
                           'featured_image': ''})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form(self):
        form = CourseForm()
        self.assertEqual(form.Meta.fields,
                         ('__all__'))


class TestTestimonialsForm(TestCase):

    def test_fields_are_required(self):
        form = TestimonialsForm({'name': '',
                                 'review': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertIn('review', form.errors.keys())
        self.assertEqual(form.errors['name']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['review']
                         [0], 'This field is required.')

    def test_fields_are_explicit_in_form(self):
        form = TestimonialsForm()
        self.assertEqual(form.Meta.fields,
                         ('name', 'review'))
