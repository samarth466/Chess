from django.test import TestCase
from UserAuth.forms import RegistrationForm

class UserAuthTest(TestCase):
    def test_registration_form_email(self):
        form = RegistrationForm(data={"email": ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["email"], ["This field is required."])
