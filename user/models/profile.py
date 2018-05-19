from django.db import models
from django.conf import settings

from django.utils.translation import ugettext_lazy as _

from core.validators import validate_phone_number
from user.const import GENDER, GENDER_CHOICES

class Profile(models.Model):
  """
  Fields:
  - major_intake
  - phone_number
  - state
  - country
  - office
  - job_title
  - title
  - gender
  - message
  """
  user = models.OneToOneField(settings.AUTH_USER_MODEL, primary_key=True, on_delete=models.CASCADE)
  gender = models.PositiveIntegerField(_('Gender'), choices=GENDER_CHOICES, default=GENDER.UNDEFINED)
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
  office = models.CharField(_('Organization you are working for/studying at'), default='', max_length=255)
  job_title = models.CharField(_('Position/Major'), default='', max_length=255)
  message = models.CharField(_('Message to VGU Alumni Community'), null=True, blank=True, default='', max_length=1000)

  def __str__(self):
    return "{}'s profile".format(self.user)
