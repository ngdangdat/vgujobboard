from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import rotate_token
from django.contrib.auth import _get_backends

from rest_framework import viewsets, exceptions, permissions
from rest_framework.decorators import list_route
from rest_framework.authentication import get_authorization_header

from api.http import Response
from api.serializers import AuthSerializer, ProfileSerializer
from api.models import Token

from user.models import Profile

SESSION_KEY = '_auth_user_id'
BACKEND_SESSION_KEY = '_auth_user_backend'
HASH_SESSION_KEY = '_auth_user_hash'

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

    @csrf_exempt
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
        return self.login_success(serializer.validated_data['user'], request)

    def login_success(self, user, request):
        # token = Token.objects.create(user=user)
        try:
            backend = user.backend
        except AttributeError:
            backends = _get_backends(return_tuples=True)
            if len(backends) == 1:
                _, backend = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument or set the '
                    '`backend` attribute on the user.'
                )
        session_auth_hash = ''
        if hasattr(user, 'get_session_auth_hash'):
            session_auth_hash = user.get_session_auth_hash()

        request.session[SESSION_KEY] = user._meta.pk.value_to_string(user)
        request.session[BACKEND_SESSION_KEY] = backend
        request.session[HASH_SESSION_KEY] = session_auth_hash
        user_logged_in.send(sender=user.__class__, request=self.request, user=user)
        if hasattr(request, 'user'):
            request.user = user
        rotate_token(request)
        return Response({
            # 'token': token.key,
            'user': {
                'id': user.id,
                'email': user.email,
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
