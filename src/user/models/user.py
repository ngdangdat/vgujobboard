from django.db import models
from django.db.models.manager import Manager

from django.contrib.auth.models import \
  (AbstractBaseUser, PermissionsMixin, Group as RootGroup)

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.crypto import get_random_string


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

class Group(RootGroup):
  """Proxy class"""
  class Meta:
    proxy = True
