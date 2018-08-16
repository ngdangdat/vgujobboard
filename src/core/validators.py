from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.conf import settings

import phonenumbers

def validate_phone_number(value, country_code='VN'):
    """
    Validate a phone number
    :param value:
    :param country_code: country code to check phone number
    :return: formated phone number
    """
    msg = _('Invalid phone number format.')
    try:
        phone = phonenumbers.parse(value, country_code)
    except:
        raise ValidationError(msg)
    if not phonenumbers.is_valid_number_for_region(phone, country_code):
        raise ValidationError(msg)
    return value


def validate_password(value):
    """
    Validate given password is valid with following rules:
    - Length >= PASSWORD_MIN_LENGTH
    - At least 1 digit
    :param value: Password
    :return: str
    """
    if len(value) < settings.PASSWORD_MIN_LENGTH:
        raise ValidationError(_('Require %d characters at least.'))

    total_digits = sum([1 for c in value if c.isdigit()])
    if total_digits < settings.PASSWORD_MIN_DIGITS:
        raise ValidationError(_('Require %d digits at least.'))

    return value

def validate_intake(value):
    current_year = datetime.now().year
    return value < current_year - 4
