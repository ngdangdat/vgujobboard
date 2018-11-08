import hashlib

from django.db import models
from django.db.models.manager import Manager
from django.contrib.auth.models import \
  (AbstractBaseUser, PermissionsMixin, Group as RootGroup)
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string
from django.conf import settings

from api.models import Token
from user.const import OTP_INTERVAL, OTP_LIMIT


class BaseUserManager(Manager):
  @classmethod
  def normalize_email(cls, email):
    """
    Lowercase the email's domain part
    """
    email = email or ''
    try:
      email_name, domain_part = email.strip().rsplit('@', 1)
    except ValueError:
      pass
    else:
      email = '@'.join([email_name, domain_part.lower()])
    return email

  @classmethod
  def make_random_password(self, length=10,
                          allowed_chars='abcdefghjkmnpqrstuvwxyz'
                                        'ABCDEFGHJKLMNPQRSTUVWXYZ'
                                        '23456789'):
    return get_random_string(length, allowed_chars)

  def get_by_natural_key(self, username):
    return self.get(**{self.model.USERNAME_FIELD: username})


class UserManager(BaseUserManager):

  def _create_user(self, email, password, **extra_fields):
    """
    Create and save a user with given email, password
    """
    if not email:
      raise ValueError('The email must be set')
    email = self.normalize_email(email)
    user = self.model(email=email, **extra_fields)
    # @TODO Create make_random_password
    user.set_password(password)
    user.save(using=self._db)
    return user
  
  def create_user(self, email=None, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', False)
    extra_fields.setdefault('is_superuser', False)
    return self._create_user(email, password, **extra_fields)
  
  def create_superuser(self, email=None, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
    if extra_fields.get('is_superuser') is not True:
        raise ValueError('Superuser must have is_superuser=True.')

    return self._create_user(email, password, **extra_fields)

  def get_active_users(self):
    return self.filter(is_staff=False, is_active=True).order_by('-id')


class AbstractUser(AbstractBaseUser, PermissionsMixin):
  is_staff = models.BooleanField(
    _('Staff status'),
    default=False,
    help_text=('Designate if user can log in admin site'),
  )
  is_active = models.BooleanField(
    _('Active'),
    default=True,
    help_text=_('Designates whether this user should be treated as active.')
  )
  date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  objects = UserManager()

  class Meta:
    abstract = True

class User(AbstractUser):
  email = models.CharField(
    _('Email'),
    unique=True,
    null=True,
    default=None,
    blank=True,
    help_text=_('Required field.'),
    max_length=245,
    error_messages={
      'unique': _('A user with that email already exists.')
    },
  )
  first_name = models.CharField(_('First name'), max_length=150, blank=True)
  last_name = models.CharField(_('Last name'), max_length=150, blank=True)

  serializer_class =  'api.serializers.UserSerializer'

  class Meta:
    db_table = 'auth_user'
    swappable = 'AUTH_USER_MODEL'
    permissions = (
        # ("change_status", "Can change status"),
        # Define other permission here
    )
  
  def __str__(self):
    return "%s %s" % (self.first_name, self.last_name)

  def save(self, *args, **kwargs):
    if not self.password:
      self.set_password(get_random_string(30))
    return super(User, self).save(*args, **kwargs)

  @property
  def token(self):
    try:
      token = Token.objects.get(user=self)
    except Exception:
      token = None
    return token

  def get_otp_instance(self):
    otp, created = OneTimePassword.objects.get_or_create(user=self)
    return otp

class Group(RootGroup):
  """Proxy class"""
  class Meta:
    proxy = True


def generate_signature(*args):
  """
  Generate signature using given arguments
  """
  text = ''
  for item in args:
    text += str(item)
  signature = '%s%s%s' % (text, settings.SECRET_KEY, timezone.now())
  signature = hashlib.md5(signature.encode('utf-8')).hexdigest()
  return signature


def get_duration(from_time, to_time):
  """
  :param from_time:
  :param to_time:
  :return: int
  """
  delta = to_time - from_time
  return delta.seconds


class OneTimePassword(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='otp_set')
  signature = models.CharField(max_length=32, db_index=True)
  send_counter = models.PositiveIntegerField(default=0)
  last_send = models.DateTimeField(default=timezone.now)
  check_counter = models.PositiveIntegerField(default=0)
  last_check = models.DateTimeField(default=timezone.now)

  objects = Manager()

  def save(self, *args, **kwargs):
    if not self.pk or not self.signature:
      self.refresh_signature()
    super(OneTimePassword, self).save(*args, **kwargs)

  def refresh_signature(self, commit=False):
    self.signature = generate_signature(self.user_id)
    if commit:
      self.save()

  def can_request_otp(self):
    now = timezone.now()
    duration = get_duration(self.last_send, now)
    if duration > OTP_INTERVAL.OTP_REQUEST:
      allowed = True
      self.send_counter = 1
    else:
      self.send_counter += 1
      allowed = self.send_counter <= OTP_LIMIT.OTP_REQUEST
    if allowed:
      self.last_send = now
    self.save()
    return allowed

  def can_check_otp(self):
    now = timezone.now()
    duration = get_duration(self.last_check, now)
    if duration > OTP_INTERVAL.OTP_CHECK:
      allowed = True
      self.check_counter = 1
    else:
      self.check_counter += 1
      allowed = self.check_counter <= OTP_LIMIT.OTP_CHECK
    if allowed:
      self.last_check = now
    self.save()
    return allowed
