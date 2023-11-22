from django.test import TestCase


class TestViews(TestCase):
    """
    Test users can access coach bios
    """
    def test_coach_bios_view(self):
        response = self.client.get('/our_team/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'coaches/coach_bios.html')
