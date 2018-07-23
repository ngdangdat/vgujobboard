from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

from rest_framework import viewsets, exceptions, permissions
from rest_framework.decorators import list_route
from rest_framework.authentication import get_authorization_header

from api.http import Response
from api.serializers import AuthSerializer
from api.models import Token


def get_token_from_header(request):
    """ Get token from request's header """
    auth = get_authorization_header(request)
    try:
        auth = auth.split()
        token = auth[1].decode()
        return token
    except Exception:
        msg = _('Invalid token header.')
        raise exceptions.AuthenticationFailed(msg)


class AuthViewSet(viewsets.GenericViewSet):
    permission_classes = ()
    serializer_class = AuthSerializer

    def create(self, request, *args, **kwargs):
        """
        @apiVersion 1.0.0
        @api {POST} /auth Login
        @apiName Login
        @apiGroup Auth
        @apiPermission none

        @apiParam {string} email user's email
        @apiParam {string} password user's password

        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
                "status": 200,
                "errors": [],
                "success": true,
                "data": {
                    "user": {
                        "is_staff": false,
                        "email": "dat01@yopmail.com",
                        "name": "Dat Nguyen"
                    },
                    "token": "d5d6d757923c9f67cc8f56eac0460f36a2f14422"
                }
            }
        """
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except exceptions.ValidationError as e:
            user_login_failed.send(sender=__name__, credentials=request.data)
            raise e
        return self.login_success(serializer.validated_data['user'])

    def login_success(self, user):
        user_logged_in.send(sender=user.__class__, request=self.request, user=user)
        token = Token.objects.create(user=user)
        return Response({
            'token': token.key,
            'user': {
                'email': user.email,
                'name': user.profile.name,
                'is_staff': user.is_staff,
            }
        })

    def delete(self, request, *args, **kwargs):
        """
        @apiVersion 1.0.0
        @api {DELETE} /auth Login
        @apiName Logout
        @apiGroup Auth
        @apiPermission Authenticated

        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
                "status": 200,
                "success": true,
                "errors: [],
                "data": {}
            }
        """
        try:
            token_key = get_token_from_header(request)
            token = Token.objects.get(key=token_key)
            user = token.user
            token.delete()
            user_logged_out.send(sender=user.__class__, request=request, user=user)
        except Exception:
            raise exceptions.AuthenticationFailed(_('Invalid Token'))
        return Response()
