from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):

    def test_profile(self):
        """
        tests that an anonymous user is redirected
        when accessing profile url
        """
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 302)
        """
        tests that a logged in user can access profile
        and correct tempalte is used
        """
        self.user = User.objects.create_user(username='testuser',
                                             password='12345')
        login = self.client.login(username='testuser', password='12345')
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
