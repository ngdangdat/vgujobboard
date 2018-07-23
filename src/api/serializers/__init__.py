from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate

from rest_framework import serializers
from rest_framework.serializers import ValidationError

from api.exceptions import CODE
from api.serializers.base import Serializer

class AuthSerializer(Serializer):
    email = serializers.CharField(label=_("Email"), required=False, allow_blank=False)
    password = serializers.CharField(label=_("Password"), style={'input_type': 'password'})

    def check_login_allowed(self, user):
        if user.is_staff or user.is_superuser:
            msg = _("Staff account is disabled.")
            raise ValidationError(
                msg, CODE.USER.DISABLED
            )

        if not user.is_active:
            msg = _("User is disabled.")
            raise ValidationError(
                msg, CODE.USER.DISABLED
            )

    def validate(self, attrs):
        if attrs:
            email = attrs.pop('email', None)
            user = authenticate(email=email, **attrs)
            if user:
                self.check_login_allowed(user)
            else:
                msg = _("Credentials invalid.")
                raise ValidationError(
                    msg, CODE.AUTH.CREDENTIAL_INVALID
                )
        else:
            msg = _("Missing credentials provided.")
            raise ValidationError(
                msg, CODE.AUTH.CREDENTIAL_MISSING
            )
        attrs['user'] = user
        return attrs

from .user import UserSerializer, ProfileSerializer, UserChangePasswordSerializer, UserChangePasswordByOTPSerializer
