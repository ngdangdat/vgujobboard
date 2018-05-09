from datetime import datetime
import os

from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _
from django.conf import settings

PROFILE_AVATAR_KEY = settings.PROFILE_AVATAR_KEY

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

def validate_file(value, file_types=['jpeg', 'jpg', 'png'], max_size=None):
    """
    Validate file
    :param value: file path
    :param file_types: allowed file extensions
    :param max_size: max file size
    """
    name, ext = os.path.splitext(value)
    ext = ext.lower().replace('.', '')
    if ext not in file_types:
        raise ValidationError(_('Not allowed file extension.'))
    return value

validate_file.code = 'type_invalid'

validate_url = URLValidator()

def validate_avatar(value):
    """
    Validate avatar
    :param value: string url or path to file with PROFILE_AVATAR_KEY flag
    """
    name = value.name if not isinstance(value, str) else value
    if name.startswith(PROFILE_AVATAR_KEY):
        validate_file(name.replace(PROFILE_AVATAR_KEY, ''))
    else:
        validate_url(name)

validate_avatar.code = 'url_or_file_invalid'
