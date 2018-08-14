from django.db import models
from django.conf import settings

from django.utils.translation import ugettext_lazy as _

from core.validators import validate_phone_number
from user.const import GENDER, GENDER_CHOICES


class ProfileManager(models.Manager):
  def get_or_create_profile(self, user, **data):
    try:
      profile = self.get(user=user)
    except Exception:
      profile = self.create(user=user, **data)
    return profile


class Profile(models.Model):
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
  gender = models.PositiveIntegerField(_('Gender'), choices=GENDER_CHOICES, default=GENDER.UNDEFINED)
  avatar = models.ImageField(
      _('Profile avatar'),
      upload_to='profile_pics/%Y-%m-%d/',
      null=True,
      blank=True,
      max_length=255,
      validators=[validate_avatar]
  )
  major_intake = models.CharField(_('Major - Intake'), default='', max_length=255)
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
  message = models.CharField(_('Message to VGU Alumni Community'), null=True, blank=True, default='', max_length=1000)
  linkedin_url = models.URLField(_('LinkedIn Profile URL'), null=True, blank=True)

  objects = ProfileManager()

  def __str__(self):
    return "{}'s profile".format(self.user)

  @property
  def name(self):
    user = getattr(self, 'user', None)
    if user:
      return "%s %s" % (user.first_name, user.last_name)
    return None