from django.contrib.auth.models import (AbstractBaseUser, PermissionsMixin, update_last_login, Group)

class AbstractUser(AbstractBaseUser, PermissionsMixin):
  class Meta:
    abstract = True
