from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_isnumeric(value):
    value = str(value)
    if not value.isnumeric():
        raise ValidationError(_('%(value)s is an invalid pin'),params={'value': value})