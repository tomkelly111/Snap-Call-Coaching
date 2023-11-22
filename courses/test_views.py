from django.test import TestCase
from django.contrib.auth.models import User
from .models import Course


class TestViews(TestCase):
    """
    Checks that a logged in user that accesses the edit url
    is redirected to the homepage
    """
    def test_edit_course_for_loggedin_user(self):
        course = Course.objects.create(name='test',
                                       description='test',
                                       content='test',
                                       price=100,
                                       order=1,
                                       featured_image='placeholder')
        self.user = User.objects.create_user(username='testuser',
                                             password='12345')
        login = self.client.login(username='testuser', password='12345')
        response = self.client.get(f'/courses/edit/{course.id}')
        self.assertRedirects(response, '/')

    """
    Tests if anonymous user is redirected to login
    when they try to access the edit course page
    """
    def test_edit_course_for_anonymous_user(self):
        course = Course.objects.create(name='test',
                                       description='test',
                                       content='test',
                                       price=100,
                                       order=1,
                                       featured_image='placeholder')
        response = self.client.get(f'/courses/edit/{course.id}')
        self.assertRedirects(response,
                             f'/accounts/login/?next=/'
                             f'courses/edit/{course.id}')
    """
    Checks that a logged in user that accesses the delete url
    is redirected to the homepage
    """
    def test_delete_course_for_loggedin_user(self):
        course = Course.objects.create(name='test',
                                       description='test',
                                       content='test',
                                       price=100,
                                       order=1,
                                       featured_image='placeholder')
        self.user = User.objects.create_user(username='testuser',
                                             password='12345')
        login = self.client.login(username='testuser', password='12345')
        response = self.client.get(f'/courses/delete/{course.id}')
        self.assertRedirects(response, '/')

    """
    Tests if anonymous user is redirected to login
    when they try to access the delete course page
    """
    def test_delete_course_for_anonymous_user(self):
        course = Course.objects.create(name='test',
                                       description='test',
                                       content='test',
                                       price=100,
                                       order=1,
                                       featured_image='placeholder')
        response = self.client.get(f'/courses/delete/{course.id}')
        self.assertRedirects(response,
                             f'/accounts/login/?next=/'
                             f'courses/delete/{course.id}')
