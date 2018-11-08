from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.utils.translation import ugettext_lazy as _
from django.utils import six

from rest_framework.views import set_rollback
from rest_framework import exceptions, status

from api.http import Response
from api.exceptions import CODE
from core.utils import camel_to_snake_case

from .auth import AuthViewSet
from .user import UserViewSet

def exception_handler(exc, context):
    """
    Override to handle exception returning structured format
    """
    if isinstance(exc, Http404):
        msg = _("Not found.")
        errors = { CODE.NOT_FOUND: six.text_type(msg) }
        set_rollback()
        return Response(errors=errors, status=status.HTTP_404_NOT_FOUND)

    elif isinstance(exc, PermissionDenied):
        msg = _("Permission denied.")
        errors = { CODE.PERMISSION_DENIED: six.text_type(msg) }
        set_rollback()
        return Response(errors=errors, status=status.HTTP_403_FORBIDDEN)
    if isinstance(exc, exceptions.APIException):
        code = getattr(exc, 'code', None)
        headers = {}

        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait

        if isinstance(exc.detail, dict):
            errors = exc.detail
        else:
            if not code:
                errors = { 
                    camel_to_snake_case(exc.__class__.__name__): exc.detail
                }
            else:
                errors = {code: ' '.join(exc.detail)} if isinstance(exc.detail, list) else {code: exc.detail}
        set_rollback()
        return Response(errors=errors, status=exc.status_code, headers=headers)

    return None
