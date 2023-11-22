from django.test import TestCase

class TestViews(TestCase):
    """
    Test users can access bag (shopping cart)
    """
    def test_bag_view(self):
        response = self.client.get('/shopping_cart/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')