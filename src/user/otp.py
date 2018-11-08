"""
  - Check if user is allowed to request OTP:
    + last_request_otp_time - now > INTERVAL_REQUEST?
      > True: request_count = 0. Move to next step.
      > False:
        request_count > MAX_TIME_REQUEST_ALLOWED?
          True: not allowed
          False: allowed && request_count += 1 
  - Check if user is allowed to check OTP:
    SAME
"""
import hashlib
import base64
import datetime

from django.utils import timezone
from django.conf import settings

from pyotp import TOTP

from user.models import OneTimePassword
from user.const import OTP_INTERVAL
from user.exceptions import LimitedException, InvalidOTPException


def generate_secret_key(signature):
  """
  Generate secret key from given signature
  :param str:
  :return bytes:
  """
  secret_key = '%s%s' % (
    signature,
    settings.SECRET_KEY,
  )

  secret_key = hashlib.md5(secret_key.encode('utf-8')).hexdigest()
  key_in_bytes = base64.b32encode(secret_key.encode('utf-8'))
  return key_in_bytes[:16]


def generate_otp(signature, interval=OTP_INTERVAL.OTP_LIVE_TIME, for_time=None):
  """
  :param signature:
  :param interval:
  :param for_time:
  :return: str
  """
  key = generate_secret_key(signature)
  totp = TOTP(key, interval=interval)
  if for_time is None:
    for_time = datetime.datetime.now().replace(microsecond=0)
  # TODO: Logger for generated OTP code
  return totp.at(for_time)


def generate_otp_from_instance(instance, interval=OTP_INTERVAL.OTP_LIVE_TIME):
  """
  :param instance:
  :param interval:
  :return: tuple(otp, signature)
  """
  if not instance.can_request_otp():
    raise LimitedException
  instance.refresh_signature(commit=True)
  signature = instance.signature
  otp = generate_otp(signature, interval=interval)
  return otp, signature


def get_otp_instance(signature):
  """
  :param signature:
  :return: OneTimePassword
  """
  try:
    params = dict(signature=signature)
    return OneTimePassword.objects.get(**params)
  except OneTimePassword.DoesNotExist:
    return None


def is_valid_otp(otp, instance, interval=OTP_INTERVAL.OTP_LIVE_TIME, for_time=None):
  """
  :param otp:
  :param otp_instance:
  :param interval:
  :param for_time:
  :return: boolean
  """
  if not instance.can_check_otp():
    raise LimitedException

  if not instance or not instance.signature:
    return False

  signature = instance.signature
  key = generate_secret_key(signature)
  totp = TOTP(key, interval=interval)
  if for_time is None:
    for_time = datetime.datetime.now().replace(microsecond=0)
  # TODO: Logger for generated OTP code
  return totp.verify(otp, for_time, valid_window=1)
