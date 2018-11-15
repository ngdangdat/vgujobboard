import os
from os import path, makedirs
from hashlib import md5

from PIL import Image

from django.db import models
from django.core.files.base import File
from django.conf import settings
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from core.validators import validate_phone_number, validate_intake, validate_avatar
from core.models import ModelDiffMixin
from core.modules.storage import get_storage_path, get_cdn_url
from core.modules.image import crop_it

from user.const import GENDER, GENDER_CHOICES, MAJOR, MIN_INTAKE

AVATAR_SIZE = 256, 256
PROFILE_AVATAR_KEY = settings.PROFILE_AVATAR_KEY

def save_temp_avatar(file_stream):
  """
  Save avatar to upload dir
  """
  temp_dir = path.join(settings.BASE_DIR, settings.UPLOAD_TEMP_DIR)
  if not path.exists(temp_dir):
    makedirs(temp_dir)
  file_path = path.join(temp_dir, file_stream.name)
  with open(file_path, '+wb') as destination:
    for chunk in file_stream.chunks():
      destination.write(chunk)
  return '%s%s' % (PROFILE_AVATAR_KEY, file_path)


def save_avatar(file_path):
  """
  :param file_path:
  :return: url
  """
  file_name = path.basename(file_path)
  _, ext = path.splitext(file_name)
  time_in_bytes = bytes(str(timezone.now()), 'utf-8')
  file_name = '%s_%s%s' % (
    PROFILE_AVATAR_KEY,
    md5(time_in_bytes).hexdigest(),
    ext,
  )

  # Crop avatar
  img = Image.open(file_path)
  img = crop_it(img, AVATAR_SIZE)
  img.save(file_path)

  img_data = open(file_path, 'rb')
  os.remove(file_path)
  img_file = File(img_data)
  return file_name, img_file


class ProfileManager(models.Manager):

  def get_or_create_profile(self, user, **data):
    try:
      profile = self.get(user=user)
    except Exception:
      profile = self.create(user=user, **data)
    return profile


class Profile(ModelDiffMixin, models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
  gender = models.PositiveSmallIntegerField(_('Gender'), choices=GENDER_CHOICES, default=GENDER.UNDEFINED)
  birthday = models.DateField(_('Birthday'), null=True, default=None, blank=True,)
  avatar = models.ImageField(
      _('Profile avatar'),
      upload_to='avatars/',
      null=True,
      blank=True,
      max_length=255,
      validators=[validate_avatar],
  )
  major = models.PositiveSmallIntegerField(_('Major'), choices=MAJOR.choices, default=MAJOR.UNDEFINED,)
  intake = models.PositiveSmallIntegerField(_('Intake'), default=MIN_INTAKE, validators=[validate_intake])
  phone_number = models.CharField(_('Phone Number'),
    default=None,
    max_length=15,
    blank=True,
    null=True,
    validators=[validate_phone_number],
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

  def save(self, *args, **kwargs):
    self.clean()
    super(Profile, self).save(*args, **kwargs)

  def clean(self):
    if self.avatar:
      name = self.avatar.name
      if name.startswith(PROFILE_AVATAR_KEY):
        name = name.replace(PROFILE_AVATAR_KEY, '')
        name_to_save, avatar = save_avatar(name)
        self.avatar.save(name_to_save, avatar, save=False)
        self.avatar.name = get_cdn_url(self.avatar.name)
