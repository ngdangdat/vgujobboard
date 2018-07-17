import phonenumbers
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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