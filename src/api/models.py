import binascii
import os

from django.db import models
from django.db.models.manager import Manager

from django.utils import timezone
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _


class TokenManager(Manager):
  pass


@python_2_unicode_compatible
class Token(models.Model):
  """
  The default authorization token model
  """
  key = models.CharField(_("Key"), max_length=40, primary_key=True)
  user = models.ForeignKey(
    settings.AUTH_USER_MODEL, related_name='auth_token',
    on_delete=models.CASCADE, verbose_name=_("User"),
  )
  created_at = models.DateTimeField(_("Created"), auto_now_add=True)
  updated_at = models.DateTimeField(_("Updated at"), default=timezone.now)

  objects = TokenManager()

  # TODO: Add cache for token
  def __str__(self):
    return self.key

  class Meta:
    verbose_name = _("Token")
    verbose_name_plural = _("Tokens")

  def save(self, *args, **kwargs):
    if not self.key:
      self.key = self.generate_key()
    self.updated_at = timezone.now()
    return super(Token, self).save(*args, **kwargs)

  def generate_key(self):
    return binascii.hexlify(os.urandom(20)).decode()
