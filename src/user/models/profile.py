from os import path
from hashlib import md5
import timezone

from django.db import models
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from core.validators import validate_phone_number, validate_intake
from core.models import ModelDiffMixin

from user.const import GENDER, GENDER_CHOICES, MAJOR, MIN_INTAKE

PROFILE_AVATAR_KEY = 'profile.avatar'

def save_avatar(file_path):
  """
  :param file_path:
  :return: url
  """
  file_name = path.basename(file_path)
  name, ext = path.splitext(file_name)
  file_name = '%s%s' % (md5(str(timezone.now())), ext)
  new_file_path = get_storage_path(file_name)

class ProfileManager(models.Manager):
  def get_or_create_profile(self, user, **data):
    try:
      profile = self.get(user=user)
    except Exception:
      profile = self.create(user=user, **data)
    return profile


class Profile(ModelDiffMixin, models.Model):
  """
  Fields:
  - major
  - intake
  - birthday
  - phone_number - optional
  - state
  - country
  - organization
  - title
  - gender (drop-down box)
  - LinkedIn
  - message
  - avatar
  """
  user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
  gender = models.PositiveSmallIntegerField(_('Gender'), choices=GENDER_CHOICES, default=GENDER.UNDEFINED)
  birthday = models.DateTimeField(_('Birthday'), null=True, default=None, blank=True,)
  avatar = models.ImageField(
      _('Profile avatar'),
      upload_to='profile_pics/%Y-%m-%d/',
      null=True,
      blank=True,
      max_length=255,
      validators=[validate_avatar]
  )
  major = models.PositiveSmallIntegerField(_('Major'), choices=MAJOR.choices, default=MAJOR.UNDEFINED,)
  intake = models.PositiveSmallIntegerField(_('Intake'), default=MIN_INTAKE, validators=[validate_intake])
  phone_number = models.CharField(_('Phone Number'),
    default=None,
    max_length=15,
    blank=True,
    null=True,
    validators=[validate_phone_number]
  )
  state = models.CharField(_('City of Residence'), default='', max_length=255)
  country = models.CharField(_('Country of Residence'), default='', max_length=255)
  organization = models.CharField(_('Organization'), default='', max_length=255)
  title = models.CharField(_('Position/Major'), default='', max_length=255)
  linkedin = models.URLField(_('LinkedIn Profile URL'), null=True, blank=True)
  status = models.CharField(_('Status'), null=True, blank=True, default='', max_length=1000)

  objects = ProfileManager()

  def __str__(self):
    return "{}'s profile".format(self.user)

  @property
  def name(self):
    user = self.user
    return "%s %s" % (user.first_name, user.last_name)

  def clean(self):
    if self.avatar:
      name = self.avatar.name
      if name.startswith(PROFILE_AVATAR_KEY):
        self.avatar.name = name.replace(PROFILE_AVATAR_KEY, '')
