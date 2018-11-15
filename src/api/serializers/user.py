from django.contrib.auth import authenticate
from django.conf import settings

from rest_framework import serializers, exceptions

from user.models import *
from user.otp import get_otp_instance, is_valid_otp
from user.exceptions import InvalidOTPException, LimitedException

from api.serializers.base import ModelSerializer, Serializer
from api.exceptions import CODE

from core.validators import validate_password, validate_avatar
from core.modules.image import create_image_from_b64

PROFILE_AVATAR_KEY = settings.PROFILE_AVATAR_KEY

PROFILE_FIELDS = (
  'gender', 'major', 'intake', 'phone_number', 'state', 'country',
  'organization', 'title', 'status', 'avatar', 'birthday',
  'linkedin',
)


class ProfileSerializer(ModelSerializer):
  avatar = serializers.CharField(max_length=255, required=False)

  def validate_avatar(self, value):
    try:
      validate_avatar(value)
    except Exception as e:
      raise exceptions.ValidationError('Invalid avatar.')
    return value
  
  def to_internal_value(self, data):
    files = self.context.get('files', {})
    if PROFILE_AVATAR_KEY in files:
      if 'avatar' in data:
        del data['avatar']
      avatar = files.get(PROFILE_AVATAR_KEY)
      data['avatar'] = save_temp_avatar(avatar)
    data = super(ProfileSerializer, self).to_internal_value(data)
    return data

  class Meta:
    model = Profile
    fields = PROFILE_FIELDS


class UserSerializer(ModelSerializer):
  profile = ProfileSerializer(required=False, many=False)
  password = serializers.CharField(write_only=True)

  def to_internal_value(self, data):
    ps = self.fields['profile']
    if self.instance:
      ps.instance = self.instance.profile
      ps.partial = True
    else:
      ps.instance = None
      ps.partial = False
    data = super(UserSerializer, self).to_internal_value(data)
    return data

  def create(self, validated_data):
    _profile = {}
    if 'profile' in validated_data:
      _profile = dict(validated_data.pop('profile'))

    if 'email' not in validated_data or not validated_data['email']:
      raise exceptions.ParseError('Please enter email.', CODE.USER.REQUIRED_EMAIL)
    
    user = User(**validated_data)
    user.set_password(validated_data['password'])
    user.is_active = False
    user.save()
    user.profile = Profile.objects.get_or_create_profile(user=user, **_profile)
    return user

  def update(self, instance, validated_data):
    files = self.context.get('files', {})
    if 'profile' in validated_data:
      profile = instance.profile
      data = validated_data.pop('profile', {})
      serializer = ProfileSerializer(instance=profile, data=data, partial=True, many=False, context=self.context)
      serializer.is_valid()
      serializer.save()
    instance = super(UserSerializer, self).update(instance, validated_data)
    return instance

  class Meta:
    model = User
    extra_kwargs = {'password': {'write_only': True}}
    fields = (
      'id', 'email', 'first_name', 'last_name', 'profile', 'password',
    )


class UserChangePasswordMixin(Serializer):
  new_password = serializers.CharField(required=True)

  def validate_new_password(self, value):
    if value:
      value = validate_password(value)
    return value

  def create(self, validated_data):
    user = self.context.get('user')
    user.set_password(validated_data.get('new_password'))
    user.save()
    return user


class UserChangePasswordSerializer(UserChangePasswordMixin):
  password = serializers.CharField(required=True)

  def validate(self, attrs):
    user = self.context.get('user')
    password = attrs.get('password', None)

    if not user.check_password(password):
      raise exceptions.ParseError('Invalid old password.', CODE.AUTH.CREDENTIAL_INVALID)

    return attrs


class UserChangePasswordByOTPSerializer(UserChangePasswordMixin):
  otp = serializers.CharField(required=True)
  signature = serializers.CharField(required=True)

  def validate(self, attrs):
    signature = attrs.get('signature')
    otp = attrs.get('otp')
    invalid_message = 'Invalid OTP.'

    otp_instance = get_otp_instance(signature)
    if not otp_instance:
      raise exceptions.ParseError(invalid_message, CODE.USER.OTP_INVALID)

    is_valid = is_valid_otp(otp, otp_instance)
    if not is_valid:
      raise exceptions.ParseError(invalid_message, CODE.USER.OTP_INVALID)

    self.context['user'] = otp_instance.user
    return attrs
