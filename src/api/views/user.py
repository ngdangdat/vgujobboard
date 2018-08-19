from rest_framework import viewsets, mixins
from rest_framework.decorators import list_route
from rest_framework import status
from rest_framework.settings import api_settings
from rest_framework.exceptions import PermissionDenied, ParseError, NotFound, NotAuthenticated

from api.serializers import UserSerializer, UserChangePasswordSerializer, UserChangePasswordByOTPSerializer
from api.http import Response
from api.exceptions import Throttled, CODE

from user.models import User, OneTimePassword
from user.otp import generate_otp_from_instance, is_valid_otp
from user.exceptions import LimitedException, InvalidOTPException
from user.const import OTP_INTERVAL

def raise_throttled(wait=None, detail=None):
  exc = Throttled(wait=wait, detail=detail)
  exc.code = CODE.USER.OTP_REQUEST_LIMITED
  raise exc

class UserViewSet(viewsets.ModelViewSet, mixins.ListModelMixin):
  permission_classes = (api_settings.DEFAULT_PERMISSION_CLASSES,)
  serializer_class = UserSerializer
  queryset = User.objects.get_active_users()

  def create(self, request, *args, **kwargs):
    """
    @apiVersion 1.0.0
    @api {POST} /user
    @apiName Register
    @apiGroup User
    @apiPermission none

    @apiParam {string} email user's email
    @apiParam {string} password user's password
    @apiParam {string} first_name user's first name
    @apiParam {string} last_name user's last name
    @apiParam {string} profile__major user's major
    @apiParam {string} profile__intake user's intake
    @apiParam {integer} profile__gender user's gender

    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
        {
            "status": 200,
            "success": true,
            "errors: [],
            "data": {
                "email": "ngdangdat09@gmail.com",
                "password": "Admin@123",
                "first_name": "Dat",
                "last_name": "Nguyen",
                "id": 5,
                "profile": {
                  "gender": 5,
                  "major": "EEIT",
                  "intake": 2017,
                  "phone_number": "0905772919",
                  "state": "Quy Nhon",
                  "birthday": "10/11/1994",
                  "country": "VN",
                  "organization": "Vinagame",
                  "title": "Software Engineer",
                  "status": null,
                }
            }
        }
    """
    serializer = self.get_serializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    headers = self.get_success_headers(serializer.data)
    data = serializer.data
    return Response(data, status=status.HTTP_201_CREATED, headers=headers)

  def update(self, request, pk, *args, **kwargs):
    """
    @apiVersion 1.0.0
    @api {PUT} /user/:id
    @apiName Update
    @apiGroup User
    @apiPermission none

    @apiParam {Object} profile User's profile

    @apiSuccessExample {json} Success-Response:
        HTTP/1.1 200 OK
          {
            "success": true,
            "errors": [],
            "data": {
                "id": 3,
                "email": "dat01@yopmail.com",
                "first_name": "Dat",
                "last_name": "Nguyen",
                "profile": {
                    "gender": 5,
                    "major": "EEIT",
                    "intake": 2012,
                    "phone_number": null,
                    "state": "Ahihi",
                    "country": "Test",
                    "office": "Test",
                    "job_title": "Test",
                    "message": null,
                    "name": "Dat Nguyen"
                }
            },
            "status": 200
          }
    """
    if int(pk) != request.user.id:
      raise PermissionDenied()
    serializer = self.get_serializer(data=request.data, instance=request.user, partial=True)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
    return Response(serializer.data)

  def get_serializer_context(self):
    context = super().get_serializer_context()
    files = self.request.data.pop('files', {})
    context['files'] = files
    return context

  def list(self, *args, **kwargs):
    """
    @api {GET} /user

    @apiSuccessExample {json} Success-Response:
      HTTP/1.1 200 OK
      {
        "success": true,
        "status": 200,
        "data": [
            {
              "id": 3,
              "email": "dat01@yopmail.com",
              "first_name": "Dat",
              "last_name": "Nguyen",
              "profile": {
                  "gender": 5,
                  "major_intake": "Test 2",
                  "phone_number": null,
                  "state": "Ahihi",
                  "country": "Test",
                  "office": "Test",
                  "job_title": "Test",
                  "message": null,
                  "name": "Dat Nguyen"
              }
            },
            {
              "id": 1,
              "email": "ngdangdat09@gmail.com",
              "first_name": "",
              "last_name": "",
              "profile": {
                  "gender": 5,
                  "major_intake": "",
                  "phone_number": null,
                  "state": "",
                  "country": "",
                  "office": "",
                  "job_title": "",
                  "message": "",
                  "name": " "
                }
            }
        ],
        "errors": []
    }
    """
    return super(UserViewSet, self).list(*args, **kwargs)

  def retrieve(self, request, pk=None, *args, **kwargs):
    """
    @apiVersion 1.0.0
    @api {GET} /user/:id User > Retrieve
    @apiDescription Retrieve User
    @apiGroup User
    @apiPermission Authenticated
    """
    if not request.user.is_authenticated:
      raise NotAuthenticated()
    try:
      instance = self.get_queryset().get(pk=pk)
    except Exception:
      raise NotFound()
    serializer = self.get_serializer(instance)
    return Response(serializer.data)

  @list_route(methods=['get'], permission_classes=(api_settings.DEFAULT_PERMISSION_CLASSES,))
  def profile(self, request):
    """
    @api {GET} /user/profile

    @apiSuccessExample {json} Success-Response:
      HTTP/1.1 200 OK
        {
          "errors": [],
          "status": 200,
          "success": true,
          "data": {
            "id": 3,
            "email": "dat01@yopmail.com",
            "first_name": "Dat",
            "last_name": "Nguyen",
            "profile": {
              "gender": 5,
              "major_intake": "Test",
              "phone_number": null,
              "state": "Ahihi",
              "country": "Test",
              "office": "Test",
              "job_title": "Test",
              "message": null,
              "name": "Dat Nguyen"
            }
            
          }
        }
    """
    user = request.user
    data = UserSerializer(instance=user).data
    return Response(data)

  @list_route(methods=['post'], permission_classes=())
  def request_otp(self, request, identify=None, *args, **kwargs):
    """
    @apiVersion 1.0.0
    @api {POST} /user/request_otp Require otp
    @apiDescription Request send otp via email sent to email
    @apiName Verify user
    @apiGroup User
    @apiPermission None

    @apiError ParseError 400
    @apiError NotFound 404
    @apiError Throttled 429

    @apiParam {string} type email

    @apiParamExample {json} Request-by-email
        {
            "email": "ngdangdat09@gmail.com",
        }

    @apiSuccessExample {json} Success-with-email:
        {
          "data" : {
              "otp" : "655343",
              "signature" : "107b40205eff8bec52b8982ca7c216ce"
          },
          "status" : 200,
          "errors" : [],
          "success" : true
        }
    """
    email = request.data.get('email', None)
    if not email:
      raise ParseError('Email is required to generate OTP.')
    try:
      user = User.objects.get(email=email)
      otp_instance = user.get_otp_instance()
    except User.DoesNotExist:
      raise NotFound('User not found.')

    try:
      otp, signature = generate_otp_from_instance(otp_instance)
    except LimitedException:
      raise_throttled(OTP_INTERVAL.OTP_REQUEST)

    return Response({
      'otp': otp,
      'signature': signature,
    })

  @list_route(methods=['post'], permission_classes=())
  def verify(self, request, *args, **kwargs):
    """
    @apiVersion 1.0.0
    @api {POST} /user/verify Verify OTP
    @apiDescription Verify given OTP with given signature
    @apiName Verify user
    @apiGroup User
    @apiPermission None

    @apiError ParseError 400
    @apiError NotFound 404
    @apiError Throttled 429

    @apiParam {string} type email

    @apiParamExample {json}
        {
            "signature": "107b40205eff8bec52b8982ca7c216ce",
            "otp": "655343"
        }

    @apiSuccessExample {json} Success-with-email:
        {
          "data" : {
              "otp" : "655343",
              "signature" : "107b40205eff8bec52b8982ca7c216ce"
          },
          "status" : 200,
          "errors" : [],
          "success" : true
        }
    """
    otp = request.data.get('otp', None)
    signature = request.data.get('signature', None)
    try:
      otp_instance = OneTimePassword.objects.get(signature=signature)
    except OneTimePassword.DoesNotExist:
      raise NotFound('User doesn\'t exist.')

    try:
      is_valid = is_valid_otp(otp, otp_instance)
    except LimitedException:
      raise_throttled(OTP_INTERVAL.OTP_CHECK)

    return Response({
      'valid': is_valid
    })

  @list_route(methods=['put'], permission_classes=())
  def password(self, request, *args, **kwargs):
    otp = request.data.get('otp', None)
    data = request.data.copy()

    if otp is not None:
      serializer = UserChangePasswordByOTPSerializer(data=data)
      try:
        serializer.is_valid(raise_exception=True)
      except LimitedException:
        raise_throttled(OTP_INTERVAL.OTP_CHECK)
    else:
      if not request.user.is_authenticated:
        raise NotAuthenticated()
      context = dict(user=request.user)
      serializer = UserChangePasswordSerializer(data=data, context=context)
      serializer.is_valid(raise_exception=True)
      serializer.save()
    return Response({})
