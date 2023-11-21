from django.test import TestCase
from .forms import UserProfileForm


class TestUserProfileForm(TestCase):

    """
    test that all fields which are non required
    fields are not required
    """
    def test_fields_not_required(self):
        form = UserProfileForm({'default_full_name': '',
                                'default_phone_number': '',
                                'default_street_address1': '',
                                'default_street_address2': '',
                                'default_town_or_city': '',
                                'default_postcode': '',
                                'default_country': '',
                                'default_county': ''})
        self.assertTrue(form.is_valid())

    """tests that all correct fields are present in form """
    def test_fields_are_explicit_in_form(self):
        form = UserProfileForm()
        self.assertEqual(form.Meta.exclude,
                         ('user',
                          'purchased_courses',
                          'reviewed_courses'))
