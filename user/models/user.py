from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, update_last_login, Group)
from django.utils.translation import ugettext_lazy as _
from user.const import USER_STATUS
from django.utils import timezone

class AbstractUser(AbstractBaseUser, PermissionsMixin):
  is_staff = models.BooleanField(
    _('Staff status'),
    default=False,
    help_text=('Designate if user can log in admin site'),
  )
  is_validated = models.BooleanField(_('Validation status'), default=False)
  date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

  USERNAME_FIELD = 'email'

  class Meta:
    abstract = True

class User(AbstractBaseUser):
  email = models.CharField(
    _('Email'),
    unique=True,
    null=True,
    default=None,
    blank=True,
    help_text=_('Required field.'),
    error_messages={
      'unique': _('A user with that email already exists.')
    },
  )
  name = models.CharField(_('Full name'), max_length=150, blank=True)
