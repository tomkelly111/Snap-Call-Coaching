from django.test import TestCase
from .forms import OrderForm


class TestOrderForm(TestCase):

    """test that required fields are required """
    def test_fields_are_required(self):
        form = OrderForm({'full_name': '',
                          'email': '',
                          'phone_number': '',
                          'street_address1': '',
                          'town_or_city': '',
                          'country': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertIn('email', form.errors.keys())
        self.assertIn('phone_number', form.errors.keys())
        self.assertIn('street_address1', form.errors.keys())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(form.errors['full_name']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['email']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['phone_number']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['street_address1']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['town_or_city']
                         [0], 'This field is required.')
        self.assertEqual(form.errors['country']
                         [0], 'This field is required.')

    """test that non required fields are not required """
    def test_fields_not_required(self):
        form = OrderForm({'full_name': 'John Smith',
                          'email': 'john@mail.com',
                          'phone_number': '0812345678',
                          'street_address1': '123 Fakestreet',
                          'street_address2': '',
                          'town_or_city': 'Dublin',
                          'postcode': '',
                          'country': 'IE',
                          'county': ''})
        self.assertTrue(form.is_valid())

    """tests that all fields are present in form """
    def test_fields_are_explicit_in_form(self):
        form = OrderForm()
        self.assertEqual(form.Meta.fields,
                         ('full_name', 'email', 'phone_number',
                          'street_address1', 'street_address2',
                          'town_or_city', 'postcode', 'country',
                          'county'))
