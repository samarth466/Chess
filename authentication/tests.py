from django.test import TestCase
from authentication.forms import RegistrationForm


class AuthenticationTest(TestCase):
    def test_registration_form_email(self):
        form = RegistrationForm(data={"email": ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["email"], ["This field is required."])
