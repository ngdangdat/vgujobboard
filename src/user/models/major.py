from django.db import models

from user.const import DEGREE, DEGREE_CHOICES

from django.utils.translation import ugettext_lazy as _


class Major(models.Model):
  name = models.CharField(default=None, max_length=100, blank=True, null=True, )
  shorten = models.CharField(default=None, max_length=20, blank=True, null=True, unique=True, )
  start_from = models.PositiveSmallIntegerField(_('Start Year'), blank=True, null=True, )
  degree = models.PositiveSmallIntegerField(_('Degree'), blank=True, null=True, choices=DEGREE_CHOICES, )
  objects = models.Manager()

  def __str__(self):
    degree_display = DEGREE.get_name(self.degree)
    return "%s (%s)" % (self.name, degree_display)

  @property
  def degree_display(self):
    return DEGREE.get_name(self.degree)
