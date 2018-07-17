from django.db import models

# Create your models here.
class Email(models.Model):
    email = models.CharField(('Email'), max_length=255, unique=True, null=True, blank=True)
