from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):

    def test_profile(self):
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
        self.user = User.objects.create_user(username='testuser',
                                             password='12345')
        login = self.client.login(username='testuser', password='12345')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
