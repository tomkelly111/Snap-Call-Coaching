from django.test import TestCase


class TestViews(TestCase):
    """
    Test users can with empty bag that tries
    to access checkout is redirected to courses
    """
    def test_checkout_view(self):
        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/courses/')
