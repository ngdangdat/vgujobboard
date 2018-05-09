import math

from django.utils.encoding import force_text
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ungettext

from rest_framework.exceptions import APIException
from rest_framework import status


class Throttled(APIException):
    status_code = status.HTTP_429_TOO_MANY_REQUESTS
    default_detail = _('Request was throttled.')
    extra_detail_singular = 'Expected available in {wait} second.'
    extra_detail_plural = 'Expected available in {wait} seconds.'
    default_code = 'throttled'

    def __init__(self, wait=None, detail=None, code=None):
        if detail is None:
            detail = force_text(self.default_detail)
        if wait is not None:
            wait = math.ceil(wait)
            detail = ' '.join((
                detail,
                force_text(ungettext(self.extra_detail_singular.format(wait=wait),
                                    self.extra_detail_plural.format(wait=wait),
                                    wait)) 
            ))
        self.wait = wait
        super(Throttled, self).__init__(detail, code)


class CODE(object):
    NOT_FOUND = 'not_found'
    PERMISSION_DENIED = 'permission_denied'

    class AUTH(object):
        CREDENTIAL_INVALID = 'credential_invalid'
        CREDENTIAL_MISSING = 'credential_missing'


    class USER(object):
        DISABLED = 'user_disabled'
        NOT_VERIFIED = 'user_not_verified'
        REQUIRED_EMAIL = 'required_email'
        OTP_REQUEST_LIMITED = 'otp_request_limited'
        OTP_INVALID = 'otp_invalid'


def __api_exc_init__(self, detail=None, code=None):
    """
    Patch for rest_framework.exceptions.APIException.__init__
    Injected code to Exception
    """
    if detail is not None:
        self.detail = force_text(detail)
    else:
        self.detail = force_text(self.default_detail)
    if code is not None:
        self.code = code


def __validator_exc_ini__(self, detail=None, code=None):
    """
    Patch for rest_framework.exceptions.ValidationError.__init__
    Injected code to Exception
    """
    if not isinstance(detail, dict) and not isinstance(detail, list):
        detail = [detail]
    self.detail = detail
    if code is not None:
        self.code = code
